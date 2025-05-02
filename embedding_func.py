from langchain_ollama import OllamaEmbeddings

def get_embedding_function(input_model):
    embeddings = OllamaEmbeddings(model=input_model)
    return embeddings