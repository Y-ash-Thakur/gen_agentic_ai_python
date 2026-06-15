#index.py

from dotenv import load_dotenv

from pathlib import Path
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_qdrant import QdrantVectorStore

load_dotenv()

#taking the pdf path
pdf_path = Path(__file__).parent / "Quantitative_Aptitude.pdf"

# Load this file in python program
loader = PyPDFLoader(file_path=pdf_path)
docs = loader.load()

# splits the docs into chunks
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=400 # taking some data from the previous chunk to understand the context of it
)

chnuks = text_splitter.split_documents(documents=docs)

# now we have to create a vector embeddings.
embedding_model = OpenAIEmbeddings(
    model="text-embedding-3-large"
)

#store it to the vectordb (qdrantdb)
vector_store = QdrantVectorStore.from_documents(
    documents=chnuks,
    embedding=embedding_model,
    url="http://localhost:6333",
    collection_name="learning_rag"
)

print("Indexing of documents done....")