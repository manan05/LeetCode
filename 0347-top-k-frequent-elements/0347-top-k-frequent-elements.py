import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # # Using Heapq
        # res = []
        # counter = Counter(nums)
        # min_heap = []
        # for elem, count in counter.items():
        #     heapq.heappush(min_heap, (count, elem))
        #     if len(min_heap) > k:
        #         heapq.heappop(min_heap)
        # for c, elem in min_heap:
        #     res.append(elem)
        # return res


        # # Using QuickSelect
        counter = Counter(nums)
        unique = list(counter.keys())

        def partition(left, right):
            pivot_idx = right
            pivot_freq = counter[unique[pivot_idx]]

            j = left
            for i in range(left, right):
                if counter[unique[i]] < pivot_freq:
                    unique[i], unique[j] = unique[j], unique[i]
                    j += 1
            unique[j], unique[pivot_idx] = unique[pivot_idx], unique[j]
            return j

        def quickselect(left, right, target_idx):
            while left <= right:
                pivot_final_idx = partition(left, right)

                if pivot_final_idx == target_idx:
                    return
                elif pivot_final_idx < target_idx:
                    left = pivot_final_idx + 1
                else:
                    right = pivot_final_idx - 1

        n = len(unique)
        target = n - k
        quickselect(0, n - 1, target)
        return unique[target:]
