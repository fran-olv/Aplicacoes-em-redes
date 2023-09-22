import threading

mem_compartilhada = ""
mutex = threading.Semaphore(1)
sem_escrita = threading.Semaphore(1)

def escritor():
    global mem_compartilhada
    sem_escrita.acquire()

    data = input("Digite a nova informação: ")
    mem_compartilhada = data

    sem_escrita.release()

if __name__ == "__main__":
    escritor()
