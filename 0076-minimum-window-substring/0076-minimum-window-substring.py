class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""
        counter_t = Counter(t)
        i, j = 0, 0
        required = len(counter_t)
        formed = 0
        window_counter = {}
        ans = float('inf'), None, None
        while j < len(s):
            char = s[j]
            window_counter[char] = window_counter.get(char, 0) + 1
            if (char in counter_t and counter_t[char] == window_counter[char]):
                formed += 1
            while i <= j and formed == required:
                char = s[i]
                if j - i + 1 < ans[0]:
                    ans = (j - i + 1, i, j)
                window_counter[char] -= 1
                if char in counter_t and window_counter[char] < counter_t[char]:
                    formed -= 1
                i += 1
            j += 1
        return "" if ans[0] == float('inf') else s[ans[1]: ans[2] + 1]
