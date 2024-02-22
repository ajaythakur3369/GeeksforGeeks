'''
Task:- 
Given two strings s and t of length n and m respectively. Find the count of distinct occurrences of t in s as a sub-sequence modulo 10^9 + 7.
'''

'''
Example 1:- 
Input:
s = "banana" , t = "ban"
Output: 
3
Explanation: 
There are 3 sub-sequences:[ban], [ba n], [b an].
'''

'''
Example 2:- 
Input:
s = "geeksforgeeks" , t = "ge"
Output: 
6
Explanation: 
There are 6 sub-sequences:[ge], [ge], [g e], [g e] [g e] and [g e].
'''

'''
Complexity:- 
 Expected Time Complexity: O(n*m).
 Expected Auxiliary Space: O(n*m).
'''

'''
Constraints:- 
 1 ≤ n,m ≤ 1000
'''

'''
Your task is to complete this function
Finction should return Integer
'''

class Solution:
    def sequenceCount(self,s, t):
        
        '''
        Code here
        '''
        
        m=len(s)
        n=len(t)
        if m>n:
            m,n=n,m
            s,t=t,s
        from functools import lru_cache
        @lru_cache(None)
        def dp(i=0,j=0):
            nonlocal s,t,m,n
            if i>=m:
                return 1
            nxtj=t.find(s[i],j)
            if nxtj>=0:
                return (dp(i,nxtj+1)+dp(i+1,nxtj+1))%(10**9+7)
            return 0
        return dp()