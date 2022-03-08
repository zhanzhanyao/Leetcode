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
        vowels = set("aeiouAEIOU")
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

    def valid_palindrome(self, s: str) -> bool:
        """
        Valid palindrome
        :param s: given a string s
        :return: return true if the s can be palindrome after deleting at most one character.

        >>> DoublePoint().valid_palindrome(s='aba')
        True
        >>> DoublePoint().valid_palindrome(s='abca')
        True
        >>> DoublePoint().valid_palindrome(s='abc')
        False
        """

        def is_palindrome(i, j) -> bool:
            while i < j:
                if s[i] != s[j]:
                    return False
                i += 1
                j -= 1
            return True

        slow, fast = 0, len(s) - 1
        while slow <= fast:
            if s[slow] == s[fast]:
                slow += 1
                fast -= 1
            else:
                return is_palindrome(slow + 1, fast) or is_palindrome(slow, fast - 1)
        return True

    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> List[int]:
        """
        Merge sorted array
        :param nums1: non-decreasing order
        :param m: the number of nums1, exclude 0 in the end of nums1
        :param nums2: non-decreasing order
        :param n:  the number of nums2
        :return: merge num1 and num2 into num1 sorted in non-decreasing order.

        >>> DoublePoint().merge(nums1=[1,2,3,0,0,0], m=3, nums2=[2,5,6], n=3)
        [1, 2, 2, 3, 5, 6]
        >>> DoublePoint().merge(nums1=[1], m=1, nums2=[], n=0)
        [1]
        >>> DoublePoint().merge(nums1=[0], m=0, nums2=[1], n=1)
        [1]
        """
        slow, fast = m - 1, n - 1
        tail = m + n - 1
        while slow >= 0 or fast >= 0:
            if slow == -1:
                nums1[tail] = nums2[fast]
                fast -= 1
            elif fast == -1:
                nums1[tail] = nums1[slow]
                slow -= 1
            elif nums1[slow] > nums2[fast]:
                nums1[tail] = nums1[slow]
                slow -= 1
            else:
                nums1[tail] = nums2[fast]
                fast -= 1
            tail -= 1
        return nums1

    def find_longestword(self, s: str, dictionary: List[str]) -> str:
        """
        Longest word in dictionary through deleting
        :param s:
        :param dictionary:
        :return: the longest string in the dictionary that can be formed by deleting some of the given string characters.

        >>> DoublePoint().find_longestword(s="abpcplea", dictionary=["ale","apple","monkey","plea"])
        "apple"
        >>> DoublePoint().find_longestword(s="abpcplea", dictionary=["a","b","c"])
        "a"
        """
        for word in dictionary:
            slow, fast = 0, 0
            while slow < len(s) and fast < len(word):
                if s[slow] == word[fast]:
                    fast += 1
                slow += 1
            if fast == len(word):
                pass


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)
