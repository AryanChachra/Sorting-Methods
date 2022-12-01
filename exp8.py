def insertion_sort(list1):  
        for i in range(1, len(list1)):  
  
            value = list1[i]  

            j = i - 1  
            while j >= 0 and value < list1[j]:  
                list1[j + 1] = list1[j]  
                j -= 1  
            list1[j + 1] = value   
  
list1 = [10, 5, 13, 8, 2]
n=len(list1)  
print("The unsorted list is")  
for i in range(n):
    print(list1[i],end=" ")
    
insertion_sort(list1) 
print("\n\nThe sorted list1 is")
for i in range(n):
    print(list1[i],end=" ") 