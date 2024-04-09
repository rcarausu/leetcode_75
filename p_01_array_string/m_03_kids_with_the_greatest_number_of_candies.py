"""
1431. Kids With the Greatest Number of Candies (https://leetcode.com/problems/kids-with-the-greatest-number-of-candies)

There are n kids with candies. You are given an integer array candies, where each candies[i] represents the number of candies the ith kid has, and an integer extraCandies, denoting the number of extra candies that you have.

Return a boolean array result of length n, where result[i] is true if, after giving the ith kid all the extraCandies, they will have the greatest number of candies among all the kids, or false otherwise.

Note that multiple kids can have the greatest number of candies.



Example 1:

Input: candies = [2,3,5,1,3], extraCandies = 3
Output: [true,true,true,false,true]
Explanation: If you give all extraCandies to:
- Kid 1, they will have 2 + 3 = 5 candies, which is the greatest among the kids.
- Kid 2, they will have 3 + 3 = 6 candies, which is the greatest among the kids.
- Kid 3, they will have 5 + 3 = 8 candies, which is the greatest among the kids.
- Kid 4, they will have 1 + 3 = 4 candies, which is not the greatest among the kids.
- Kid 5, they will have 3 + 3 = 6 candies, which is the greatest among the kids.

Example 2:

Input: candies = [4,2,1,1,2], extraCandies = 1
Output: [true,false,false,false,false]
Explanation: There is only 1 extra candy.
Kid 1 will always have the greatest number of candies, even if a different kid is given the extra candy.

Example 3:

Input: candies = [12,1,12], extraCandies = 10
Output: [true,false,true]


"""
from typing import List


def _my_solution(candies: List[int], extra_candies: int) -> List[bool]:
    previous_max = max(candies)
    return [c + extra_candies >= previous_max for c in candies]


def _official_solution(candies: List[int], extra_candies: int) -> List[bool]:
    # Find out the greatest number of candies among all the kids.
    maxCandies = max(candies)
    # For each kid, check if they will have greatest number of candies
    # among all the kids.
    result = []
    for i in range(len(candies)):
        result.append(candies[i] + extra_candies >= maxCandies)
    return result


def kids_with_the_greatest_number_of_candies(candies: List[int], extra_candies: int) -> List[bool]:
    assert _my_solution(candies, extra_candies) == _official_solution(candies, extra_candies)
    return _my_solution(candies, extra_candies)
