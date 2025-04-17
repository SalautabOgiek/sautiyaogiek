from langchain_community.document_loaders import Docx2txtLoader


def load_documents(input_docs_paths):
    # This will hold all the Document objects from every file
    all_documents = []

    # Go through each file path in the input list
    for path in input_docs_paths:
        # Create a loader for that .docx file
        loader = Docx2txtLoader(path)
        
        # Load returns a list of Document objects for that file
        current_file_documents = loader.load()
        
        # Add each Document into our master list
        for document in current_file_documents:
            all_documents.append(document)

    # After the loops, return the full list
    return all_documents

# Example usage:
# paths = [
#     "./data/data/Basic_Messages_Ogiek_SMS.docx",
#     "./data/data/Swahili Translation datasets.docx",
#     "./data/data/Training.JSONL Format for Swahili Training Data.docx",
# ]

# all_docs = load_documents(paths)
# print(f"Loaded {len(all_docs)} documents in total")