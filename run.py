from app.utils import generate_documents

for document in generate_documents():
    print(f"Document ID: {document.document_id}")
    print(f"Content: {document.content}")
    print(f"Source: {document.source}")
    print("-" * 50)
    print("\n")