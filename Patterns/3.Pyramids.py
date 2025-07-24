def pyramid_of_stars(n):
    print('pyramid of stars\n')
    for i in range(n+1):
        for j in range(n-i):
            print(' ',end= '')
             
        for k in range(2*i-1):
            print('*',end = '')  
              
        print()    


def butterfly(n):
    print("butterfly pattern: \n")
    # Upper half
    for i in range(1, n + 1):
        # Left stars
        for j in range(i):
            print("*", end="")
        # Spaces
        for j in range(2 * (n - i)):
            print(" ", end="")
        # Right stars
        for j in range(i):
            print("*", end="")
        print()

    # Lower half
    for i in range(n, 0, -1):
        # Left stars
        for j in range(i):
            print("*", end="")
        # Spaces
        for j in range(2 * (n - i)):
            print(" ", end="")
        # Right stars
        for j in range(i):
            print("*", end="")
        print()

def numbers_pyramid(n):
    print("numbers pyramid")
    for i in range(1, n + 1):
        # Print leading spaces
        for k in range(n - i):
            print(' ', end=' ')

        # Decreasing numbers
        temp = i
        while temp > 1:
            print(temp, end=' ')
            temp -= 1

        # Increasing numbers
        for l in range(1, i + 1):
            print(l, end=' ')

        print()


def special_pattern1(N):
    for i in range(1, N + 1):
        temp = i
        # Increasing part
        for j in range(1, i + 1):
            print(temp, end='')
            temp += 1
        
        temp -= 2
        # Decreasing part
        for j in range(1, i):
            print(temp, end='')
            temp -= 1
        
        print()  # Move to next line

def special_pattern2(n):
    for i in range(1, n + 1):
        temp = 2
        # First increasing even numbers
        for j in range(i):
            print(temp, end=' ')
            temp += 2

        temp -=4
        # Then decreasing even numbers
        for j in range(i - 1):
            print(temp, end=' ')
            temp -= 2

        print()  # Move to next line

 




pyramid_of_stars(4)
print('--------------------------------------')
butterfly(4)
print('--------------------------------------')
numbers_pyramid(4)
 
print('--------------------------------------')
special_pattern1(4)
print('--------------------------------------')
 
special_pattern2(4)