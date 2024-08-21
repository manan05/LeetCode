from typing import List
from collections import defaultdict

class Solution:
    def groupAnagrams(strs: List[str]) -> List[List[str]]:
        ans = defaultdict(list)
        for s in strs:
            # print(s)
            key = "".join(sorted(s))
            # print(key)
            ans[key].append(s)
            # print(ans)
        # print(ans)
        return ans.values()

        

strs: List[str] = ["eat","tea","tan","ate","nat","bat"]
print(Solution.groupAnagrams(strs= strs))