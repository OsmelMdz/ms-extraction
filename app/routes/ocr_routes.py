from fastapi import APIRouter, UploadFile, File, Form, HTTPException
from app.services.document_service import DocumentService
import shutil
import os
import uuid

router = APIRouter()
UPLOAD_DIR = os.getenv("UPLOAD_DIR", "/app/uploads")
os.makedirs(UPLOAD_DIR, exist_ok=True)

@router.post("/extract")
async def extract_metadata(
    tipo: str = Form(..., description="Tipo de acta: nacimiento, matrimonio, defuncion"), 
    file: UploadFile = File(...)
):
    tipo_normalizado = tipo.strip().lower()
    safe_filename = os.path.basename(file.filename or "documento")
    file_id = uuid.uuid4()
    file_path = os.path.join(UPLOAD_DIR, f"{file_id}_{safe_filename}")
    
    try:
        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        data = DocumentService.procesar_documento(file_path, tipo_normalizado)
        
        return {
            "status": "success",
            "filename": safe_filename,
            "metadata": data
        }

    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e)) from e

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error en procesamiento local: {str(e)}") from e
    
    finally:
        await file.close()
        if os.path.exists(file_path):
            os.remove(file_path)