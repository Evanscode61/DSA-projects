# Finding two sum using hash set approach, O(1) time complexity
def twoSum(arr, target):
    s = set()
    for i in range(len(arr)):
        complement = target - arr[i]
        if complement in s:
            return True
        s.add(arr[i])
    return False
arr = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
target = 21
print(twoSum(arr, target))


