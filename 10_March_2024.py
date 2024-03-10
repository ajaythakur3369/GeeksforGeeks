'''
Task:- 
Given a string str which may contains lowercase and uppercase chracters. The task is to remove all duplicate characters from the string and find the resultant string. The order of remaining characters in the output should be same as in the original string.
'''

'''
Example 1:- 
Input:
str = "geEksforGEeks"
Output: 
"geEksforG"
Explanation: 
After removing duplicate characters such as E, e, k, s, we have string as "geEksforG".
'''

'''
Example 2:- 
Input:
str = "HaPpyNewYear"
Output: 
"HaPpyNewYr"
Explanation: 
After removing duplicate characters such as e, a, we have string as "HaPpyNewYr".
'''

'''
Complexity:- 
 Expected Time Complexity: O(N)
 Expected Auxiliary Space: O(N)
'''

'''
Constraints:-
 1 ≤ N ≤ 10^5
 String contains uppercase and lowercase english letters.
'''

'''
User function Template for python3
'''

class Solution:
    def removeDuplicates(self, str):
        '''
        Code here
        '''
        
        mp = {}
        ans = ''
        for char in str:
            if mp.get(char, 0) == 0:
                ans += char
                mp[char] = mp.get(char, 0) + 1
        return ans