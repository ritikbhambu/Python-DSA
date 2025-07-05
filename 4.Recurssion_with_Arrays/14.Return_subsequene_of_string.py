

# let string = "abc"
# substring = it should be contionuous and order should be maintained
# eg = a , b , c , ab , bc , abc   ----> n(n+1)/2
# subsequence = onlu order should be maintained
# eg = a , b , c , ab , bc , ac , abc , " "   -----> 2^n






def returnsubseq(strr):
    if strr== '': # as empty string is also part of the subsequence
        ans = ['']
        return ans 
    small = returnsubseq(strr[1:])

    mchar = strr[0]
    ans = []

    ans.extend(small)
                        # if we add [4,5,6] into a string append will give [ 2,3,[4,5,6]]
    for i in small:      # but we need [2,3,4,5,6] thats why we will use extend
        ans.append(mchar+i)
        
    return ans   


print(returnsubseq("abc"))


# go till "" and return ""
# for its above function small will consist "" ( every child fuction returned value will be stored in parent's small ariable)
# in the same function :
  # take first char of string in mychar
  # first create empty list
  # extend the small's value in the list 
  # loop on small:
        # for every iteration --> add mychar before every value and append them in the list
  # return the ans to its parent function
  # that ans will be stored in small      






