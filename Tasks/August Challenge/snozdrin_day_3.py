# https://leetcode.com/explore/challenge/card/august-leetcoding-challenge/549/week-1-august-1st-august-7th/3411/

class Solution:
    def isPalindrome(self, s: str) -> bool:
        import re
        new_s = re.sub(r"[^a-zA-Z0-9]+", "", s.lower())
        return new_s == new_s[::-1]


# s = "A man, a plan, a canal: Panama".lower()

# a = 0
# b = -1

# while a < len(s):
#     if not s[a].isalnum():
#         a += 1
#     if not s[b].isalnum():
#         b -= 1
# else:
#     print("True")

# a = 0
# while a < len(s)-1 and not s[a].isalnum():
#     a += 1
# else:
#     print(a)
#     print("False")

# b = -1
# while abs(b) < len(s) and not s[b].isalnum():
#     b -= 1
# else:
#     print(b)
#     print("False2")



# s = "A man, a plan, a canal: Panama".lower()

# def my_func(string):
#     a = 0
#     b = -1

#     while True:

#         while a < len(s)-1 and not s[a].isalnum():
#             a += 1

#         while abs(b) < len(s) and not s[b].isalnum():
#             b -= 1

#         if s[a] != s[b] or not s[a].isalnum() or not s[b].isalnum():
#             return False

# # Working solution so far
# # s = "A man, a plan, a canal: Panama"
# s = "ab_a"
# import re
# new_s = re.sub(r"[^a-zA-Z0-9]+", "", s.lower())
# # return new_s == new_s[::-1]
# print(new_s)
# print(new_s == new_s[::-1])