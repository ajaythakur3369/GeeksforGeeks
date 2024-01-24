'''
Task:- 
GeeksforGeeks has introduced a special offer where you can enroll in any course, and if you manage to complete 90% of the course within 90 days, you will receive a refund of 90%.

Geek was fascinated by this offer. This offer was valid for only n days, and each day a new course was available for purchase. Geek decided that if he bought a course on some day, he will complete that course on the same day itself and redeem floor[90% of cost of the course] amount back. Find the maximum number of courses that Geek can complete in those n days if he had total amount initially.
'''

'''
Example 1:- 
Input:
n = 2
total = 10
cost = [10, 9]
Output: 2
Explanation: 
Geek can buy the first course for 10 amount, 
complete it on the same date and redeem 9 back. 
Next, he can buy and complete the 2nd course too.
'''

'''
Example 2:- 
Input:
n = 11
total = 10
cost = [10, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
Output: 10
Explanation: 
Geek can buy and complete all the courses that cost 1
 as well as 1 course that cost 10 and 9 course that cost 1.
'''

'''
Complexity:- 
 Expected Time Complexity: O(n*total)
 Expected Auxiliary Space: O(n*total)
'''

'''
Constraints:-
 1 <= n <= 1000
 0 <= total <= 1000
 1 <= cost[i] <= 1000
'''

from typing import List

class Solution:
    def max_courses(self, n: int, total: int, cost: List[int]) -> int:
        def maxi_course(i: int, n: int, avail: int, cost: List[int], dp: List[List[int]]) -> int:
            if i == n-1:
                if avail >= cost[i]:
                    return 1
                return 0
            if avail <= 0:
                return 0
            if dp[i][avail] != -1:
                return dp[i][avail]
            taken = 0
            if avail >= cost[i]:
                newavail = avail
                newavail -= cost[i]
                newavail += int(0.9 * cost[i])
                taken = 1 + maxi_course(i+1, n, newavail, cost, dp)
            nottaken = 0 + maxi_course(i+1, n, avail, cost, dp)
            dp[i][avail] = max(taken, nottaken)
            return dp[i][avail]

        dp = [[-1] * (total+1) for _ in range(n+1)]
        ans = maxi_course(0, n, total, cost, dp)
        return ans












