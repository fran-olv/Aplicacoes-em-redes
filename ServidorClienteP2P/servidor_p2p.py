import socket

HOST = '127.0.0.1'  # Endereço IP do servidor
PORT = 12345  # Porta de escuta do servidor

# Lista de hosts cadastrados no servidor
hosts_cadastrados = {
    'file1': '192.168.0.101',
    'file2': '192.168.0.102',
    'file3': '192.168.0.103',
}

def handle_client(client_socket):
    # Recebe a requisição de arquivo do cliente
    arquivo = client_socket.recv(1024).decode()

    # Procura o host que possui o arquivo
    if arquivo in hosts_cadastrados:
        host_ip = hosts_cadastrados[arquivo]
        response = host_ip
    else:
        response = "FILE_NOT_FOUND"

    # Envia a resposta para o cliente
    client_socket.send(response.encode())

    # Fecha a conexão com o cliente
    client_socket.close()

def start_server():
    # Cria um socket TCP/IP
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Vincula o socket à porta e ao endereço
    server_socket.bind((HOST, PORT))

    # Coloca o socket em modo de escuta
    server_socket.listen()

    print(f"Servidor ouvindo em {HOST}:{PORT}")

    while True:
        # Aguarda por conexões dos clientes
        client_socket, address = server_socket.accept()

        print(f"Conexão estabelecida com {address[0]}:{address[1]}")

        # Lida com o cliente em uma nova thread
        handle_client(client_socket)

if __name__ == '__main__':
    start_server()
