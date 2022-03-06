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

    def judge_squaresum(self, c: int) -> bool:
        """
        Sum of Square Numbers
        :param c: given a non-nagative integer.
        :return: whether there're two integers a and b such that a^2 + b^2 = c

        >>> DoublePoint().judge_squaresum(c=10)
        True
        >>> DoublePoint().judge_squaresum(c=3)
        False
        """
        slow, fast = 0, int(math.sqrt(c))
        while slow < fast:
            result = slow**2 + fast**2
            if result < c:
                slow += 1
            elif result > c:
                fast -= 1
            else:
                return True
        return False

    def reverse_vowels(self, s: str) -> str:
        """
        Reverse all vowels in a string
        :param s: given a string s contains vowels 'a','e','i','o','u' and capital letters
        :return: reverse only all the vowels in s and return it.

        >>> DoublePoint().reverse_vowels(s='hello')
        'holle'
        >>> DoublePoint().reverse_vowels(s='leetcode')
        'leotcede'
        """
        vowels = set('aeiouAEIOU')
        slow, fast = 0, len(s) - 1
        s = list(s)
        while slow < fast:
            if s[slow] in vowels:
                while fast > 0 and s[fast] not in vowels:
                    fast -= 1
                s[slow], s[fast] = s[fast], s[slow]
                slow += 1
                fast -= 1
            else:
                slow += 1
        return "".join(s)


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)
