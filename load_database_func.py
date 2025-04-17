from langchain_community.document_loaders import Docx2txtLoader

def load_documents(input_docs_paths):
    for path in input_docs_paths:
        loader = Docx2txtLoader(path)
    return loader.load()