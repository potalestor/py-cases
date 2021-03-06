
'''
https://leetcode.com/explore/challenge/card/june-leetcoding-challenge/539/week-1-june-1st-june-7th/3351/

Given an array w of positive integers, where w[i] describes the weight of index i, write a function pickIndex which randomly picks an index in proportion to its weight.

Note:

1 <= w.length <= 10000
1 <= w[i] <= 10^5
pickIndex will be called at most 10000 times.
Example 1:

Input: 
["Solution","pickIndex"]
[[[1]],[]]
Output: [null,0]
Example 2:

Input: 
["Solution","pickIndex","pickIndex","pickIndex","pickIndex","pickIndex"]
[[[1,3]],[],[],[],[],[]]
Output: [null,0,1,1,1,0]
Explanation of Input Syntax:

The input is two lists: the subroutines called and their arguments. Solution's constructor has one argument, the array w. pickIndex has no arguments. Arguments are always wrapped with a list, even if there aren't any.

'''
from typing import List
from itertools import accumulate 
import bisect
import random
import itertools

class Solution:
    def __init__(self, w: List[int]):
        self.sum = list(accumulate(w))

    def pickIndex(self) -> int:
       return bisect.bisect_left(self.sum, self.sum[-1]* random.random())
        


s = Solution([1, 3, 3, 4])
print([s.pickIndex() for _ in range(10)])

