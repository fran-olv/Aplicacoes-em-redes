import threading

mem_compartilhada = ""
leitores = 0
mutex = threading.Semaphore(1)
sem_escrita = threading.Semaphore(1)
sem_leitura = threading.Semaphore(1)

def leitor():
    global mem_compartilhada, leitores
    mutex.acquire()
    leitores += 1
    if leitores == 1:
        sem_escrita.acquire()
    mutex.release()

    print(f"Conteúdo da memória compartilhada: {mem_compartilhada}")

    mutex.acquire()
    leitores -= 1
    if leitores == 0:
        sem_escrita.release()
    mutex.release()

def iniciar_leitores(num_leitores):
    threads = []
    for _ in range(num_leitores):
        thread = threading.Thread(target=leitor)
        thread.start()
        threads.append(thread)
    return threads

if __name__ == "__main__":
    num_leitores = int(input("Digite o número de leitores: "))

    threads_leitores = iniciar_leitores(num_leitores)

    for thread in threads_leitores:
        thread.join()
Crie 2 arquivos um de leitor e outro de escritor onde caso o usuario queira ler, o processo imprime o que esta na area de memoria caso queira escrever, o processo apaga o que esta na area de memoria e coloca a nova informacao