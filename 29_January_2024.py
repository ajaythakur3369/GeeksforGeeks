'''
Task:-
Given a string str consisting of digits, you can divide it into sub-groups by separating the string into substrings. For example, "112" can be divided as {"1", "1", "2"}, {"11", "2"}, {"1", "12"}, and {"112"}.

A valid grouping can be done if you are able to divide sub-groups where the sum of digits in a sub-group is less than or equal to the sum of the digits of the sub-group immediately right to it. Your task is to determine the total number of valid groupings that could be done for a given string.
'''

'''
Example 1:- 
Input: 
str = "1119"
Output: 
7
Explanation: 
One valid grouping is {"1", "11", "9"}.
Sum of digits of first sub-group ("1") is 1,
for the second sub-group ("11"), it is 2,
and for the third one ("9"), it is 9.
As the sum of digits of the sub-groups is 
in increasing order, it forms a valid grouping.
Other valid grouping are {"1", "119"}, {"1","1","19"}, 
{"1","1","1","9"}, {"11","19"}, {"111","9"} and {"1119"}
are six other valid groupings.
'''

'''
Example 2:- 
Input: 
str = "12"
Output: 
2
Explanation: 
{"1","2"} and {"12"} are two valid groupings.
'''

'''
Complexity:- 
 Expected Time Complexity: O(N^3) where N is the length of the string.
 Expected Space Complexity: O(N^2)
'''

'''
Constraints:- 
 1 <= N <= 100
 stri ∈ {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
'''

class Solution:
    def TotalCount(self, s):
        n = len(s)
        summ = 0

        for i in s:
            summ += int(i)

        dp = [[-1 for _ in range(summ + 1)] for _ in range(n + 1)]

        return self.group(n, 0, 0, s, dp)

    def group(self, n, idx, initialsum, s, dp):
        if idx == n:
            return 1

        if dp[idx][initialsum] != -1:
            return dp[idx][initialsum]

        cursum = 0
        ans = 0

        for i in range(idx, n):
            cursum += int(s[i])

            if cursum >= initialsum:
                ans += self.group(n, i + 1, cursum, s, dp)

        dp[idx][initialsum] = ans

        return dp[idx][initialsum]