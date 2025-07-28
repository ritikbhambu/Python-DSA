# def maxx(arr):
#     max =0
#     for i in range(len(arr)):
#         if arr[i]>max:
#             max = arr[i]
#     return max         



# arr = [1,5,8,9]
# print(maxx(arr))


# def kth_largest(arr):
     
#     n = len(arr)
#     for i in range(n):
#         for j in range(n-i-1):
#             if arr[j]>arr[j+1]:
#                 arr[j+1],arr[j] = arr[j],arr[j+1]
#     return arr                    



# arr = [1,5,10,8,9]
# res =kth_largest(arr)
# tup = tuple(res)
# print(tup[-2])

# def sorted_or_not(arr):
     
#     n = len(arr)
#     for i in range(1,n):
        
#             if arr[i]<arr[i-1]:
#                   return False
                
#     return True                    



# arr = [1,5,3,8,9]
# res =sorted_or_not(arr)
# print(res)

# def reversearr(arr):
#     n = len(arr)
#     start = 0
#     end = n-1 
#     while(start<=end):
#             arr[start],arr[end] = arr[end],arr[start]
#             start+=1
#             end-=1
#     return arr                    

# arr = [1,5,3,8,9]
# res =reversearr(arr)
# print(res)

# def remove_duplicates(arr):
#     n = len(arr)
#     res =[]
#     for i in range(n):
#         if arr[i] not in res:
#             res.append(arr[i])                     
#     return res
# arr = [1,5,3,8,9,3,5,3]
# res =remove_duplicates(arr)
# print(res)

# def move_zeroes(arr):
#     n = len(arr)
#     for i in range(n):
#         if arr[i]==0:
#             for j in range(i+1,n):
#                 if arr[j]!= 0:
#                     arr[i],arr[j]= arr[j],arr[i]
#     return arr
                
# arr = [1,0,3,8,0,3,5,3]
# res =movezeroes(arr)
# print(res)

 
# def count_frequencies(arr):
#     n = len(arr)
#     count = 1

#     for i in range(1, n):
#         if arr[i] == arr[i - 1]:
#             count += 1
#         else:
#             print(arr[i - 1], "occurs", count, "times")
#             count = 1

#     # Print frequency of the last element
#     print(arr[n - 1], "occurs", count, "times")

# count_frequencies([1,2,2,3,3,3,4,4,4,])

def maxProfit( price):
    n = len(price)
    profit = 0

    for i in range(1,n):
    
        if (price[i] > price[i - 1]):
            profit += price[i] - price[i - 1]
    

    return profit
print(maxProfit([1,2,5,2,3,9]))


