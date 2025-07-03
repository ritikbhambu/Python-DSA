def digit(num):
    
    if num>=1 and num<=9 :
        return 1
    elif num==0:
        return 0
    count =1 +digit(int(num/10)) # counting the no of times loop ran
    
    return count


print(digit(57834545))
 