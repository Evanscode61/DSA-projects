class Solution:
    def search(self, arr, x):
        for i in range(len(arr)):
            if arr[i] == x:
                return i
        return -1
print(Solution().search([1,3,5,6,7,8,9], 5))
