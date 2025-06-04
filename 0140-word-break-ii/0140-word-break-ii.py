class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        def helper(start, curr, s, wordDict, ans):
            if start == len(s):
                ans.append(curr)
                return
            for end in range(start + 1, len(s) + 1):
                mStr = s[start:end]
                if mStr in wordDict:
                    temp = curr
                    if curr:
                        curr += " "
                    curr += mStr
                    helper(end, curr, s, wordDict, ans)
                    curr = temp

        ans = []
        helper(0, "", s, wordDict, ans)
        return ans