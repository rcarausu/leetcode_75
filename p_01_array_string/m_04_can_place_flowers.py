"""
605. Can Place Flowers (https://leetcode.com/problems/can-place-flowers)

You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be planted in adjacent plots.

Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, and an integer n, return true if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule and false otherwise.



Example 1:

Input: flowerbed = [1,0,0,0,1], n = 1
Output: true

Example 2:

Input: flowerbed = [1,0,0,0,1], n = 2
Output: false



Constraints:

    1 <= flowerbed.length <= 2 * 104
    flowerbed[i] is 0 or 1.
    There are no two adjacent flowers in flowerbed.
    0 <= n <= flowerbed.length
"""
from typing import List


def _my_solution(flowerbed: List[int], n: int) -> bool:
    length = len(flowerbed)
    if n > length:
        return False

    flowers = 0

    for i in range(length):
        if flowerbed[i] == 0:
            left = (i == 0) or (flowerbed[i - 1] == 0)
            right = (i == length - 1) or (flowerbed[i + 1] == 0)
            if left and right:
                flowers += 1
                flowerbed[i] = 1

    return flowers >= n


def _official_solution(flowerbed: List[int], n: int) -> bool:
    count = 0
    for i in range(len(flowerbed)):
        # Check if the current plot is empty.
        if flowerbed[i] == 0:
            # Check if the left and right plots are empty.
            empty_left_plot = (i == 0) or (flowerbed[i - 1] == 0)
            empty_right_lot = (i == len(flowerbed) - 1) or (flowerbed[i + 1] == 0)

            # If both plots are empty, we can plant a flower here.
            if empty_left_plot and empty_right_lot:
                flowerbed[i] = 1
                count += 1
                if count >= n:
                    return True

    return count >= n


def can_place_flowers(flowerbed: List[int], n: int) -> bool:
    assert _my_solution(flowerbed.copy(), n) == _official_solution(flowerbed.copy(), n)
    return _my_solution(flowerbed, n)
