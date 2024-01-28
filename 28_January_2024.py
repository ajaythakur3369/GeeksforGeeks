'''
Task:- 
It is a universal fact that Geekina hates 1s however it is also known that Geekina loves the integers having atmost k 1s (set-bits) in their binary representation. 

Geekina demanded nth such non-negative number from Geek, and being a good friend of Geek, now it's your responsibility to tell him that number.
'''

'''
Example 1:- 
Input:
n = 5
k = 1
Output:
8
Explanation:
Following numbers are loved by Geekina -
0 = (0)2
1 = (1)2
2 = (10)2
4 = (100)2
8 = (1000)2
'''

'''
Example 2:- 
Input:
n = 6
k = 2
Output:
5
Explanation:
Following numbers are loved by Geekina -
0 = (0)2
1 = (1)2
2 = (10)2
3 = (11)2
4 = (100)2
5 = (101)2
'''

'''
Complexity:- 
 Expected Time Complexity: O(k*log(n) + constant)
 Expected Auxiliary Space: O(k*log(n) + constant)
'''

'''
Constraints:-
 1 <= n <= 10^9
 1 <= k <= 63
'''

from typing import List

class Solution:
    def findNthNumber(self, n, k):
        low, high = 0, 10 ** 18
        self.dp = [[[-1] * 65 for _ in range(65)] for _ in range(2)]

        while low <= high:
            mid = low + (high - low) // 2
            count = self.find(mid, k)
            if count >= n:
                high = mid - 1
            else:
                low = mid + 1
        return low

    def find(self, n, k):
        s = format(n, 'b').zfill(64)
        self.reset()
        return self.dpf(s, len(s), 1, k)

    def dpf(self, s, n, tight, k):
        if k < 0:
            return 0
        if n == 0:
            return 1
        if self.dp[tight][k][n] is not None:
            return self.dp[tight][k][n]

        ub = int(s[len(s) - n]) if tight == 1 else 1
        ans = 0
        for dig in range(ub + 1):
            if dig == ub:
                ans += self.dpf(s, n - 1, tight, k - dig)
            else:
                ans += self.dpf(s, n - 1, 0, k - dig)
        self.dp[tight][k][n] = ans
        return ans

    def reset(self):
        for i in range(65):
            for j in range(65):
                self.dp[0][i][j] = None
                self.dp[1][i][j] = None