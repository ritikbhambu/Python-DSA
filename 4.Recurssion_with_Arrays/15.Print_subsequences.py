def printseq(strr,takensofar):
    if len(strr)==0 or strr=='':
        print(takensofar)
        return

    current_char = strr[0]
    small_strr = strr[1:]
    printseq(small_strr,takensofar+current_char) 
    printseq(small_strr,takensofar)  
    return


strr = 'ab'
printseq(strr,'')
