class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator == 0:
            return "0"

        res = []

        if numerator < 0 and denominator > 0:
            res.append("-")
        elif numerator > 0 and denominator < 0:
            res.append("-")

        numerator, denominator = abs(numerator), abs(denominator)
        res.append(str(numerator // denominator))
        remainder = numerator % denominator
        if remainder == 0:
            return "".join(res)

        res.append(".")
        hashmap = {}
        while remainder != 0:
            if remainder in hashmap:
                res.insert(hashmap[remainder], "(")
                res.append(")")
                break
            hashmap[remainder] = len(res)
            remainder = remainder * 10
            res.append(str(remainder // denominator))
            remainder = remainder % denominator
        return "".join(res)
