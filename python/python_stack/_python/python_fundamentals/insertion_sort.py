#Insertion Sort
    # Start at index 1
    # Shift the value to the left if smaller
    # Repeat until sorted

arr = [6,5,3,1,8,7,2,4]

for i in range(len(arr)):
    for j in range(i):
        if arr[i] < arr[j]:
            arr[i],arr[j] = arr[j],arr[i]
print(arr)
