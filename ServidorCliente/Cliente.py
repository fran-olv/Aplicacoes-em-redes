from socket import *
import os
import pickle

serverName = 'localhost'
serverPort = 12000

try:
    # Criacao do socket
    clientSocket = socket(AF_INET, SOCK_STREAM)
    # Conexao com o servidor
    clientSocket.connect((serverName,serverPort))
except:
    print("Erro ao conectar!")
    quit()

dados_byte = arquivo.read(2000)
arquivo.write(dados_byte)


if len(sys.argv) < 4:
    print('Modo de uso:')
    print(sys.argv[0], '<host> \
    <arquivo remoto> <arquivo local>')
    quit()

serverName = sys.argv[1]
filename = sys.argv[2]
filename2 = sys.argv[3]

# Fechamento
clientSocket.close()