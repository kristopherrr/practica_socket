# server.py
import socket

host = '0.0.0.0'  # Escucha en todas las interfaces
port = 8050 #el numero de puerto en el que el servidor aceptara la conexión entrante

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Crea un objeto de socket, AF_INET indica que estamos utilizando IPv4, y SOCK_STREAM especifica que es un socket TCP. 
s.bind((host, port)) #Vincula el socket a la dirección IP y al puerto especificados.
s.listen(1)  # Escucha una conexión entrante 1na a la vez

print(f"Esperando conexiones en {host}:{port}...")

conn, addr = s.accept() # Acepta una conexión entrante. conn es un nuevo objeto de socket que representa la conexión con el cliente, y addr contiene la dirección IP y el puerto del cliente.
print(f"Conexión establecida desde {addr}")

data = conn.recv(1024).decode() #Recibe datos del cliente. En este caso, se espera recibir hasta 1024 bytes de datos y se decodifican a una cadena
print(f"Datos recibidos: {data}")

conn.send("¡Hola, cliente!".encode()) #Envía una respuesta al cliente. La cadena “¡Hola, cliente!”
conn.close() #Cierra la conexión con el cliente.
