"""
Given an array of integers, return indices of the two numbers such that they add up to a specific target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.

Given nums = [2, 7, 11, 15], target = 9,
Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
"""


array = [1, 3, 2, 13, 15, 7]
array2 = [2, 7, 11, 15]
target = 9



def find_target(arg):
	for i in range(len(arg)):
		check = target - arg[i]
		if arg[i] > 9:
			i+=1
		elif check in arg:
			my_return = []
			my_return.append(i)
			my_return.append(arg.index(check))
			print(my_return)
			break
			
find_target(array2)

