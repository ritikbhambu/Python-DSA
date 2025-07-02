def oneton(n):
    if n<=0:
        return 0
    oneton(n-1)
    print(n)


oneton(50)        