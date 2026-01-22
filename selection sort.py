# function to perform selection sort.
def selection_sort(arr):
    n = len(arr)
    temp = arr[0]
    for i in range(len(arr)-1):
        if arr[i] > arr[0]:
            temp = arr[i]
            for j in range (i+1, len(arr)):
                if arr[j] < arr[i]:
                    arr[i], arr[j] = arr[j], arr[i]
arr =[5,2,35,3,4,67,9]
size = len(arr)
selection_sort(arr)
print(arr)