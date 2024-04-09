from unittest import TestCase

from p_01_array_string.m_01_merge_strings_alternately import merge_strings_alternately
from p_01_array_string.m_02_greatest_common_divisor_of_strings import greatest_common_divisor_of_strings
from p_01_array_string.m_03_kids_with_the_greatest_number_of_candies import kids_with_the_greatest_number_of_candies
from p_01_array_string.m_04_can_place_flowers import can_place_flowers
from p_01_array_string.m_05_reverse_vowels_of_a_string import reverse_vowels_of_a_string
from p_01_array_string.m_06_reverse_words_in_a_string import reverse_words_in_a_string


class TestArrayString(TestCase):
    def test_merge_strings_alternately(self):
        assert merge_strings_alternately(word1="abc", word2="pqr") == "apbqcr"
        assert merge_strings_alternately(word1="ab", word2="pqrs") == "apbqrs"
        assert merge_strings_alternately(word1="abcd", word2="pq") == "apbqcd"

    def test_greatest_common_divisor_of_strings(self):
        assert greatest_common_divisor_of_strings(str1="ABCABC", str2="ABC") == "ABC"
        assert greatest_common_divisor_of_strings(str1="ABABAB", str2="ABAB") == "AB"
        assert greatest_common_divisor_of_strings(str1="LEET", str2="CODE") == ""

    def test_kids_with_the_greatest_number_of_candies(self):
        assert (kids_with_the_greatest_number_of_candies(candies=[2, 3, 5, 1, 3], extra_candies=3)
                == [True, True, True, False, True])
        assert (kids_with_the_greatest_number_of_candies(candies=[4, 2, 1, 1, 2], extra_candies=1)
                == [True, False, False, False, False])
        assert (kids_with_the_greatest_number_of_candies(candies=[12, 1, 12], extra_candies=10)
                == [True, False, True])

    def test_can_place_flowers(self):
        assert can_place_flowers(flowerbed=[1, 0, 0, 0, 1], n=1) is True
        assert can_place_flowers(flowerbed=[1, 0, 0, 0, 1], n=2) is False

    def test_reverse_vowels_of_a_string(self):
        assert reverse_vowels_of_a_string(s="hello") == "holle"
        assert reverse_vowels_of_a_string(s="leetcode") == "leotcede"

    def test_reverse_words_in_a_string(self):
        assert reverse_words_in_a_string(s="the sky is blue") == "blue is sky the"
        assert reverse_words_in_a_string(s="  hello world  ") == "world hello"
        assert reverse_words_in_a_string(s="a good   example") == "example good a"
