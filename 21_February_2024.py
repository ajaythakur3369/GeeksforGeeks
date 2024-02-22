'''
Task:- 
Given a boolean expression s of length n with following symbols.
Symbols
    'T' ---> true
    'F' ---> false
and following operators filled between symbols
Operators
    &   ---> boolean AND
    |   ---> boolean OR
    ^   ---> boolean XOR
Count the number of ways we can parenthesize the expression so that the value of expression evaluates to true.
'''

'''
Example 1:- 
Input: 
n = 7
s = T|T&F^T
Output: 
4
Explaination: 
The expression evaluates to true in 4 ways ((T|T)&(F^T)), (T|(T&(F^T))), (((T|T)&F)^T) and (T|((T&F)^T)).
'''

'''
Example 2:- 
Input: 
n = 5
s = T^F|F
Output: 
2
Explaination: 
((T^F)|F) and (T^(F|F)) are the only ways.
'''

'''
Complexity:- 
 Expected Time Complexity: O(n^3)
 Expected Auxiliary Space: O(n^2)
'''

'''
Constraints:-
 1 ≤ n ≤ 200 
'''

'''
User function Template for python3
'''

class Solution:
    def countWays(self, n, s):
        
        '''
        Code here
        '''
        
        from functools import lru_cache
        
        @lru_cache(None)
        def count(i, j, result=True):
            if i == j:
                if result:
                    return int(s[i:j+1] == 'T')
                else:
                    return int(s[i:j+1] == 'F')
            r = 0
            for k in range(i+1, j, 2):
                if s[k] == '&':
                    if result:
                        r += count(i, k-1, True) * count(k+1, j, True)
                    else:
                        r += count(i, k-1, False) * count(k+1, j, False)
                        r += count(i, k-1, False) * count(k+1, j, True)
                        r += count(i, k-1, True) * count(k+1, j, False)
                if s[k] == '|':
                    if result:
                        r += count(i, k-1, True) * count(k+1, j, False)
                        r += count(i, k-1, False) * count(k+1, j, True)
                        r += count(i, k-1, True) * count(k+1, j, True)
                    else:
                        r += count(i, k-1, False) * count(k+1, j, False)
                if s[k] == '^':
                    if result:
                        r += count(i, k-1, True) * count(k+1, j, False)
                        r += count(i, k-1, False) * count(k+1, j, True)
                    else:
                        r += count(i, k-1, False) * count(k+1, j, False)
                        r += count(i, k-1, True) * count(k+1, j, True)
            return r%1003
        return count(0, n-1)