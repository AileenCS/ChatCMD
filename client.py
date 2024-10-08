import socket
import os

def main():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = '127.0.0.1'
    port = 12345

    try:
        client_socket.connect((host, port))
        print("Connected to the server.")
        
        while True:
            command = input("Enter your command (lsFiles or get <filename>): ")
            client_socket.sendall(command.encode('utf-8'))

            if command.startswith("get "):
                filename = command.split(" ")[1]
                file_path = os.path.join('download', filename)

                # Crear carpeta 'download' si no existe
                if not os.path.exists('download'):
                    os.makedirs('download')
                    print("Created 'download' directory.")

                # Esperar confirmación del servidor
                response = client_socket.recv(1024).decode('utf-8')
                if response == "READY":
                    # Recibir archivo en bloques de 1024 bytes
                    with open(file_path, 'wb') as f:
                        print(f"Receiving file: {filename}")
                        while True:
                            data = client_socket.recv(1024)
                            if data == b"EOF":  # Chequea si es el final del archivo
                                break
                            f.write(data)
                    print(f"File '{filename}' has been downloaded to 'download/'")
                else:
                    print(f"Server response: {response}")
            
            else:
                # Recibir y mostrar respuesta para otros comandos (como 'lsFiles')
                response = client_socket.recv(1024).decode('utf-8')
                print(f"Server response: {response}")

    except Exception as e:
        print(f"An error occurred: {str(e)}")
    finally:
        client_socket.close()
        print("Connection closed.")

if __name__ == "__main__":
    main()
