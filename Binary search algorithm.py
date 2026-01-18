def binarySearch(arr,x):
    low = 0
    high = len(arr)-1
    while low <= high:
        mid = (low + high) // 2
        #check if the middle array is the target value
        if arr[mid] == x:
            return mid
        #if the middle array is less than the target value, ignore right part.

        elif arr[mid] < x:
            low = mid + 1
            #If middle array is greater than the target ignore the left part
        else:
            high = mid - 1
    return -1

if __name__== '__main__':
    arr = [3,4,5,6,7,8,9,10]
    x=4
    result = binarySearch(arr,x)
    if result != -1:
        print("Element is present at index "+str(result))
    else:
        print("Element is not present in the array.")




