'''
Task:- 
Consider a game where a player can score 3 or 5 or 10 points in a move. Given a total score n, find number of distinct combinations to reach the given score.
'''

'''
Example 1:-
Input
n = 10
Output
2
Explanation
There are two ways {5,5} and {10}.
'''

'''
Example 2:-
Input
n = 20
Output
4
Explanation
There are four possible ways. {5,5,5,5}, {3,3,3,3,3,5}, {10,10}, {5,5,10}.
'''

'''
Complexity:- 
 Expected Time Complexity: O(n)
 Expected Auxiliary Space: O(n)
'''

'''
Constraints:- 
 1 ≤ n ≤ 5*10^5
'''

'''
User function Template for python3
'''

class Solution:
    def count(self, n: int) -> int:
        
        '''
        Your code here
        '''
        
        dp=[0]*(n+1)
        dp[0]=1
        for i in range(3,n+1):
            dp[i]=dp[i]+dp[i-3]
        for i in range(5,n+1):
            dp[i]=dp[i]+dp[i-5]
        for i in range(10,n+1):
            dp[i]=dp[i]+dp[i-10]
        return dp[-1]