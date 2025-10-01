from abc import ABC, abstractmethod

#Strategy
# Clase base de las notificaciones que envia la tienda
class NotificationStore(ABC):
        @abstractmethod
        def enviar(self, mensaje: str, destino: str)->None:
            pass

# Clase para notificaciones por SMS
class SMSNotification(NotificationStore):
        def enviar(self, mensaje: str, destino: str)->None:
            print(f"Mensaje Enviado a: {destino}: {mensaje}")

# Clase para notificaciones por Email
class EmailNotification(NotificationStore):
        def enviar(self, mensaje: str, destino: str)->None:
            print(f"Email Enviado a: {destino}: {mensaje}")

#Observer
# Clase base del observador     
class NotificationClient(ABC):
        @abstractmethod
        def recibir(self, mensaje: str)->None:
            pass

# Clase que representa el cliente
# Guardamos  el medio por el que notifica y a quien se envia
class Cliente(NotificationClient):
        def __init__(self, store_notificacion: NotificationStore, destino: str)->None:
            self.store_notificacion = store_notificacion
            self.destino = destino

        def recibir(self, mensaje: str)->None:
            self.store_notificacion.enviar(mensaje, self.destino)

# Sujeto que notifica a los clientes
class NotificaClientes:
        def __init__(self)->None:
            self._clientes = []
    
        def attach(self, cliente: NotificationClient)->None:
            self._clientes.append(cliente)
        
        def notifica(self, mensaje: str)->None:
            for o in self._clientes:
                o.recibir(mensaje)