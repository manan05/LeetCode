class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        hashMap = {}
        for r in range(n):
            if(nums[r] in hashMap):
                if(abs(r - hashMap[nums[r]] <= k) and r!= hashMap[nums[r]]):
                    return True
            hashMap[nums[r]] = r
        return False