class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {
            "I": 1,
            "IV": 4,
            "V": 5,
            "IX": 9,
            "X": 10,
            "XL": 40,
            "L": 50,
            "XC": 90,
            "C": 100,
            "CD": 400,
            "D": 500,
            "CM": 900,
            "M": 1000
        }
        result = 0
        next = 0
        for i, n in enumerate(s):
            if next:
                next = 0
                continue
            elif (i < len(s) - 1) and ((n == "I" and s[i+1] in "VX") or (n == "X" and s[i+1] in "LC") or (n == "C" and s[i+1] in "DM")):
                result += roman[f"{n}{s[i+1]}"]
                next = 1
            else:
                result += roman[f"{n}"]

        return result


class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        result = 0
        for i, n in enumerate(s):
            a = roman[n]
            if i < len(s) - 1:
                if a >= roman[s[i+1]]:
                    result += a
                else:
                    result -= a
            else:
                result += a

        return result


if __name__ == "__main__":
    pass
