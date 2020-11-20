# https://leetcode.com/explore/challenge/card/august-leetcoding-challenge/549/week-1-august-1st-august-7th/3414/

def findDuplicates(nums):
    dups = set()
    nums.sort()
    for i in range(len(nums)-1):
        if nums[i] == nums[i+1]:
            dups.add(nums[i+1])

    return dups


# lst = [4,3,2,7,8,2,3,1]
# print(findDuplicates(lst))
