"""
Given a data stream input of non-negative integers a1, a2, ..., an, ..., summarize the numbers seen so far as a list of disjoint intervals.

For example, suppose the integers from the data stream are 1, 3, 7, 2, 6, ..., then the summary will be:

1: [1, 1]
3: [1, 1], [3, 3]
7: [1, 1], [3, 3], [7, 7]
2: [1, 3], [7, 7]
6: [1, 3], [6, 7]
4: [1, 4], [6, 7]
10: [1, 4], [6, 7], [10, 10]
"""


def group_nums(nums):
    groups = [[nums[0]]]
    for i in range(1, len(nums)):
        for j in groups:
            if nums[i] - min(j) in {-1, 1} or nums[i] - max(j) in {-1, 1}:
                j.append(nums[i])
                break
        else:
            groups.append([nums[i]])
    return groups


# def group_nums(nums):
#     groups = [[nums[0]]]
#     converged = False
#     while not converged:
#         for j in groups:
#             for i in range(1, len(nums)):
#                 if nums[i] - min(j) in {-1, 1} or nums[i] - max(j) in {-1, 1}:
#                     j.append(nums[i])
#                     break
#                 else:
#                     groups.append([nums[i]])
#     return groups


def normalize(groups):
    for i in range(1, len(groups)):
        if min(groups[i]) - max(groups[i-1]) in {-1, 1} or max(groups[i]) - min(groups[i-1]) in {-1, 1}:
            tmp = groups.pop(i)
            groups[i-1] = groups[i-1] + tmp
    return groups


def calculate_summary(groups):
    for i in range(len(groups)):
        m0 = min(groups[i])
        m1 = max(groups[i])
        groups[i] = [m0, m1]
    return groups


nums = [1, 3, 7, 2, 6]
# nums = [8, 9, 10, 7, 8, 1, 2, 3]
# print(group_nums(nums))
print(normalize(group_nums(nums)))
# print(calculate_summary(group_nums(nums)))


def merge_intervals(array):
    array.sort()
    merged = [[array[0], array[0]]]
    for i in range(1, len(array)):
        if array[i] - merged[-1][1] == 1:
            merged[-1] = [merged[-1][0], max(merged[-1][1], array[i])]
        else:
            merged.append([array[i], array[i]])
    return merged
