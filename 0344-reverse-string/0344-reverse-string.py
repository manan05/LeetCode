class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        # iteratively
        # i = 0
        # j = len(s) - 1
        # while (i < j):
        #     s[i], s[j] = s[j], s[i]
        #     i += 1
        #     j -= 1
        
        # recursively
        def helper(i, j, s):
            if (i >= j):
                return
            s[i], s[j] = s[j], s[i]
            helper(i + 1, j - 1, s)

        i = 0
        j = len(s) - 1
        helper(i , j , s)
        