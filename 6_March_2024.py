'''
Task:- 
Given two strings, one is a text string and other is a pattern string. The task is to print the indexes of all the occurences of pattern string in the text string. For printing, Starting Index of a string should be taken as 1. The strings will only contain lowercase English alphabets ('a' to 'z').
'''

'''
Example 1:- 
Input: 
text = "birthdayboy"
pattern = "birth"
Output: 
[1]
Explanation: 
The string "birth" occurs at index 1 in text.
'''

'''
Example 2:-
Input:
text = "geeksforgeeks"
pattern = "geek"
Output: 
[1, 9]
Explanation: 
The string "geek" occurs twice in text, one starts are index 1 and the other at index 9.
'''

'''
Complexity:- 
 Expected Time Complexity: O(|text| + |pattern|).
 Expected Auxiliary Space: O(1).
'''

'''
Constraints:- 
 1<=|text|<=5*10^5
 1<=|pattern|<=|text|
'''

'''
User function Template for python
'''

class Solution:
    def search(self, pattern, text):
        
        '''
        Code here
        '''
        
        l=[]
        for i in range(len(text)-len(pattern)+1):
            if(text[i:i+len(pattern)])==pattern:
                l.append(i+1)
        return l