
# Finding sum of two values in a list using two pointer technique.

def twoSum(arr, target):
    left, right = 0, len(arr)-1
    while left < right:
        sum = arr[left] + arr[right]
        if sum == target:
            return True
        elif sum < target:
            left += 1
        else:
            right -= 1
    return False
arr = [2,4,5,6,9,10]
target = 9
# The otput should give a bool= True
print(twoSum(arr, target))




