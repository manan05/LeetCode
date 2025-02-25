class Solution:
    def isPalindrome(self, s: str) -> bool:
        # # iterative, two pointer
        # lower_str = s.lower()
        # cut_str = []
        # for i in lower_str:
        #     if i.isalnum():
        #         cut_str.append(i)
        # l = 0
        # r = len(cut_str) - 1
        # while l < r:
        #     if cut_str[l] != cut_str[r]:
        #         return False
        #     l += 1
        #     r -= 1
        # return True

        # recursion answer

        myStr = [ch for ch in s.lower() if ch.isalnum()]
        n = len(myStr) - 1

        def helper(i, n, myStr):
            if n < i:
                return True

            # self work
            if (myStr[i] != myStr[n]):
                return False

            return helper(i + 1, n - 1, myStr)

        return helper(0, n, myStr)
