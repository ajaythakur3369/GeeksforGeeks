'''
Task:- 
Given a string s check if it is "Panagram" or not.

A "Panagram" is a sentence containing every letter in the English Alphabet.
'''

'''
Example 1:- 
Input:
s = "Bawds jog, flick quartz, vex nymph"
Output: 
1
Explanation: 
In the given input, there
are all the letters of the English
alphabet. Hence, the output is 1.
'''

'''
Example 2:- 
Input:
s = "sdfs"
Output: 
0
Explanation: 
In the given input, there
aren't all the letters present in the
English alphabet. Hence, the output
is 0.
'''

'''
Complexity:- 
 Expected Time Complexity: O( |s| )
 Expected Auxiliary Space: O(1)
|s| denotes the length of the input string.
'''

'''
Constraints:- 
 1 ≤ |s| ≤ 10^4
 Both Uppercase & Lowercase are considerable
'''

'''
User function Template for python3
'''

class Solution:
    
    '''
    Function to check if a string is Pangram or not.
    '''
    
    def checkPangram(self,s):
        
        '''
        Code here
        '''
        
        h = [0 for x in range(26)]
        for char in s:
            char = char.lower()
            if char.isalnum():
                h[ord(char)-97]+=1
        for count in h:
            if  count==0: return False
        return True



