# llm  libarys 
import os
from langchain_huggingface import HuggingFaceEndpoint
from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq
from langchain_huggingface import HuggingFaceEmbeddings
from dotenv import load_dotenv
load_dotenv()

#llm 
qroq_llm = ChatGroq(
    model="openai/gpt-oss-20b",
    temperature=0
)

# embedding model
embeddings_huggingface = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)
# embedding  fuction 

def embeddings_model():
    return embeddings_huggingface



# max
def llm_max():

    return ChatGroq(

        model="openai/gpt-oss-120b",

        temperature=0,

        max_retries=2
    )

#  llm  min

def llm_mini(question):
    groq_llm = ChatGroq(
        model="openai/gpt-oss-20b",
        temperature=0
    )

    response = groq_llm.invoke(question)

    return response.content

# llm reasoning
def llm_reasoning(question):
    groq_llm = ChatGroq(
        model="qwen/qwen3.8-27b",
        temperature=0
    )

    response = groq_llm.invoke(question)

    return response.content