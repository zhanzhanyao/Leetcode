# In many problems dealing with an array (or a LinkedList), we are asked to find or calculate something
# among all the contiguous subarrays (or sublists) of a given size.
from sys import maxsize
from typing import List


def min_subarray_len(target: int, nums: List[int]) -> int:
    """
    Minimum size subarray sum

    :param target: an array of positive integers
    :param nums: a positive integer
    :return: the minimal length of a contogious subarray, of which the sum is greater than or equal target.if no such array,rerurn 0

    >>> min_subarray_len(target=7, nums=[2,3,1,2,4,3])
    2
    >>> min_subarray_len(target=4, nums=[1,4,4])
    1
    >>> min_subarray_len(target=11, nums=[1,1,1,1,1,1,1,1])
    0
    >>> min_subarray_len(target=213, nums=[12,28,83,4,25,26,25,2,25,25,25,12])
    8
    """
    left, total = 0, 0
    res = maxsize
    for i in range(len(nums)):
        total += nums[i]
        while total >= target:
            res = min(res, i - left + 1)
            total -= nums[left]
            left += 1
    return res if res != maxsize else 0


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)
