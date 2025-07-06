def toh(n,source,destination,auxiliary):
    if n==0:
        return
    if n==1:
        print(source+ "---->" + destination)
        return
    toh(n-1,source,auxiliary,destination)
    print(source + "---->" + destination)
    toh(n-1,auxiliary,destination,source)    

toh(3,'a','b','c')