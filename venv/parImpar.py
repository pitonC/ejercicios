

def find(n1):
    if n1%2 == 0:
        return "par"
    return "impar"

n1 = int(input('dame numero: '))
numtype = find(n1)
print('el numero es: ',numtype)
