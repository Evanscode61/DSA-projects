


class Solution:
    def reverseArray(self, arr):
        left, right = 0, len(arr)-1
        while left < right:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1
        return arr
sol = Solution()
print(sol.reverseArray([1,2,3,4,5,6,7,8,9]))


