import math
from typing import List


class DoublePoint:
    """
    Double pointer is used to iterate array,
    and the two pointers point to different elements
    to complete task cooperatively.
    """

    def two_sum(self, numbers: List[int], target: int) -> List[int]:
        """
        Two sum - input array is sorted
        :param numbers: one 1-indexed array of integers that is sorted in non-decreasing order.
        :param target: find 2 numbers such that they add up to a specific target number.
        :return: an array made by the indices of two numbers
        >>> DoublePoint().two_sum(numbers=[2, 7, 11, 15], target=9)
        [1, 2]
        """
        slow, fast = 0, len(numbers) - 1
        while slow < fast:
            sum = numbers[slow] + numbers[fast]
            if sum < target:
                slow += 1
            elif sum > target:
                fast -= 1
            else:
                return [slow + 1, fast + 1]


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)
