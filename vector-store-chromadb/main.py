# from vectorstore tutorial
# https://python.langchain.com/docs/modules/data_connection/vectorstores/
import os
from dotenv import load_dotenv
from langchain_community.document_loaders import TextLoader
from langchain_openai import OpenAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain_community.vectorstores import Chroma

load_dotenv()
file_name = 'state-of-the-union-working.txt'

# Load the document, split it into chunks, embed each chunk and load it into the vector store.
raw_documents = TextLoader(file_name).load()
text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
documents = text_splitter.split_documents(raw_documents)
db = Chroma.from_documents(documents, OpenAIEmbeddings())

if __name__ == "__main__":
    query = "What did the president say about Ketanji Brown Jackson"
    docs = db.similarity_search(query)
    print(docs[0].page_content)