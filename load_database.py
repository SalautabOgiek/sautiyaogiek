from langchain_community.document_loaders import Docx2txtLoader

loader = Docx2txtLoader("./data/data/Basic_Messages_Ogiek_SMS.docx")

data = loader.load()