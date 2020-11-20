##Split arrays to two subarrays with equal sum of elements or return False.

array = [1, 3, 2, 1, 1, 1, 1, 2]
array1 = [1, 1, 3]
array2 = [100, 25, 25, 25, 25]


def find_equal(arg):
	half_point = sum(arg) // 2
	x = 0
	for i in range(len(arg)):
		if x != half_point:
			x = arg[i] + x
			#print(i)
		else:
			return i 


def check_array(arg):
	if sum(arg) % 2 != 0:
		return False
	else:
		i = find_equal(arg)
		sub_array1 = arg[0:i]
		sub_array2 = arg[i:]
		print(sub_array1)
		print(sub_array2)


check_array(array)