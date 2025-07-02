def fact(n):
     
    if n==1:
        return 1
    value = n*fact(n-1)
    return value

print(fact(6))
