def palindrome(str,start,end):
    if start>=end:  #  = means we reached to the middle element of string
        return True # > means if the string is off even length
    if str[start] != str[end]:  # if starting and ending characters are not same 
        return False
    return palindrome(str,start+1,end-1) # everytime increment start pointer and decrement end pointer

str = "nitin"
print(palindrome(str,0,len(str)-1))



# without indexing
def pali(strr):
    if len(strr)==0 or len(strr)==1:
        return True
    first = strr[0]
    last = strr[-1]
    if first != last:
        return False
    return pali(strr[1:-1])
   
     
print(pali('cabacc'))