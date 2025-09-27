from abc import ABC, abstractmethod

#Strategy
class NotificationStore(ABC):
        @abstractmethod
        def enviar(self, mensaje: str, destino: str)->None:
            pass

#Observer        
class NotificationClient(ABC):
        @abstractmethod
        def recibir(self, mensaje: str)->None:
            pass
        
class SMSNotification(NotificationStore):
        def enviar(self, mensaje: str, destino: str)->None:
            print(f"Mensaje Enviado a: {destino}: {mensaje}")

class EmailNotification(NotificationStore):
        def enviar(self, mensaje: str, destino: str)->None:
            print(f"Email Enviado a: {destino}: {mensaje}")

class Cliente(NotificationClient):
        def __init__(self, store_notificacion: NotificationStore, destino: str)->None:
            self.store_notificacion = store_notificacion
            self.destino = destino

        def recibir(self, message: str)->None:
            self.store_notificacion.enviar(mensaje, self.destino)
    
class NotificaClientes:
        def __init__(self)->None:
            self._clientes = []
            
        def attach(self, cliente: Cliente)->None:
            self._clientes.append(cliente)
        
        def notifica(self, mensaje: str)->None:
            for o in self._clientes:
                o.update(mensaje)