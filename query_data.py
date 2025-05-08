import argparse
from langchain_chroma import Chroma
from langchain.prompts import ChatPromptTemplate
from langchain_ollama import OllamaLLM
from embedding_func import get_embedding_function


# path to the local database to fetch information populate by running update_database.py 
DB_PATH = "database"

# prompt feeding the model to get desired response, context is fetch from database, and question is user input
PROMPT_TEMPLATE = """
You are an informational agent dedicated to educating users about the Ogiek community. Given the most relevant documentations and a question either in English or Swahili from the user, 
you must answer the question in English if asked in English, in Swahili if asked in Swahili. Your answer should be short, no more than 190 characters. If a question is asked that does not relate to the documentation given,
tell the users you can only answer on what you are trained for.

Here are the documentations:
 
{context}
 
---
 
Here  is the question asked by the user: {question}

AGAIN, THE MOST IMPORTANT THINGS ARE: ANSWER IN LESS THAN 190 CHARACTERS, IN SWAHILI IF THE QUESTION IS IN SWAHILI, and only give answer derived from the source.
"""


def main():
    # grab query for chatbot from terminal
    parser = argparse.ArgumentParser()
    parser.add_argument("query_text", type=str, help="The query text.")
    args = parser.parse_args()
    query_text = args.query_text
    query_rag(query_text)


def query_rag(query_text: str):

    # can change the model here
    model = "mannix/llamax3-8b-alpaca"

    # prepare the DB.
    embedding_function = get_embedding_function(input_model= model)
    db = Chroma(persist_directory=DB_PATH, embedding_function=embedding_function)

    # search the DB.
    results = db.similarity_search_with_score(query_text, k=3) 


    # Make sure response is relevant
    if len(results) == 0 or results [0][1] < 0.7:
        print("Unable to find matching results.")
        return

    context_text = "\n\n---\n\n".join([doc.page_content for doc, _score in results])
    prompt_template = ChatPromptTemplate.from_template(PROMPT_TEMPLATE)
    prompt = prompt_template.format(context=context_text, question=query_text)
    # print(prompt)


    ollama_model = OllamaLLM(model = model)
    response_text = ollama_model.invoke(prompt)

    sources = [doc.metadata.get("id", None) for doc, _score in results]
    formatted_response = f"\n{model}:{response_text}\n\nSources: {sources}"
    print(f"\n{model}: {response_text}\n")
    # print(formatted_response)
    return response_text


if __name__ == "__main__":
    main()  