from langchain_community.embeddings.ollama import OllamaEmbeddings

def get_embedding_function(input_model):
    embeddings = OllamaEmbeddings(model=input_model)
    return embeddings