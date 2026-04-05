import os

from dotenv import load_dotenv
from docstrange import DocumentExtractor
from app.schemas.response_model import ACTA_SCHEMAS

load_dotenv()

API_KEY = os.getenv("DOCTSTRANGE_API_KEY")

if not API_KEY:
    raise RuntimeError("Falta la variable de entorno DOCTSTRANGE_API_KEY.")

extractor = DocumentExtractor(api_key=API_KEY)

class DocumentService:
    @staticmethod
    def procesar_documento(file_path: str, tipo: str):
        if tipo not in ACTA_SCHEMAS:
            raise ValueError(f"Tipo '{tipo}' no soportado")

        result = extractor.extract(file_path)
        raw_text = result.extract_markdown()

        if not raw_text:
            raise ValueError("No se pudo extraer texto del documento localmente.")

        return result.extract_data(json_schema=ACTA_SCHEMAS[tipo])