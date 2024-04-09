"""
345. Reverse Vowels of a String (https://leetcode.com/problems/reverse-vowels-of-a-string)

Given a string s, reverse only all the vowels in the string and return it.

The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.



Example 1:

Input: s = "hello"
Output: "holle"

Example 2:

Input: s = "leetcode"
Output: "leotcede"



Constraints:

    1 <= s.length <= 3 * 105
    s consist of printable ASCII characters.


"""


def _my_solution(s: str) -> str:
    s = list(s)
    left = 0
    right = len(s) - 1
    vowels = "aAeEiIoOuU"
    while left < right:
        if s[left] in vowels and s[right] in vowels:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
        elif s[left] not in vowels:
            left += 1
        elif s[right] not in vowels:
            right -= 1
    return "".join(s)


def _most_voted_solution(s: str) -> str:
    # Convert the input string to a character array.
    word = list(s)
    start = 0
    end = len(s) - 1
    vowels = "aeiouAEIOU"

    # Loop until the start pointer is no longer less than the end pointer.
    while start < end:
        # Move the start pointer towards the end until it points to a vowel.
        while start < end and vowels.find(word[start]) == -1:
            start += 1

        # Move the end pointer towards the start until it points to a vowel.
        while start < end and vowels.find(word[end]) == -1:
            end -= 1

        # Swap the vowels found at the start and end positions.
        word[start], word[end] = word[end], word[start]

        # Move the pointers towards each other for the next iteration.
        start += 1
        end -= 1

    # Convert the character array back to a string and return the result.
    return "".join(word)


def reverse_vowels_of_a_string(s: str) -> str:
    assert _my_solution(s) == _most_voted_solution(s)
    return _my_solution(s)
