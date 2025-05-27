class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)
        res = []

        def helper(index, curr):
            if index == n:
                res.append(curr[:])
                return

            for i in range(index + 1, n + 1):
                substr = s[index:i]
                if self.isPalindrome(substr):
                    curr.append(substr)
                    helper(i, curr)
                    curr.pop()

        helper(0, [])
        return res

    def isPalindrome(self, mstr):
        return mstr == mstr[::-1]
