from typing import List


# Two Pointers is working on sorted arrays or LinkedLists and finding a set of elements that fulfill certain constraints
# The set of elements could be a pair, a triplet or even a subarray


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


def remove_duplicates(nums: List[int]) -> int:
    """
    Remove duplicates from sorted array

    :param nums: an integer array sorted by non-decreasing order
    :return: the length of unique elements

    >>> remove_duplicates(nums=[1, 1, 2, 2])
    2
    >>> remove_duplicates(nums=[0, 0, 1, 1, 1, 2, 2, 3, 3, 4])
    5
    """
    slow = len(nums) - 1
    fast = slow - 1
    while slow >= 0 and fast >= 0:
        if nums[slow] == nums[fast]:
            nums.pop(slow)
            fast -= 1
        slow -= 1
        fast = slow - 1
    return len(nums)


def sorted_squares(nums: List[int]) -> List[int]:
    """
    Squares of a sorted array

    :param nums: given an integer array nums sorted in non-decreasing order
    :return: an array of the squares of each number sorted in non-decreasing.

    >>> sorted_squares(nums=[-4, -1, 0, 3, 10])
    [0, 1, 9, 16, 100]
    >>> sorted_squares(nums=[-7, -3, 2, 3, 11])
    [4, 9, 9, 49, 121]
    """
    slow, fast = 0, len(nums) - 1
    output = [0] * len(nums)
    while slow <= fast:
        if abs(nums[slow]) <= abs(nums[fast]):
            output[fast - slow] = nums[fast] ** 2
            fast -= 1
        elif abs(nums[slow]) > abs(nums[fast]):
            output[fast - slow] = nums[slow] ** 2
            slow += 1
    return output


def three_sum(nums: List[int]) -> List[List[int]]:
    """
    Three sum

    :param nums: given an integer array
    :return: all the  triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

    >>> three_sum(nums=[-1, 0, 1, 2, -1, -4])
    [(-1, -1, 2), (-1, 0, 1)]
    >>> three_sum(nums=[])
    []
    >>> three_sum(nums=[0])
    []
    """
    nums.sort()
    ans = []
    for i in range(len(nums)):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        slow = i + 1
        fast = len(nums) - 1
        while slow < fast:
            curr_sum = nums[i] + nums[slow] + nums[fast]
            if curr_sum == 0:
                ans.append((nums[i], nums[slow], nums[fast]))
                slow += 1
                fast -= 1
                while slow < fast and nums[slow] == nums[slow - 1]:
                    slow += 1
                while slow < fast and nums[fast] == nums[fast + 1]:
                    fast -= 1
            elif curr_sum < 0:
                slow += 1
            else:
                fast -= 1
    return ans


def three_sum_closest(nums: List[int], target: int) -> int:
    """
    Three sum closest

    :param nums: given an integer array nums
    :param target: integer target
    :return: find three integers in nums such that the sum is closest to target and return the sum.

    >>> three_sum_closest(nums=[-1, 2, 1, -4], target=1)
    2
    >>> three_sum_closest(nums=[0, 0, 0], target=1)
    0
    >>> three_sum_closest(nums=[1, 1, -1], target=1)
    1
    """
    nums.sort()
    result = nums[0] + nums[1] + nums[2]
    for i in range(len(nums)):
        slow = i + 1
        fast = len(nums) - 1
        while slow < fast:
            sum = nums[i] + nums[slow] + nums[fast]
            if sum == target:
                return sum
            if abs(sum - target) < abs(result - target):
                result = sum

            if sum < target:
                slow += 1
            elif sum > target:
                fast -= 1
    return result


def subarray_product(nums: List[int], k: int) -> int:
    """
    Nums subarray product less than k

    :param nums: an array of integers
    :param k: an integers
    :return: the number of contiguous subarrays where the product of all the elements in the subarray is strictly less than k.

    >>> subarray_product(nums=[10,5,2,6],k=100)
    8
    >>> subarray_product(nums=[1,2,3],k=0)
    0
    """
    slow = 0
    res = 0
    prod = 1
    for fast in range(len(nums)):
        prod *= nums[fast]

        while prod >= k and slow <= fast:
            prod /= nums[slow]
            slow += 1

        res += fast - slow + 1
    return res


def sort_colors(nums: List[int]) -> None:
    """
    sort colors in-places so that objects of the same color are adjacent.

    :param nums: an array nums in which the 0, 1, 2 represent the color red, white ,and blue.
    :return: sorted nums

    >>> sort_colors(nums=[2,0,2,1,1,0])
    [0, 0, 1, 1, 2, 2]
    >>> sort_colors(nums=[2,0,1])
    [0, 1, 2]
    """
    slow, mid, fast = 0, 0, len(nums) - 1

    while mid <= fast:
        if nums[mid] == 0:
            nums[slow], nums[mid] = nums[mid], nums[slow]
            mid += 1
            slow += 1
        elif nums[mid] == 2:
            nums[fast], nums[mid] = nums[mid], nums[fast]
            mid += 1
            fast -= 1
        else:
            mid += 1
    return nums


def four_sum(nums: List[int], target: int) -> List[List[int]]:
    """
    Four nums

    :param nums: given an integer array
    :param target: nums[a] + nums[b] + nums[c] + nums[d] == target
    :return: an array of all the unique quadruplets

    >>> four_sum(nums=[1,0,-1,0,-2,2], target=0)
    [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
    >>> four_sum(nums=[2,2,2,2], target=8)
    [[2,2,2,2]]
    """
    pass


def backspace_compare(s: str, t: str) -> bool:
    """
    Backspace string compare

    :param s: a string maybe has backspace #
    :param s: a string maybe has backspace #
    :return:  return true if they are equal when both are typed into empty text editors

    >>> backspace_compare(s="ab#c",t="ad#c")
    True
    >>> backspace_compare(s="ab##",t="c#d#")
    True
    >>> backspace_compare(s="a#c",t="b")
    False
    """
    scounter, tcounter = 0, 0
    sfast, tfast = len(s) - 1, len(t) - 1
    while sfast >= 0 or tfast >= 0:
        while sfast >= 0 and (s[sfast] == "#" or scounter):
            if s[sfast] == "#":
                scounter += 1
            else:
                scounter -= 1
            sfast -= 1
        while tfast >= 0 and (t[tfast] == "#" or tcounter):
            if t[tfast] == "#":
                tcounter += 1
            else:
                tcounter -= 1
            tfast -= 1
        if s[sfast] != t[tfast]:
            return False
        sfast -= 1
        tfast -= 1
    return True


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)
