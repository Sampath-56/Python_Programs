def bubble_Sort(array):  
    n = len(array)  
    for i in range(n-1):  
        for j in range(0, n-i-1):  
            if array[j] > array[j + 1]:  
                array[j], array[j + 1] = array[j + 1], array[j]  
    print(array)  
  
# Example array  
arr = [23, 14, 64, 13, 64, 23, 86]  
  
bubble_Sort(arr)

#output: [13, 14, 23, 23, 64, 64, 86]