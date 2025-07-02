def digit(num):
    
    if num>=1 and num<=9 :
        return 1
    elif num==0:
        return 0
    small = digit(int(num/10))
    count = 1+small
    return count


print(digit(57834545))
 