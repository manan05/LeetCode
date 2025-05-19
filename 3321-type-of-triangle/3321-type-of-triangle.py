class Solution:
    def triangleType(self, nums: List[int]) -> str:
        a, b, c = nums[0], nums[1], nums[2]
        if a + b > c and b + c > a and a + c > b:
            mset = set(nums)
            length = len(mset)
            if length == 1:
                return "equilateral"
            elif length == 2:
                return "isosceles"
            else:
                return "scalene"
        else:
            return "none"