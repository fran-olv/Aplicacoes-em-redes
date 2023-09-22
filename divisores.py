import sys;

print(sys.argv)

def divisores(n):
    for i in range(1, n + 1):
        if (n % i) == 0:
            print(i)


if __name__ == '__main__':
    divisores(int(sys.argv[1]))
