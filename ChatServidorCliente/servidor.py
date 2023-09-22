from socket import *
from random import randint
import pickle
import sys

def aceita(conexao):
    global clients
    #procura nome no dicionario
    disponivel = False
    while not disponivel:
        data = conexao.recv(1024)
        if not data: break
        dados = data.decode().spli(":")
        if len(dados) != 2:
            print("Formato invalido")
            return
        if dados[1] in clients:
            try:
                conexao.sendall("Not OK")
            except:
                print('caiu conexao')
                return
        else:
            disponivel = True
            try:
                conexao.sendall("OK")
            except:
                print('caiu conexao')
                return




    def avisa_todos(nome):
        global clients
        for client in clients.keys()
            if nome != client.key()
                clients[client].sendall()






serverPort = 12001
serverSocket = socket(AF_INET, SOCK_STREAM)
# Reusar porta no caso de matar processo.
serverSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
serverSocket.bind(('', serverPort))
serverSocket.listen(1)
print('O servidor esta pronto para receber conexoes')

clients = {}

while 1:
    print('Aguardando conexao...')
    connectionSocket, addr = serverSocket.accept()
    print('Nova conexao recebida!')

    t=Thread()

    # Recepcao de dados
    print('Aguardando dados...')
    # Recebendo nome do arquivo de origem
    origem = connection.recv(1024).decode()

    # Recebendo nome do arquivo de destino
    destino = connection.recv(1024).decode()
    print('Dado recebido do cliente')



    connectionSocket.send()

# Fechamento
print('Fechando socket...')
connectionSocket.close()