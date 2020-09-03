# Implement the selection sort algorithm
arr = [4,7,5,6,-2,0,1,-9,3]

#Steps:

#1. Iterate through the list and find the minimum value
#2. Move the minimum value to the beginning of the list
#3. Ignore the first position (it is sorted)
#4. Repeat steps 1-3 

# Set initial conditions
for i in range(len(arr)):
    min_ind = i
    for j in range(i+1, len(arr)):
        if arr[min_ind] > arr[j]:
            min_ind = j
    temp = arr[i]
    arr[i] = arr[min_ind]
    arr[min_ind] = temp
    print("Iteration",i,":",arr)