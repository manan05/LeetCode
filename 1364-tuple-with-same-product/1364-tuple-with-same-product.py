class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        # O(n3)
        # length = len(nums)
        # nums.sort()

        # count_total = 0
        # for a in range(length):
        #     for b in range(length - 1, a, -1):
        #         product = nums[a] * nums[b]
        #         possible_d = set()

        #         # c would be between a and b
        #         for c in range(a + 1, b):
        #             if product % nums[c] == 0:
        #                 d = product // nums[c]

        #                 # adding 8 so that all possible permutations of the 4 elements are considered
        #                 if d in possible_d:
        #                     count_total += 8
        #                 # adding c here
        #                 possible_d.add(nums[c])
        # return count_total


        # # Approach 2: using prod_arr and sorting it
        # n = len(nums)
        # prod_arr = []
        # total_count = 0

        # for i in range(n):
        #     for j in range(i + 1, n):
        #         prod_arr.append(nums[i] * nums[j])

        # prod_arr.sort()

        # last_prod = -1
        # same_prod = 0

        # for p in range(len(prod_arr)):
        #     if prod_arr[p] == last_prod:
        #         same_prod += 1
        #     else:
        #         pairs_of_equal = ((same_prod - 1) * same_prod // 2)

        #         total_count += 8 * (pairs_of_equal)
        #         last_prod = prod_arr[p]
        #         same_prod = 1
        
        # pairs_of_equal = ((same_prod - 1) * same_prod // 2)
        # total_count += 8*pairs_of_equal
        # return total_count

        # Approach 3: using hashmap to store product counts

        n = len(nums)
        total_count = 0
        prod_dict = {}

        for i in range(n):
            for j in range(i + 1, n):
                prod = nums[i] * nums[j]
                if prod in prod_dict:
                    prod_dict[prod] += 1
                else:
                    prod_dict[prod] = 1
        
        for i in prod_dict.keys():
            if prod_dict[i] > 1:
                pairs_of_equal = ((prod_dict[i] - 1) * prod_dict[i] // 2)
                total_count += 8 * (pairs_of_equal)
        return total_count