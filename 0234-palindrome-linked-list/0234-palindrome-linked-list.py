# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # # Brute Force Solution
        # def checkPalindrome(nums):
        #     left = 0
        #     right = len(nums) - 1
        #     while left < right:
        #         if nums[left] == nums[right]:
        #             left += 1
        #             right -= 1
        #         else:
        #             return False
        #     return True

        # nums = []
        # curr = head
        # while curr:
        #     nums.append(curr.val)
        #     curr = curr.next
        # return checkPalindrome(nums)

        # # Approach 2: Reverse second half of the LL

        # Reverse the second half of LL
        def reverseLL(head):
            prev = None
            curr = head
            while curr:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
            return prev

        # find the first half ending
        def firstHalfEnd(head):
            fast = head
            slow = head
            while fast.next and fast.next.next:
                fast = fast.next.next
                slow = slow.next
            return slow


        if not head:
            return True
        first_half_end = firstHalfEnd(head)
        second_half_start = reverseLL(first_half_end.next)
        result = True
        first = head
        second = second_half_start
        while result and second:
            if first.val != second.val:
                result = False
            first = first.next
            second = second.next

        # Restore the LL back
        first_half_end.next = reverseLL(second_half_start)
        return result
