keys = {
    '1': 'a', '2': 'b', '3': 'c', '4': 'd', '5': 'e', '6': 'f',
    '7': 'g', '8': 'h', '9': 'i', '10': 'j', '11': 'k', '12': 'l',
    '13': 'm', '14': 'n', '15': 'o', '16': 'p', '17': 'q', '18': 'r',
    '19': 's', '20': 't', '21': 'u', '22': 'v', '23': 'w',
    '24': 'x', '25': 'y', '26': 'z'
}

def returncodes(input):
    if input == '':
        return ['']
    
    ans = []

    # Single digit case
    if input[0] in keys:
        single = keys[input[0]] # take value of first key 
        small_output = returncodes(input[1:])
        for item in small_output:
            ans.append(single + item)

    # Double digit case (only if input has at least 2 characters)
    if len(input) >= 2 and input[:2] in keys:
        double = keys[input[:2]]
        small_output2 = returncodes(input[2:])
        for item in small_output2:
            ans.append(double + item)

    return ans

# Example
print(returncodes('1123'))
