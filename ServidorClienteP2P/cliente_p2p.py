import socket

def download_file(host_ip, file_name):
    # Cria um socket TCP/IP
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Define o endereço do host para conexão
    host_address = (host_ip, 12345)

    try:
        # Conecta ao host
        client_socket.connect(host_address)

        # Envia o nome do arquivo desejado para o host
        client_socket.send(file_name.encode())

        # Recebe o conteúdo do arquivo do host e salva localmente
        with open(file_name, 'wb') as file:
            while True:
                data = client_socket.recv(1024)
                if not data:
                    break
                file.write(data)

        print(f"Download do arquivo '{file_name}' concluído.")
    except ConnectionRefusedError:
        print("Não foi possível conectar ao host.")
    except FileNotFoundError:
        print(f"Arquivo '{file_name}' não encontrado no host.")
    finally:
        # Fecha a conexão com o host
        client_socket.close()

def request_file(file_name):
    # Cria um socket TCP/IP
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Define o endereço do servidor
    server_address = ('127.0.0.1', 12345)

    try:
        # Conecta ao servidor
        client_socket.connect(server_address)

        # Envia o nome do arquivo desejado para o servidor
        client_socket.send(file_name.encode())

        # Recebe o IP do host que possui o arquivo
        host_ip = client_socket.recv(1024).decode()

        if host_ip == "FILE_NOT_FOUND":
            print(f"Arquivo '{file_name}' não foi encontrado em nenhum host.")
        else:
            print(f"O arquivo '{file_name}' está no host com IP: {host_ip}")
            download_file(host_ip, file_name)

    except ConnectionRefusedError:
        print("Não foi possível conectar ao servidor.")

    finally:
        # Fecha a conexão com o servidor
        client_socket.close()

if __name__ == '__main__':
    file_name = input("Digite o nome do arquivo que deseja baixar: ")
    request_file(file_name)
