import unittest
'''
https://leetcode.com/problems/count-triplets-that-can-form-two-arrays-of-equal-xor/

1442. Count Triplets That Can Form Two Arrays of Equal XOR
Medium

214

15

Add to List

Share
Given an array of integers arr.

We want to select three indices i, j and k where (0 <= i < j <= k < arr.length).

Let's define a and b as follows:

a = arr[i] ^ arr[i + 1] ^ ... ^ arr[j - 1]
b = arr[j] ^ arr[j + 1] ^ ... ^ arr[k]
Note that ^ denotes the bitwise-xor operation.

Return the number of triplets (i, j and k) Where a == b.

 

Example 1:

Input: arr = [2,3,1,6,7]
Output: 4
Explanation: The triplets are (0,1,2), (0,2,2), (2,3,4) and (2,4,4)
Example 2:

Input: arr = [1,1,1,1,1]
Output: 10
Example 3:

Input: arr = [2,3]
Output: 0
Example 4:

Input: arr = [1,3,5,7,9]
Output: 3
Example 5:

Input: arr = [7,11,12,9,5,2,7,17,22]
Output: 8
 

Constraints:

1 <= arr.length <= 300
1 <= arr[i] <= 10^8

'''
from typing import List

class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        result = 0
        for i in range (len(arr)):
            
            xor = arr[i]
            for j in range (i+1, len(arr)):
                print(arr, arr[i], arr[j], xor, xor^arr[j])
                xor ^=arr[j]
                if xor == 0:
                    result +=j-i
                
        return result




class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_1(self):
        self.assertEqual(self.solution.countTriplets([2,3,1,6,7]), 4)

    def test_2(self):
        self.assertEqual(self.solution.countTriplets([1,1,1,1,1]), 10)

    def test_3(self):
        self.assertEqual(self.solution.countTriplets([2,3]), 0)

    def test_4(self):
        self.assertEqual(self.solution.countTriplets([1,3,5,7,9]), 3)

    def test_5(self):
        self.assertEqual(self.solution.countTriplets([7,11,12,9,5,2,7,17,22]), 8)


if __name__ == '__main__':
    unittest.main()
