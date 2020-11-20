# Iterative approach:
def sum_two_arrays_iterative(array):
    count = 0
    middle = len(array) // 2
    left = array[:middle]
    right = array[middle:]

    while sum(left) != sum(right):
        if sum(array) % 2 or (count == len(array) // 2) or not left or not right:
            print(f"Count is: {count}")
            return False
        elif sum(left) > sum(right):
            count += 1
            middle -= 1
            left = array[:middle]
            right = array[middle:]
        elif sum(left) < sum(right):
            count += 1
            middle += 1
            left = array[:middle]
            right = array[middle:]

    print(f"Count is: {count}")
    print(left, right)
    return True


# Recursive approach:
def sum_two_arrays_recursive(array):
    count = 0
    middle = len(array) // 2

    def sum_two_arrays(middle, array, count):
        left = array[:middle]
        right = array[middle:]

        if sum(array) % 2 or (count == len(array) // 2) or not left or not right:
            print(f"Count is: {count}")
            return False
        elif sum(left) == sum(right):
            print(f"Count is: {count}")
            print(left, right)
            return True
        elif sum(left) > sum(right):
            return sum_two_arrays(middle-1, array, count+1)
        elif sum(left) < sum(right):
            return sum_two_arrays(middle+1, array, count+1)

    if sum_two_arrays(middle, array, count):
        return True

    return False


if __name__ == "__main__":
    pass
    # array = [1, 3, 2, 1, 1, 1, 1, 2]
    # array = [1, 1, 3]

    # print(sum_two_arrays_iterative(array))
    # print(sum_two_arrays_recursive(array))
