"""
1071. Greatest Common Divisor of Strings (https://leetcode.com/problems/greatest-common-divisor-of-strings)

For two strings s and t, we say "t divides s" if and only if s = t + t + t + ... + t + t (i.e., t is concatenated with itself one or more times).

Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2.



Example 1:

Input: str1 = "ABCABC", str2 = "ABC"
Output: "ABC"

Example 2:

Input: str1 = "ABABAB", str2 = "ABAB"
Output: "AB"

Example 3:

Input: str1 = "LEET", str2 = "CODE"
Output: ""



Constraints:

    1 <= str1.length, str2.length <= 1000
    str1 and str2 consist of English uppercase letters.


"""
from math import gcd


def _my_solution(str1: str, str2: str) -> str:
    if str1 == str2:
        return str1

    largest = str1
    smallest = str2

    if len(str1) < len(str2):
        smallest = str1
        largest = str2

    solution = ""

    for i in range(1, len(smallest) + 1):
        divisor = smallest[0:i]

        largest_factor = len(largest) // len(divisor)
        smallest_factor = len(smallest) // len(divisor)

        if (divisor * largest_factor) == largest and (divisor * smallest_factor) == smallest:
            solution = divisor
    return solution


def _official_solution(str1: str, str2: str) -> str:
    # Check if they have non-zero GCD string.
    if str1 + str2 != str2 + str1:
        return ""

    # Get the GCD of the two lengths.
    max_length = gcd(len(str1), len(str2))
    return str1[:max_length]


def greatest_common_divisor_of_strings(str1: str, str2: str) -> str:
    assert _my_solution(str1, str2) == _official_solution(str1, str2)
    return _my_solution(str1, str2)
