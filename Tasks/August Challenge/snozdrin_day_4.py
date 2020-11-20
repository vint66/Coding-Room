# https://leetcode.com/explore/challenge/card/august-leetcoding-challenge/549/week-1-august-1st-august-7th/3412/

class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        import math

        if num <= 0:
            return False

        power = math.log(num, 4)
        if power % 1 != 0:
            return False

        return 4 ** power == num
