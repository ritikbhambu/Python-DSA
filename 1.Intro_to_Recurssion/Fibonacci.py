def fibonacci(num):
    if num==0:
        return 1
    if num==1:
        return 1
    last = fibonacci(num-1)
    secondlast = fibonacci(num-2)
    series = last + secondlast
    return series

print(fibonacci(7))
