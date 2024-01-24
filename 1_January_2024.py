'''
Task:- 
Given an array of integers nums and a number k, write a function that returns true if given array can be divided into pairs such that sum of every pair is divisible by k.
'''

'''
Example 1:- 
Input: 
nums = [9, 5, 7, 3]
k = 6
Output: 
True
Explanation: 
{(9, 3), (5, 7)} is a 
possible solution. 9 + 3 = 12 is divisible
by 6 and 7 + 5 = 12 is also divisible by 6.
'''

'''
Example 2:- 
Input: 
nums = [4, 4, 4]
k = 4
Output: 
False
Explanation: 
You can make 1 pair at max, leaving a single 4 unpaired.
'''

'''
Complexity:- 
 Expected Time Complexity: O(n)
 Expected Space Complexity : O(n)
'''

'''
Constraints:- 
 1 <= length( nums ) <= 10^5
 1 <= numsi <= 10^5
 1 <= k <= 10^5
'''

'''
User function Template for python3
'''

class Solution:
    def canPair(self, nuns, k):
        # Code here
        if len(nums) % 2 != 0:
            return False
        mp = {}
        for i in nums:
            y = i % k
            if mp.get((k - y) % k, 0) != 0:
                mp[(k - y) % k] -= 1
            else:
                mp[y] = mp.get(y, 0) + 1
        for key, value in mp.items():
            if value != 0:
                return False
        return True











