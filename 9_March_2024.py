'''
Task:- 
Given a binary string s. Perform r iterations on string s, where in each iteration 0 becomes 01 and 1 becomes 10. Find the nth character (considering 0 based indexing) of the string after performing these r iterations (see examples for better understanding).
'''

'''
Example 1:- 
Input:
s = "1100"
r = 2
n = 3
Output:
1
Explanation: 
After 1st iteration s becomes "10100101".
After 2nd iteration s becomes "1001100101100110".
Now, we can clearly see that the character at 3rd index is 1, and so the output.
'''

'''
Example 2:- 
Input:
s = "1010"
r = 1
n = 2
Output:
0
Explanation : 
After 1st iteration s becomes "10011001".
Now, we can clearly see that the character at 2nd index is 0, and so the output.
'''

'''
Complexity:- 
 Expected Time Complexity: O(r*|s|)
 Expected Auxilary Space: O(|s|)
'''

'''
Constraints:- 
 1 ≤ |s| ≤ 10^3
 1 ≤ r ≤ 20
 0 ≤ n < |s|
'''

'''
User function Template for python3
'''

class Solution:
    def nthCharacter(self, s, r, n):
        
        '''
        Code here
        '''
        
        for i in range(r,0,-1):
            a=n//(2**i)
            n-=a*(2**i)
            if(s[a]=='0'):
                s='01'
            else:
                s='10'
        return s[n]