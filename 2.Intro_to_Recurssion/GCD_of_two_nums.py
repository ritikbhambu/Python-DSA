def gcd(num1,num2):
    if num2<=0:
        return
    if num1%num2 ==0:
        return num2
    return gcd(num1,int(num2/2))
print(gcd(60,36) )  




