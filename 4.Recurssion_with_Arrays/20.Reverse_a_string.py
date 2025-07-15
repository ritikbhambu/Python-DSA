def revstring(strr):
    if len(strr)==1:
        return strr
    last = strr[-1]
    small = revstring(strr[:-1])
    return  last + small

print(revstring('abcd'))


 