from dotenv import load_dotenv
import os
from langchain.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser
from langgraph.graph import StateGraph, END

load_dotenv()
os.environ.get("GOOGLE_API_KEY")

llm = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash",
    temperature=0.7
)

template_text = (
    ""
)
prompt = PromptTemplate(
    input_variables=["nome", "pergunta"],
    template=template_text
)

qa_chain = prompt | llm | StrOutputParser()
