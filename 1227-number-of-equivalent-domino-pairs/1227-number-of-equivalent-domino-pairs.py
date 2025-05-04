class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        # Brute Force Approach:
        # count = 0
        # for i in range(len(dominoes) - 1):
        #     for j in range(i + 1, len(dominoes)):
        #         first = dominoes[i]
        #         second = dominoes[j]
        #         if (first[0] == second[0] and first[1] == second[1]):
        #             count += 1
        #         elif (first[0] == second[1] and first[1] == second[0]):
        #             count += 1
        # return count

        # # Optimized
        hashmap = {}
        count = 0
        for a, b in dominoes:
            key = tuple(sorted((a, b)))
            count += hashmap.get(key, 0)
            hashmap[key] = hashmap.get(key, 0) + 1
        return count
