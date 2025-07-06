 
def permutation(strr,takensofar):
    if len(strr)==0:
        print(takensofar)
        return
    
    current_char = strr[0]
    small = strr[1:]
    for i in range(0,len(takensofar)+1):
        permutation(small,takensofar[0:i]+current_char+takensofar[i:])

    return    

permutation('abc','')
 
 




#                                   abc|''

#                                   bc|a

#                   c|ba                               c|ab

#       ''|cba    ''|bca    ''|bac         ''|cab     ''|acb    ''|abc



# for "|cba ---> current_char= c , takensofar = ba 
# for it we need like    0     +        c      +   ba      and that can be possible like
#              takensofar[0:0] + current_char  + takensofar[0:]
# for "|bca we need      b     +        c      +    a
#              takensofar[0:1] + current_char  + takensofar[1:]
# for "|bac we need      ba    +        c      +    0
#              takensofar[0:2] + current_char  + takensofar[2:]

# hence these can be replaced by i of for loop
#   eg =       takensofar[0:i] + current_char  + takensofar[i:]