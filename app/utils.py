from pathlib import Path
from app.models import Document


DOCUMENTS_DIR = Path("data/documents")

def generate_documents():
    """Read documents one at a time and yield Document objects."""
    for file_path in DOCUMENTS_DIR.glob("*.txt"):
        try:
            content = file_path.read_text(encoding="utf-8")

            document = Document(
                document_id=file_path.stem,
                content=content,
                source=file_path.name
            )
            yield document
        except Exception as e:
            print(f"Error reading document {file_path}: {e}")
            continue

