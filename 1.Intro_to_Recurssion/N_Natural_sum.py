def sum(n):
    if n==1:
        return 1
    small = sum(n-1)
    value = n + small
    return value


print(sum(5))
