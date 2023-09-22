from multiprocessing import Process
import os

def funcao():
    valor_novo = os.getpid()-valor
    print(os.getpid(), valor_novo)

valor=os.getpid()
valor_novo=os.getpid()-valor

print(os.getpid(), valor_novo)

p1 = Process(target=funcao, args=())
p1.start()

p2=Process(target=funcao,args=())
p2.start()

p3=Process(target=funcao,args=())
p3.start()
