class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        lastOcc = -1
        for i in range(len(nums)):
            if lastOcc == -1 and nums[i] == 1:
                lastOcc = i
                continue
            if nums[i] == 1:
                if i - lastOcc - 1 < k:
                    return False
                else:
                    lastOcc = i
        return True
