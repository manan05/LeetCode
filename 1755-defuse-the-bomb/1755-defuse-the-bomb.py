class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n = len(code)
        result = [0] * n
        if (k == 0):
            return result
        elif (k > 0):
            for i in range(n):
                for j in range(i + 1, i + k + 1):
                    result[i] = result[i] + code[j % n]
        else:
            for i in range(n):
                for j in range(i - abs(k), i):
                    result[i] = result[i] + code[(j + n) % n]

        return result