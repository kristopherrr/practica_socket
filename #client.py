#client.py
import socket

host = '192.168.1.51'
port = 8050

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))

mensaje = "Hola!, Servidor"
s.send(mensaje.encode())

datos_recibidos = s.recv(1024).decode()
print(f"Datos recibidos del servidor: {datos_recibidos}")

s.close()