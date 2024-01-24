'''
Task:- 
There is a road passing through a city with N plots on both sides of the road. Plots are arranged in a straight line on either side of the road. Determine the total number of ways to construct buildings in these plots, ensuring that no two buildings are adjacent to each other. Specifically, buildings on opposite sides of the road cannot be adjacent.

Using * to represent a plot and || for the road, the arrangement for N = 3 can be visualized as follows: * * * || * * *.
'''

'''
Example 1:- 
Input: N = 1
Output: 4
Explanation: 
Possible ways for the arrangement are B||*, *||B, B||B, *||*
where B represents a building.
'''

'''
Example 2:- 
Input: N = 3
Output: 25
Explanation: 
Possible ways for one side are BSS, BSB, SSS, SBS,
SSB where B represents a building and S
represents an empty space. Pairing up with 
possibilities on the other side of the road,
total possible ways are 25.
'''

'''
Complexity:- 
 Expected Time Complexity: O(N)
 Expected Space Complexity: O(N)
'''

'''
Constraints:-
 1 <= N <= 100000
'''

'''
User function Template for python3
'''

class Solution:
    def TotalWays(self, N):
        if N == 1:
            return 4
        if N == 2:
            return 9
        mod = 1000000007
        previous_two = 2
        previous_one = 3
        present = 0
        for i in range(3, N + 1):
            present = (previous_one + previous_two + mod) % mod
            previous_two = previous_one
            previous_one = present
        total = ((present % mod) * (present % mod)) % mod
        return total











