def fatorial(numero):
    if numero <= 1:
        return 1
    else:
        return numero * fatorial(numero - 1)


print(fatorial(0))
