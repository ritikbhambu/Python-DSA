def nto_one(n):
    if n<=0:
        return 0
    print(n)
    nto_one(n-1)

 
nto_one(5)
    