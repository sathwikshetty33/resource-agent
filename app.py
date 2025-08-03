import os
import shutil
import logging
from fastapi import FastAPI, UploadFile, File
from fastapi.responses import JSONResponse
from dotenv import load_dotenv  # <--- NEW
from agent.agent import *
from langchain_community.document_loaders import PyPDFLoader
from langchain.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq
from langchain.chains import LLMChain
from tavily import TavilyClient  # Direct Tavily API usage


# Logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger("pdf-processor")


app = FastAPI(
    title="PDF to Resources API",
    description="Extracts topics from a PDF and finds relevant websites"
)

@app.post("/process-pdf")
async def process_pdf(file: UploadFile = File(...)):
    logger.info(f"Received file: {file.filename}")
    temp_pdf = f"temp_{file.filename}"
    with open(temp_pdf, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    logger.info("File saved temporarily.")

    try:
        agent = Agent()
        return JSONResponse(content=agent.run(temp_pdf))
    except Exception as e:
        logger.error(f"Error processing PDF: {e}")
        return JSONResponse(content={"error": str(e)}, status_code=500)
       
