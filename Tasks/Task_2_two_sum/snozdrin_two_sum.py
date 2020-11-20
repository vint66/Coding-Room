# def twoSum(nums, target):
#     for i, j in enumerate(nums):
#         for n, m in enumerate(nums):
#             second = target - j
#             if second == m and i != n:
#                 return [i, n]


def twoSum(nums, target):
    count = 0
    for idx, num in enumerate(nums):
        second = target - num
        count += 1
        try:
            second_idx = nums[idx+1:].index(second)
            count += 1
            print(f"Count is: {count}")
            return [idx, second_idx+idx+1]
        except:
            count += 1
            pass


            # for i in nums[num+1:]:
            #     if i == second:
            #         first_idx = nums.index(num)
            #         second_idx = nums[num+1:].index(i)
            #         return [first_idx, second_idx]


if __name__ == "__main__":
    pass
    # nums = [2, 7, 11, 15]
    # target = 9
    # print(twoSum(nums, target))

    # nums = [2, 7, 11, 15]
    # nums = [1, 2, 3, 4, 5]
    # target = 7
    # print(twoSum(nums, target))
