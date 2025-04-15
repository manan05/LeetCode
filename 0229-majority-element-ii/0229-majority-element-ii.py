class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        # # Approach 1: hashmap
        # res = []
        # myDict = {}
        # for i in nums:
        #     myDict[i] = myDict.get(i, 0) + 1

        # threshold = len(nums) // 3
        # for i in myDict.items():
        #     if i[1] > threshold:
        #         res.append(i[0])
        # return res

        # # Boyer - Moore Algorithm
        c1, c2 = 0, 0
        candidate1, candidate2 = None, None

        for i in nums:
            if candidate1 == i:
                c1 += 1
            elif candidate2 == i:
                c2 += 1
            elif c1 == 0:
                candidate1 = i
                c1 += 1
            elif c2 == 0:
                candidate2 = i
                c2 += 1
            else:
                c1 -= 1
                c2 -= 1
        res = []
        threshold = len(nums) // 3
        c1, c2 = 0, 0
        for i in nums:
            if i == candidate1:
                c1 += 1
            elif i == candidate2:
                c2 += 1
        if c1 > threshold:
            res.append(candidate1)
        if c2 > threshold:
            res.append(candidate2)

        return res
