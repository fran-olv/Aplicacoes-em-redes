import os

valor = os.getpid()

p1 = os.fork()
if p1 == 0:
    valor_novo = os.getpid() - valor
    print(os.getpid(), valor_novo)
else:
    p2 = os.fork()
    if p2 == 0:
        valor_novo = os.getpid() - valor
        print(os.getpid(), valor_novo)
    else:
        p3 = os.fork()
        if p3 == 0:
            valor_novo = os.getpid() - valor
            print(os.getpid(), valor_novo)
        else:
            valor_novo = os.getpid() - valor
            print(os.getpid(), valor_novo)
