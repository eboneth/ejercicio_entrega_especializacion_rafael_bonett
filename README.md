# EJERCICIO PATRONES DE DISEÑO ESPECIALIZACION
## RAFAEL BONETT

Una tienda de videojuegos digital y fisico, cuando se haga una compra de juego fisico se envia un mensaje de texto informando los estados del envio, si la compra es de un juego digital debe enviar un correo electronico indicando el codigo de la descarga.
adicional a la compra de juego fisico me permita indicar si requiero que lo envuelvan como regalo.


# PATRONES DE DISEÑOS USADOS

## 1. Strategy: 
por que asi no mezclamos la logica de negocio con la forma como se envia la notificacion, si mañana queremos añadir un nuevo metodo ejemplo **"Whats app"** para notificar solo tengo que añadir la nueva estrategia **"WhatsAppNotification"** sin alterar el resto del codigo. 

## 2. Observer: 
Cuando pasa un evento por ejemplo **"Tu compra ha sido recibida"**, "tu pedido ha sido enviado" etc. con este patron avisa automaticamente a los interesados.

Se usa aqui por que un proceso de compra tiene varios estados y con este paton simplemente se notifica sin llenar el codigo de if y print, si mañana se quiere avisar a un sistema extra inventario por ejemplo simplemente se añade el observador.

## 3. Factory Method:
Se crea una "Fabrica" la cual decide si el juego que se va a comprar es **"fisico"** o **"digital"**.

## 4. Decorator: 
Al ser esto una funcion opcional al momento de hacer una compra fisica no creamos una clase **"JuegoFisicoEnvuelto"** en cambio usamos la clase **EnvolverParaRegalo** que devuelve juego Fisico con el mensaje **"El juego sera enviado para dar como regalo xD!!!!"** y esto sin duplicar codigo.

## 5. Command
La accion comprar juego es un comando **"ComprarJuegoCommand"** ese comando recibe la solicitud de compra, crea el juego, lo procesa y manda las notificaciones.


