from typing import List


def two_sum(nums: List[int], target: int) -> List[int]:
    """
    Two sum

    :param nums: given an array of integers nums
    :param target: an integer target.
    :return: indices of the two numbers such that they add up to target.

    >>> two_sum(nums=[2, 7, 11, 15], target=9)
    [0, 1]
    >>> two_sum(nums=[3, 2, 4], target=6)
    [1, 2]
    >>> two_sum(nums=[3, 3], target=6)
    [0, 1]
    """
    arr = []
    for i, j in enumerate(nums):
        arr.append((i, j))
    arr.sort(key=lambda x: x[1])
    slow, fast = 0, len(arr) - 1
    while slow < len(arr) and fast > 0:
        if arr[slow][1] + arr[fast][1] > target:
            fast -= 1
        elif arr[slow][1] + arr[fast][1] < target:
            slow += 1
        else:
            return [arr[slow][0], arr[fast][0]]

    # slow = 0
    # while slow < len(nums):
    #     fast = slow + 1
    #     while fast < len(nums):
    #         if nums[slow] + nums[fast] != target:
    #             fast += 1
    #         else:
    #             return [slow, fast]
    #     slow += 1


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)
