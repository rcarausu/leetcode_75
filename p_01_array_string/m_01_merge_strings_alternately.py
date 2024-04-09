"""
1768. Merge Strings Alternately (https://leetcode.com/problems/merge-strings-alternately)

You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1. If a string is longer than the other, append the additional letters onto the end of the merged string.

Return the merged string.


Example 1:

Input: word1 = "abc", word2 = "pqr"
Output: "apbqcr"
Explanation: The merged string will be merged as so:
word1:  a   b   c
word2:    p   q   r
merged: a p b q c r

Example 2:

Input: word1 = "ab", word2 = "pqrs"
Output: "apbqrs"
Explanation: Notice that as word2 is longer, "rs" is appended to the end.
word1:  a   b
word2:    p   q   r   s
merged: a p b q   r   s

Example 3:

Input: word1 = "abcd", word2 = "pq"
Output: "apbqcd"
Explanation: Notice that as word1 is longer, "cd" is appended to the end.
word1:  a   b   c   d
word2:    p   q
merged: a p b q c   d
"""


def _my_solution(word1: str, word2: str) -> str:
    max_length = max(len(word1), len(word2))
    result = []
    for i in range(0, max_length):
        if i < len(word1):
            result.append(word1[i])
        if i < len(word2):
            result.append(word2[i])
            "".strip()
    return "".join(result)


def _official_solution(word1: str, word2: str) -> str:
    result = []
    n = max(len(word1), len(word2))
    for i in range(n):
        if i < len(word1):
            result += word1[i]
        if i < len(word2):
            result += word2[i]

    return "".join(result)


def merge_strings_alternately(word1: str, word2: str) -> str:
    assert _my_solution(word1, word2) == _official_solution(word1, word2)
    return _my_solution(word1, word2)
