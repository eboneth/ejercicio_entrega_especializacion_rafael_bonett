from pydantic import BaseModel
from typing import Optional

# Este metodo se usa para validar los datos de entrada, lo usa FastAPI para validar la informacion que manda el cliente
class ComprarModel(BaseModel):
    tipo: str
    nombre: str
    precio: float
    email: Optional[str] = None
    telefono: Optional[str] = None
    envolver: Optional[bool] = False