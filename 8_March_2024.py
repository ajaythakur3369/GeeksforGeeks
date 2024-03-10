'''
Task:- 
Given a string s which contains only lower alphabetic characters, check if it is possible to remove at most one character from this string in such a way that frequency of each distinct character becomes same in the string. Return true if it is possible to do else return false.
'''

'''
Example 1:-
Input:
s = "xyyz"
Output: 
1 
Explanation: 
Removing one 'y' will make frequency of each character to be 1.
'''

'''
Example 2:- 
Input:
s = "xxxxyyzz"
Output: 
0
Explanation: 
Frequency can not be made same by removing at most one character.
'''

'''
Complexity:- 
 Expected Time Complexity: O(|s|) 
 Expected Auxiliary Space: O(1)
'''

'''
Constraints:- 
 1 <= |s| <= 10^5
'''

'''
User function Template for python3
'''

class Solution:
    def sameFreq(self, s):
        
        '''
        Code here
        '''
        
        freq = {}
        for char in s:
            if char in freq:
                freq[char]+=1
            else:
                freq[char]=1
        freq_list = list(set(freq.values()))
        return (len(freq_list)==2 and max(freq_list)-min(freq_list)==1 and list(freq.values()).count(max(freq_list))==1) or len(freq_list)==1