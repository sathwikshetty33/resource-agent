from langchain.prompts import ChatPromptTemplate


prompt = ChatPromptTemplate.from_messages([
    ("system", "Extract 5 key topics or questions from the text as a bullet list."),
    ("user", "{text}")
])
