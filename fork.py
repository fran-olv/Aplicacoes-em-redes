import os
import time
from multiprocessing import Semaphore

s=Semaphore(1)
s1=Semaphore(0)
#16 processos
count=0
pid = os.fork()
pid = os.fork()
pid = os.fork()
pid = os.fork()


if(pid ==0):
    count+=1
    s.acquire()
    print("filho", os.getpid(), count)
    s.release()
    s1.release()
    print(s1)
else:
    count+=1
    s.acquire()
    print("Pai", os.getpid(),"cria filho com PID", pid, count)
    s.release()
    s1.release()
    print(s1)
print(s1)


