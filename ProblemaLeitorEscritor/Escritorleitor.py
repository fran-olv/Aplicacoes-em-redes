import threading

# Área de memória compartilhada
shared_memory = ""
readers = 0
mutex = threading.Semaphore(1)
write_sem = threading.Semaphore(1)
read_sem = threading.Semaphore(1)

def reader():
    global shared_memory, readers
    mutex.acquire()
    readers += 1
    if readers == 1:
        write_sem.acquire()
    mutex.release()

    # Lendo da área de memória compartilhada
    print(f"Conteúdo da memória compartilhada: {shared_memory}")

    mutex.acquire()
    readers -= 1
    if readers == 0:
        write_sem.release()
    mutex.release()

def writer():
    global shared_memory
    write_sem.acquire()

    # Escrevendo na área de memória compartilhada
    data = input("Digite a nova informação: ")
    shared_memory = data

    write_sem.release()

def main():
    while True:
        choice = input("Deseja ler (L) ou escrever (E)? ")

        if choice.upper() == "L":
            read_sem.acquire()
            reader()
            read_sem.release()
        elif choice.upper() == "E":
            writer()
        else:
            print("Escolha inválida. Tente novamente.")

if __name__ == "__main__":
    main()
