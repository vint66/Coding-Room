import random
import time
from typing import Callable

from Task_1_find_sub_array import (Andrew_EqualArraySums, gl_find_sub_array,
                                   snozdrin_find_sub_array)
from Task_2_two_sum import snozdrin_two_sum


def test_find_sub_array(my_func: Callable) -> None:
    """Function to test performance of finding two subarray type of task.

    Args:
        my_func (Callable): Your function which is doing all job.
    """

    result = False

    while not result:
        array = [i for i in range(random.randint(1, 1000))]
        random.shuffle(array)
        start_time = time.perf_counter()

        result = my_func(array)

        duration = time.perf_counter() - start_time

        if not result:
            print(f"Duration of failed execution: {duration}")

    else:
        print(f"Result is: {result}")
        print(f"Duration of execution: {duration}")
        print(f"Original array is: {array}")


def test_two_sum(my_func: Callable) -> None:
    """Function to test performance of finding two sum type of task.

    Args:
        my_func (Callable): Your function which is doing all job.
    """

    result = False

    while not result:
        array = [i for i in range(random.randint(1, 1000))]
        random.shuffle(array)
        target = random.randint(1, 100)
        start_time = time.perf_counter()

        result = my_func(array, target)

        duration = time.perf_counter() - start_time

    else:
        print(f"Result is: {result}")
        print(f"Duration of execution: {duration}")
        print(f"Original array is: {array}")


if __name__ == "__main__":
    test_find_sub_array(snozdrin_find_sub_array.sum_two_arrays_iterative)
    # test_find_sub_array(gl_find_sub_array.check_array)
    # test_find_sub_array(Andrew_EqualArraySums.sortarray)

    # test_two_sum(snozdrin_two_sum.twoSum)
