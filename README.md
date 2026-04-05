# ms-extraction

Microservicio de OCR y extraccion estructurada de metadatos para actas civiles usando FastAPI y DocStrange.

## 1. Objetivo

Este proyecto expone una API HTTP para:

- Recibir un archivo (PDF o imagen) mediante multipart/form-data.
- Extraer texto con DocStrange OCR.
- Convertir el contenido en JSON estructurado segun un esquema por tipo de acta.

Tipos soportados:

- nacimiento
- matrimonio
- defuncion

## 2. Alcance Funcional

El servicio implementa:

- Endpoint de salud para monitoreo.
- Endpoint de extraccion con validacion de tipo de acta.
- Eliminacion del archivo temporal al finalizar cada solicitud.

El servicio NO implementa:

- Persistencia de resultados en base de datos.
- Autenticacion de clientes HTTP.
- Versionado adicional fuera de /api/v1.

## 3. Arquitectura

- app/main.py: inicializacion de FastAPI y registro de rutas.
- app/routes/ocr_routes.py: capa HTTP (entrada/salida, manejo de errores, archivo temporal).
- app/services/document_service.py: integracion con DocStrange y extraccion estructurada.
- app/schemas/response_model.py: definicion de esquemas por tipo de acta.
- Dockerfile y docker-compose.yml: empaquetado y ejecucion en contenedor.

## 4. Requisitos

- Docker Desktop (o Docker Engine + Compose plugin)
- Conexion a internet para resolver dependencias en build

## 5. Ejecucion Rapida (Docker)

1. Clonar el repositorio:

```bash
git clone https://github.com/OsmelMdz/ms-extraction.git
cd ms-extraction
```

2. Levantar el servicio:

```bash
docker compose up --build -d
```

3. Verificar salud:

```bash
curl http://localhost:8000/health
```

4. Ver logs:

```bash
docker compose logs -f
```

5. Apagar servicio:

```bash
docker compose down
```

## 6. Contrato de API

### 6.1 Health Check

- Metodo: GET
- Ruta: /health
- Respuesta esperada (200):

```json
{
  "status": "online",
  "engine": "docstrange-1.1.8"
}
```

### 6.2 Extraccion de Metadatos

- Metodo: POST
- Ruta: /api/v1/extract
- Content-Type: multipart/form-data

Parametros:

- tipo (string, requerido): nacimiento | matrimonio | defuncion
- file (binary, requerido): archivo de entrada

Ejemplo en Linux/macOS:

```bash
curl -X POST "http://localhost:8000/api/v1/extract" \
  -F "tipo=nacimiento" \
  -F "file=@./uploads/ejemplo.pdf"
```

Ejemplo en Windows PowerShell:

```powershell
curl.exe -X POST "http://localhost:8000/api/v1/extract" -F "tipo=nacimiento" -F "file=@uploads/ejemplo.pdf"
```

Respuesta exitosa (200):

```json
{
  "status": "success",
  "filename": "ejemplo.pdf",
  "metadata": {
    "datos_del_registro": {},
    "datos_de_la_acta": {}
  }
}
```

Codigos de respuesta:

- 200: extraccion completada.
- 400: solicitud invalida (por ejemplo, tipo no soportado o contenido no extraible).
- 500: error interno de procesamiento.

## 7. Configuracion Operativa

### 7.1 Directorio de carga

La ruta de almacenamiento temporal puede configurarse con la variable de entorno UPLOAD_DIR.

- Valor por defecto: /app/uploads

### 7.2 Volumenes de Docker Compose

- ./uploads -> /app/uploads
- ./docstrange_models -> /root/.cache/docstrange

### 7.3 API Key de DocStrange

La API key DEBE definirse en la variable de entorno `DOCTSTRANGE_API_KEY`.

La clave DEBE generarse en la plataforma oficial de DocStrange/Nanonets, en la siguiente ruta:

https://docstrange.nanonets.com/app

Ejemplo en `.env`:

```env
DOCTSTRANGE_API_KEY=tu_clave_aqui
```

El archivo `.env` NO DEBE subirse al repositorio.

## 8. Estructura del Proyecto

```text
.
|-- app/
|   |-- main.py
|   |-- routes/
|   |   `-- ocr_routes.py
|   |-- schemas/
|   |   `-- response_model.py
|   `-- services/
|       `-- document_service.py
|-- docker-compose.yml
|-- Dockerfile
|-- requirements.txt
`-- uploads/
```

## 9. Buenas Practicas de Uso

- El cliente DEBE enviar el campo tipo en valores soportados.
- El cliente DEBE enviar archivos legibles para OCR.
- El servicio NO DEBE usar archivos temporales despues de responder (se eliminan al finalizar cada request).
- En produccion, la API key NO DEBE quedar hardcodeada en repositorio.

## 10. Glosario

- OCR: reconocimiento optico de caracteres sobre documentos.
- Metadata: estructura JSON resultante de la extraccion.
- Tipo de acta: clasificacion funcional del documento (nacimiento, matrimonio, defuncion).
- DocumentExtractor: componente de DocStrange que procesa el archivo y expone extract_markdown y extract_data.

## 11. Estado del Proyecto

Estado actual: funcional para pruebas locales y despliegue con Docker.

Pendientes recomendados para entorno productivo:

- Externalizar API key a variable de entorno.
- Agregar autenticacion para clientes del API.
- Incorporar pruebas automaticas (unitarias e integracion).
- Definir LICENSE y .gitignore segun politica de repositorio.
