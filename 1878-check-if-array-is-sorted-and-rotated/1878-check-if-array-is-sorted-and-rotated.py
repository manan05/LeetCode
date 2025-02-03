class Solution:
    def check(self, nums: List[int]) -> bool:
        n = len(nums)

        sorted_arr = sorted(nums)

        for i in range(n):
            isMatch = True
            for j in range(n):
                if(nums[(i + j)%n] != sorted_arr[j]):
                    isMatch = False
                    break
            if isMatch == True:
                return True
        return False