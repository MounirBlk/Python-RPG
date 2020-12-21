#coding: utf-8
import socket

host, port =('localhost',5566)
socket= socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    
try:
    socket.connect((host, port))
    print("Client connecté !")
    data = "Bonjour"
    data = data.encode("utf8")
    socket.sendall(data)
    

except ConnectionRefusedError:
    print("Connexion au serveur échouée !")
finally:
    socket.close()