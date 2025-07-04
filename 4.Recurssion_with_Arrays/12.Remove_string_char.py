def removechar(stringg , target):
    if len(stringg)==0:
        return stringg  # return empty string
    small = removechar(stringg[1:],target)
    if stringg[0]==target: # if the target is matched then just return the string which we 
        return small       # got from previous function  call 
    else:
        return stringg[0] + small  # if the target is not there just return  the last char + ""
     

print(removechar("Ritikss",'s'))



'''
functions recursively calling to itself(forward)

| Level | Function Call             | `stringg[1:]` | `len() == 0` |
| ----- | ------------------------- | ------------- | ------------ |
| 1     | `removechar("abca", "a")` | `"bca"`       | ❌            |
----------------------------------------------------------------------
| 2     | `removechar("bca", "a")`  | `"ca"`        | ❌            |
----------------------------------------------------------------------
| 3     | `removechar("ca", "a")`   | `"a"`         | ❌            |
----------------------------------------------------------------------
| 4     | `removechar("a", "a")`    | `""`          | ❌            |
----------------------------------------------------------------------
| 5     | `removechar("", "a")`     | -             | ✅            |
----------------------------------------------------------------------



functions returning value to their parent( Backward)


| Level | `stringg` | Value of `small`    | Action Taken                    | Return Value |
        |           | from deeper call    |                                 |
| ----- | --------- | ------------------  | ------------------------------- | ------------ |
| 5     | `""`      | -                   | Base case → return empty string | `""`         |
| ----- | --------- | ------------------  | ------------------------------- | ------------ |
| 4     | `"a"`     | `""`                | `'a' == 'a'` → skip it          | `""`         |
| ----- | --------- | ------------------  | ------------------------------- | ------------ |
| 3     | `"ca"`    | `""`                | `'c' != 'a'` → `'c' + ""`       | `"c"`        |
| ----- | --------- | ------------------  | ------------------------------- | ------------ |
| 2     | `"bca"`   | `"c"`               | `'b' != 'a'` → `'b' + "c"`      | `"bc"`       |
| ----- | --------- | ------------------  | ------------------------------- | ------------ |
| 1     | `"abca"`  | `"bc"`              | `'a' == 'a'` → skip it          | `"bc"`       |
| ----- | --------- | ------------------  | ------------------------------- | ------------ |
'''