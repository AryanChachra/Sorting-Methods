def selection_sort(array):  
    length = len(array)  
      
    for i in range(length-1):  
        minIndex = i  
          
        for j in range(i+1, length):  
            if array[j]<array[minIndex]:  
                minIndex = j  
                  
        array[i], array[minIndex] = array[minIndex], array[i]  
               
array = [21,6,9,33,3]
n=len(array)
print('Given array is')
for i in range(n):
    print(array[i],end=" ")
selection_sort(array) 
print("\n\nThe sorted array is")
for i in range(n):
    print(array[i],end=" ") 