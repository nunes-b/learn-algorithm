def regressiva(n):
    if n < 1:
        print("fim")
    else:
        regressiva(n - 1)
        print(n)


print(regressiva(10))
