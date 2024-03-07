'''
Task:- 
Given a string s of length n, find all the possible subsequences of the string s in lexicographically-sorted order.
'''

'''
Example 1:- 
Input : 
s = "abc"
Output: 
a ab abc ac b bc c
Explanation : 
There are a total 7 number of subsequences possible 
for the given string, and they are mentioned above 
in lexicographically sorted order.
'''

'''
Example 2:- 
Input: 
s = "aa"
Output: 
a a aa
Explanation : 
There are a total 3 number of subsequences possible 
for the given string, and they are mentioned above 
in lexicographically sorted order.
'''

'''
Complexity:- 
 Expected Time Complexity: O( n*2^n)
 Expected Space Complexity: O( n * 2^n)
'''

'''
Constraints:- 
 1 <= n <= 16
 s will constitute of lower case english alphabets
'''

'''
User function Template for python3
'''

class Solution:
    def AllPossibleStrings(self, s):
        
        '''
        Code here
        '''
        
        ret, n = [], len(s)
        
        def collect(i, sofar=""):
            nonlocal ret, n, s
            if sofar:
                ret.append(sofar)
            if i >= n:
                return
            
            for k in range(i, n):
                collect(k+1, sofar+s[k])
        
        collect(0)
        return sorted(ret)