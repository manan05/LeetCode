def merge(nums, left, mid, right):
    count = 0
    s1 = left
    s2 = mid + 1
    n1 = mid + 1 - left
    n2 = right - mid
    j = s2

    # count reverse pairs
    for i in range(left, mid + 1):
        while j <= right and nums[i] > 2 * nums[j]:
            j += 1
        count += j - (mid + 1)

    # Merge
    temp = []
    i, j = s1, s2
    while i <= mid and j <= right:
        if nums[i] <= nums[j]:
            temp.append(nums[i])
            i += 1

        else:
            temp.append(nums[j])
            j += 1

    while i <= mid:
        temp.append(nums[i])
        i += 1

    while j <= right:
        temp.append(nums[j])
        j += 1

    # copy temp back to nums
    for i in range(len(temp)):
        nums[s1 + i] = temp[i]

    return count


def mergeSort(nums, left, right):
    if left >= right:
        return 0
    mid = (left + right) // 2
    count = mergeSort(nums, left, mid)
    count += mergeSort(nums, mid + 1, right)
    count += merge(nums, left, mid, right)
    return count
class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        return mergeSort(nums, 0, len(nums) - 1)
