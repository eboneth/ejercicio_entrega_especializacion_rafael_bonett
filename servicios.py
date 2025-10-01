from abc import ABC, abstractmethod
from notifications import NotificaClientes, Cliente, SMSNotification, EmailNotification

#Factory Method
# Clase base del juego
class Juego(ABC):
    def __init__(self, nombre: str, precio: float)-> None:
        self.nombre = nombre
        self.precio = precio
    
    #Este metodo procesa la compra y notifica al cliente
    @abstractmethod
    def procesar_compra(self, notifica_clientes: NotificaClientes)->None:
        pass

# Metodo que sirve para comprar juegos fisicos y notifica por sms
class JuegoFisico(Juego):
    def __init__(self, nombre: str, precio: float, telefono: str)-> None:
        super().__init__(nombre, precio)
        self.telefono = telefono

    def procesar_compra(self, notifica_clientes: NotificaClientes)->None:
        cliente = Cliente(SMSNotification(), self.telefono)
        notifica_clientes.attach(cliente)
        
        notifica_clientes.notifica(f"Hemos recibido tu compra del juego: {self.nombre}, estamos preparando tu envio!!!! xD")

# Metodo que sirve para comprar juegos digital y notifica por email
class JuegoDigital(Juego):
    def __init__(self, nombre: str, precio: float, email: str)-> None:
        super().__init__(nombre, precio)
        self.email = email

    def procesar_compra(self, notifica_clientes: NotificaClientes)->None:
        cliente = Cliente(EmailNotification(), self.email)
        notifica_clientes.attach(cliente)
        
        notifica_clientes.notifica(f"Has comprado: {self.nombre}, este es tu codigo de descarga: XXXX-YYYY-1234-5678 Disfrutalo")

##decorator
# metodo que decora la compra de un juego fisico para envolverlo para regalo
class EnvolverParaRegalo(Juego):
    def __init__(self, juego:Juego)->None:
        self.juego = juego
    
    def procesar_compra(self, notifica_clientes: NotificaClientes)->None:
        self.juego.procesar_compra(notifica_clientes)
        notifica_clientes.notifica(f"El juego sera enviado para dar como regalo xD!!!!")

##Factory
class ElegirCompra:
    @staticmethod
    def crear_juego(tipo: str, nombre: str, precio: float, email = None, telefono = None, envolver = False):
        if(tipo == "Fisico" or tipo == "fisico" or tipo == "FISICO"):
            juego = JuegoFisico(nombre, precio, telefono)
            if envolver:
                juego = EnvolverParaRegalo(juego)
            return juego
        elif(tipo == "Digital" or tipo == "digital" or tipo == "DIGITAL"):
            juego = JuegoDigital(nombre, precio, email)
            return juego
        else:
            raise ValueError(f"Tipo de juego desconocido: {tipo}")