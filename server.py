import socket
import threading
import os

# Definir el directorio donde estarán los archivos para ser enviados
DIRECTORY = r'C:\Users\Glori\OneDrive\Escritorio\backend\socket_cmd'  # Ruta absoluta

def handle_client(client_socket):
    try:
        while True:
            data = client_socket.recv(1024)
            if not data:
                break
            command = data.decode('utf-8').strip()
            print(f"Received command: {command}")
            
            if command == "lsFiles":
                # Listar archivos en el directorio 'DIRECTORY'
                if os.path.exists(DIRECTORY):
                    files = os.listdir(DIRECTORY)
                    response = "\n".join(files) if files else "No files found."
                else:
                    response = f"Directory '{DIRECTORY}' not found."
                client_socket.sendall(response.encode('utf-8'))
            
            elif command.startswith("get "):
                # Extraer nombre de archivo del comando
                filename = command.split(" ")[1]
                file_path = os.path.join(DIRECTORY, filename)
                
                if os.path.isfile(file_path):
                    client_socket.sendall(b"READY")  # Avisar al cliente que el archivo está disponible
                    
                    # Enviar archivo en bloques de 1024 bytes
                    with open(file_path, 'rb') as f:
                        while True:
                            chunk = f.read(1024)
                            if not chunk:
                                break
                            client_socket.sendall(chunk)
                    print(f"Sent file: {filename}")
                    client_socket.sendall(b"EOF")  # Enviar fin de archivo
                else:
                    client_socket.sendall(b"File not found.")
    
    finally:
        client_socket.close()

def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = '127.0.0.1'
    port = 12345
    server_socket.bind((host, port))
    server_socket.listen(5)
    print(f"Server listening on {host}:{port}")

    while True:
        client_socket, client_address = server_socket.accept()
        print(f"Accepted connection from {client_address}")
        client_handler = threading.Thread(target=handle_client, args=(client_socket,))
        client_handler.start()

if __name__ == "__main__":
    main()
