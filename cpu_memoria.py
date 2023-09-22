from multiprocessing import Process
import psutil
import time


def percentual_cpu():
    for proc in psutil.pids():
        p = psutil.Process(pid=proc)
        time.sleep(1)
        porcentagem = p.cpu_percent(interval=1)
        t = p.cpu_times()
        soma = t[0] + t[1]
        if (soma > 0):
            print(p.name(), soma)

def percentualmemoria():
    time.sleep(1)
    porcentagem = psutil.virtual_memory().percent
    t = porcentagem.cpu_times()
    soma = t[0] + t[1]
    print(soma)

if __name__ == '__main__':
    a = 1
    vezes = 60
    p1 = Process(target=percentual_cpu, args=(a, vezes))
    p2 = Process(target=percentualmemoria, args=(a, vezes))
    p1.start()
    p2.start()