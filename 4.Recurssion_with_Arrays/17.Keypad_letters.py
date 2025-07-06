keys = {'1':'', '2':'abc', '3':'def', '4':'ghi', '5':'jkl', '6':'mno',
        '7':'pqrs', '8':'tuv', '9':'wxyz'}

def keypadletter(input):
    if input == '':
        return ['']
    
    ans = []
    current_char = input[0] # it will hold first value everytime
    keysof = keys[current_char] # find all the keypad values of that num
    small = keypadletter(input[1:])

    for i in keysof:  # take first char of the keypad value  
        for j in small: # take first char of previous call
            ans.append(i + j)  # add both and append 
    return ans        

ans = print(keypadletter('23'))



# the aim is to generate all the possible combinations of keypad values
# first we will store our first part of key in current char and then let recursion give us the 
# keypad values of remaining keypads
# then take keypad values of current char and add them with previous one by one