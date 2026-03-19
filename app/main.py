from fastapi import FastAPI
from app.routes import ocr_routes

app = FastAPI(title="DocStrange OCR Microservice")

app.include_router(ocr_routes.router, prefix="/api/v1")

@app.get("/health")
def health():
    return {"status": "online", "engine": "docstrange-1.1.8"}