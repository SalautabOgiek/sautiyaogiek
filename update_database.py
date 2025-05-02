import argparse
import os
import shutil
from langchain_community.document_loaders import Docx2txtLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.schema.document import Document
from embedding_func import get_embedding_function
from langchain_chroma import Chroma


# path to where the databases is
DB_PATH = "database"
# path to where the documents are
DATA_PATH = "data"
# model
model = "mannix/llamax3-8b-alpaca:latest"

def main():

    # clear database if "--clear" flag was raise after running the file in the cli
    parser = argparse.ArgumentParser()
    parser.add_argument("--reset", action="store_true", help="Reset the database.")
    args = parser.parse_args()
    if args.reset:
        print("Clearing Database")
        clear_database()

    # grab all paths to the document sends with.docx in data folder
    paths = []
    for filename in os.listdir(DATA_PATH):
        lower_filename = filename.lower()
        
        if lower_filename.endswith(".docx"):
            full_path = os.path.join(DATA_PATH, filename)
            paths.append(full_path)
    
    # create (or update) the data store.
    documents = load_documents(paths)
    chunks = split_documents(documents)
    add_to_database(chunks)

def load_documents(input_docs_paths):
    all_documents = []
    for path in input_docs_paths:
        loader = Docx2txtLoader(path)
        current_file_documents = loader.load()
        for document in current_file_documents:
            all_documents.append(document)
    return all_documents
    
def split_documents(documents: list [Document]):
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=50,
        length_function=len,
        add_start_index = True,
    )
    return text_splitter.split_documents(documents)

def add_to_database(chunks: list[Document]):
    db = Chroma(
        persist_directory=DB_PATH, embedding_function=get_embedding_function(model)
    )
    
    chunks_with_ids = calculate_chunk_ids(chunks)
    
    # Add or Update the documents.
    existing_items = db.get(include=[])  # IDs are always included by default
    existing_ids = set(existing_items["ids"])
    print(f"Number of existing documents in the database: {len(existing_ids)}")

    # Only add documents that don't exist in the DB.
    new_chunks = []
    for chunk in chunks_with_ids:
        if chunk.metadata["id"] not in existing_ids:
            new_chunks.append(chunk)

    if len(new_chunks):
        print(f"Adding {len(new_chunks)} new documents.")
        new_chunk_ids = [chunk.metadata["id"] for chunk in new_chunks]
        db.add_documents(new_chunks, ids=new_chunk_ids)
        print(f"Finished adding {len(new_chunks)} documents.")
    else:
        print("No new documents to add.")


# This func make all IDs like "./data/path.docx:6:2"
def calculate_chunk_ids(chunks):
    last_page_id = None
    current_chunk_index = 0

    for chunk in chunks:
        source = chunk.metadata.get("source")
        page = chunk.metadata.get("page")
        current_page_id = f"{source}:{page}"

        # If the page ID is the same as the last one, increment the index.
        if current_page_id == last_page_id:
            current_chunk_index += 1
        else:
            current_chunk_index = 0

        # Calculate the chunk ID.
        chunk_id = f"{current_page_id}:{current_chunk_index}"
        last_page_id = current_page_id

        # Add it to the page meta-data.
        chunk.metadata["id"] = chunk_id

    return chunks

def clear_database():
    if os.path.exists(DB_PATH):
        shutil.rmtree(DB_PATH)

if __name__ == "__main__":
    main()