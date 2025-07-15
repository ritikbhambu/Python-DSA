def sumall(n):
    if n>=0 and n<10:
        return n
    val = n%10
    return val+sumall(int(n/10))
print(sumall(451))


def revsumall(n):
    if n>=0 and n<10:
        return n
    small = revsumall(int(n/10))
    return small + n%10 

print(revsumall(451))



    

 