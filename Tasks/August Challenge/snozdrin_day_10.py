# https://leetcode.com/explore/challenge/card/august-leetcoding-challenge/550/week-2-august-8th-august-14th/3419/

def titleToNumber(s: str) -> int:
    result = 0
    for i, n in enumerate(s[::-1]):
        result += (26 ** i) * (ord(n) - 64)
    return result

s = "AAA"
print(titleToNumber(s))


# a = ord("A") - 64
# a0 = 26 ** 0 * a
# a1 = 26 ** 1 * a
# a2 = 26 ** 2 * a
# a0 + a1 + a2
