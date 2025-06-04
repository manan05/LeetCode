class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        def helper(start, s, curr, ans, wordDict):
            if start == len(s):
                ans.append(curr)
                return

            for end in range(start + 1, len(s) + 1):
                mStr = s[start:end]
                if mStr in wordDict:
                    temp = curr
                    if curr:
                        curr = curr + " "
                    curr += mStr
                    helper(end, s, curr, ans, wordDict)
                    curr = temp

        ans = []
        helper(0, s, "", ans, wordDict)
        return ans
