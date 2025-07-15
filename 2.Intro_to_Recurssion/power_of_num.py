def power(n,m):
    if n==0:
        return 0
    if m==1:
        return n
    small = power(n,m-1)
    res = n*small
    return res

print(power(2,4))