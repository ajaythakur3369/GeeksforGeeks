'''
Task:- 
Given 3 strings A, B and C, the task is to find the length of the longest sub-sequence that is common in all the three given strings.
'''

'''
Example 1:- 
Input:
A = "geeks"
B = "geeksfor", 
C = "geeksforgeeks"
Output: 5
Explanation: 
"geeks"is the longest common
subsequence with length 5.
'''

'''
Example 2:- 
Input: 
A = "abcd"
B = "efgh"
C = "ijkl"
Output: 0
Explanation: 
There's no subsequence common
in all the three strings.
'''

'''
Complexity:- 
 Expected Time Complexity: O(n1*n2*n3).
 Expected Auxiliary Space: O(n1*n2*n3).
'''

'''
Constraints:- 
 1 <= n1, n2, n3 <= 20
Elements of the strings consitutes only of the lower case english alphabets.
'''

'''
User function Template for python3
'''

class Solution:

    def LCSof3(self,A,B,C,n1,n2,n3):
        
        '''
        Code here
        '''
        
        dp=[[[0 for _ in range(n3+1)]for _ in range(n2+1)]for _ in range(n1+1)]
        for i in range(1,n1+1):
            for j in range(1,n2+1):
                for k in range(1,n3+1):
                    if A[i-1]==B[j-1] and B[j-1]==C[k-1]:
                        dp[i][j][k]=dp[i-1][j-1][k-1]+1
                    else:
                        dp[i][j][k]=max(dp[i-1][j][k],dp[i][j-1][k],dp[i][j][k-1])
        return dp[-1][-1][-1]
