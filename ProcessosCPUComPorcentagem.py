from multiprocessing import Process
import psutil
import sys
import time

n=sys.argv[1]
n=float(n)

def percentual():
    for proc in psutil.pids():
        p = psutil.Process(pid=proc)
        time.sleep(1)
        porcentagem=p.cpu_percent(interval=1)
        t=p.cpu_times()
        soma=t[0]+t[1]
        if (soma>n):
            print(p.name(), soma)

def percentualmemoria():
        time.sleep(1)
        porcentagem=psutil.virtual_memory().percent
        t=porcentagem.cpu_times()
        soma=t[0]+t[1]
        print(soma)


a=1
vezes=60
p1= Process(target=percentual,args=(a,vezes))
p2=Process(target=percentualmemoria,args=(a,vezes))
p1.start()
p2.start()