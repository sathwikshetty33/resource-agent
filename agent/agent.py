import os
import shutil
import logging
from fastapi import FastAPI, UploadFile, File
from fastapi.responses import JSONResponse
from dotenv import load_dotenv  # <--- NEW

from langchain_community.document_loaders import PyPDFLoader
from langchain.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq
from langchain.chains import LLMChain
from tavily import TavilyClient  # Direct Tavily API usage
from.prompt import prompt  # Importing the prompt from agent/prompt.py
# Logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger("pdf-processor")
load_dotenv()  # <--- Load variables from .env

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")

class Agent:
    def __init__(self):
        self.llm =  ChatGroq(model="gemma2-9b-it", temperature=0.0)
        self.summ_chain = LLMChain(prompt=prompt, llm=self.llm)
        self.tavily = TavilyClient(api_key=TAVILY_API_KEY)
    def run(self, temp_pdf):
        # Implement the logic to run the agent with the provided input data
        try:
        # 1. Load first 3 pages
            logger.info("Loading PDF...")
            loader = PyPDFLoader(temp_pdf)
            docs = loader.load()
            first_three_pages = docs[:3]
            logger.info(f"PDF loaded. Processing {len(first_three_pages)} pages.")

            # 2. Merge pages into a single chunk for LLM
            combined_text = "\n".join(doc.page_content for doc in first_three_pages)
            logger.info("Extracting topics from PDF...")
            
            # 🔹 Single Groq call
            out = self.summ_chain.invoke({"text": combined_text})
            extracted_text = out["text"]

            # 3. Clean topics
            topics = [t.strip("-• ").strip() for t in extracted_text.split("\n") if t.strip()]
            distinct_topics = list(dict.fromkeys(topics))  # preserve order
            logger.info(f"Extracted topics: {distinct_topics}")

            if not distinct_topics:
                return JSONResponse(content={"error": "No topics extracted from the PDF."})

            # 4. Direct Tavily search per topic (no Groq used)
            resources = {}
            for i, topic in enumerate(distinct_topics, start=1):
                logger.info(f"Searching Tavily for topic {i}/{len(distinct_topics)}: {topic}")
                result = self.tavily.search(topic, max_results=5)  # returns JSON with links/snippets
                resources[topic] = [item["url"] for item in result["results"]]

            logger.info("Processing complete. Returning JSON response.")
            return resources
        finally:
            if os.path.exists(temp_pdf):
                os.remove(temp_pdf)
                logger.info("Temporary file removed.")