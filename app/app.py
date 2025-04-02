from fastapi import FastAPI, HTTPException, Request
import uvicorn
from app.controlador.PractitionersCrud import GetPractitionersById,WritePractitioners
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permitir solicitudes desde cualquier origen
    allow_credentials=True,
    allow_methods=["*"],  # Permitir todos los métodos (GET, POST, etc.)
    allow_headers=["*"],  # Permitir todos los encabezados
)

@app.get("/practitioner/{practitioner_id}", response_model=dict)
async def get_practitioner_by_id(practitioner_id: str):
    status, practitioner = GetPractitionersById(practitioner_id)
    if status == 'success':
        return practitioner  # Retorna la información del médico
    elif status == 'notFound':
        raise HTTPException(status_code=404, detail="Practitioner not found")
    else:
        raise HTTPException(status_code=500, detail=f"Internal error. {status}")

@app.post("/practitioner", response_model=dict)
async def add_practitioner(request: Request):
    new_practitioner_dict = dict(await request.json())
    status, practitioner_id = WritePractitioners(new_practitioner_dict)
    if status == 'success':
        return {"_id": practitioner_id}  # Retorna el ID del médico
    else:
        raise HTTPException(status_code=500, detail=f"Error al validar: {status}")

if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=8000)

