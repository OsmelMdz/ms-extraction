from docstrange import DocumentExtractor
from app.schemas.response_model import ACTA_SCHEMAS

extractor = DocumentExtractor(api_key="a7ccc8d4-589d-44dc-b3fb-56898e225435")

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