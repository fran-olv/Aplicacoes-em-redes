from socket import *
from random import randint
import pickle
import sys

# cria arquivo
arquivo = open("arquivo.txt", "wb")
a = bytes(248)
arquivo.write(a)

serverPort = 12001

serverSocket = socket(AF_INET, SOCK_STREAM)

# Reusar porta no caso de matar processo.
serverSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)

serverSocket.bind(('', serverPort))
serverSocket.listen(1)
print('O servidor esta pronto para receber conexoes')

while 1:
    print('Aguardando conexao...')
    connectionSocket, addr = serverSocket.accept()
    print('Nova conexao recebida!')

    # Recepcao de dados
    print('Aguardando dados...')
    # Recebendo nome do arquivo de origem
    origem = connection.recv(1024).decode()

    # Recebendo nome do arquivo de destino
    destino = connection.recv(1024).decode()
    print('Dado recebido do cliente')

    # Abrindo arquivo de origem em modo binário
    with open(origem, 'rb') as f_origem:
        # Criando arquivo de destino em modo binário
        with open(destino, 'wb') as f_destino:
            # Lendo e escrevendo 1024 bytes por vez até o fim do arquivo
            while True:
                data = f_origem.read(1024)
                if not data:
                    break
                f_destino.write(data)

    connectionSocket.send()

# Fechamento
print('Fechando socket...')
connectionSocket.close()