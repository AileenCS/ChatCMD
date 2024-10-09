# ChatCMD 
Este proyecto muestra  cómo un cliente y un servidor pueden comunicarse usando sockets en Python. El servidor puede conectarse con varios clientes al mismo tiempo y ejecutar los comandos que envía cada cliente, como mostrar una lista de archivos o enviar un archivo específico.

## Características

- **Comandos disponibles**:
  - `lsFiles`: Lista los archivos disponibles en la carpeta del servidor.
  - `get <archivo>`: Descarga un archivo del servidor y lo guarda en la carpeta `download` en el cliente.
  
- El servidor maneja múltiples conexiones a través de **threads**, y cada cliente puede enviar comandos sin que afecte a otros clientes conectados.

## Requisitos
- Python 3.x

## Instalación

1. Clona este repositorio en tu máquina local:

   ```bash
   git clone https://github.com/usuario/ChatCMD.git
   ```
2. Dirigete a tu cmd
Navega al directorio del proyecto:
```bash 
cd ChatCMD
```
Asegúrate de que los archivos del servidor se encuentran en la carpeta:

C:\Users\Glori\OneDrive\Escritorio\backend\socket_cmd

Para iniciar el servidor, ejecuta el siguiente comando en la terminal:

```bash 
python server.py
```
El servidor escuchará en 127.0.0.1 en el puerto 12345 y esperará a que los clientes se conecten.

Ejecución del Cliente
Para ejecutar el cliente, abre una nueva terminal y ejecuta:
```bash 
python client.py
```
Una vez dentro del servidor, el cliente puede enviar los siguientes comandos:
"Enter your command (lsFiles or get <filename>) donde:
lsFiles: Muestra una lista de los archivos disponibles en el servidor.
get <nombre_de_archivo>: Descarga un archivo desde el servidor. El archivo descargado se guardará en una carpeta llamada download en el cliente.


![Texto alternativo](ruta/de/la/imagen)

![image](https://github.com/user-attachments/assets/750eb4aa-8c2b-46df-8c31-07363daef912)
