from models import ComprarModel
from servicios import ElegirCompra
from notifications import NotificaClientes

class Command:
    def execute(self)->None:
        pass

# Comando especifico para comprar el juego
class ComprarJuegoCommand(Command):
    # Guardamos la informacion de la compra
    def __init__(self, compra: ComprarModel)->None:
        self.compra = compra

    def execute(self)->str:
        notifica_clientes = NotificaClientes()
        #Creamos el juego
        juego = ElegirCompra.crear_juego(
            self.compra.tipo,
            self.compra.nombre,
            self.compra.precio,
            self.compra.email,
            self.compra.telefono,
            self.compra.envolver
        )
        # Procesamos la compra
        juego.procesar_compra(notifica_clientes)

        return (f"Compra del juego {self.compra.nombre} procesada con exito!")