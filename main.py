from fastapi import FastAPI
from models import ComprarModel
from commands import ComprarJuegoCommand

app = FastAPI(title="Tienda de Juegos", version="1.0.0")

@app.post("/comprar_juego/")
def comprar_juego(compra: ComprarModel):
    command = ComprarJuegoCommand(compra)
    return command.execute()
