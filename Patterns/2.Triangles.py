def left_angled_triangle(n):
    print("left angled triangle:")
    for i in range(n+1):
        for j in range(i+1):
            print('*',end= '')
        print()    


def right_angled_triangle(n):
    print("right angled triangle: ")
    for i in range(n+1):
        for j in range(n-i):
            print(' ',end= '')
        for k in range(i+1):
            print('*',end = '')    
        print()    

def inverted_triangle(n):
    print("inverted triangle:")
    for i in range(n+1):
        for j in range(n-i):
            print('*',end= '')
        print()    


def number_triangle(n):
    print("number triangle :")
    for i in range(1,n+1):
        for j in range(1,i+1):
            print(j,end= '')
        print()    


def Floyds_triangle(n):
    print("Floyd's Triangle :")
    m=1
    for i in range(1,n+1):
        
        for j in range(1,i+1):
            print(m,end= ' ')
            m+=1        
        print()    




left_angled_triangle(4) 
right_angled_triangle(4)
inverted_triangle(4)
number_triangle(5)
Floyds_triangle(5)