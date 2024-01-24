'''
Task:- 
Given two strings, one is a text string, txt and other is a pattern string, pat. The task is to print the indexes of all the occurences of pattern string in the text string. Use one-based indexing while returning the indices. 
Note: Return an empty list incase of no occurences of pattern. Driver will print -1 in this case.
'''

'''
Example 1:- 
Input:
txt = "geeksforgeeks"
pat = "geek"
Output: 
1 9
Explanation: 
The string "geek" occurs twice in txt, one starts are index 1 and the other at index 9. 
'''

'''
Example 2:- 
Input: 
txt = "abesdu"
pat = "edu"
Output: 
-1
Explanation: 
There's not substring "edu" present in txt.
'''

'''
Complexity:- 
 Expected Time Complexity: O(|txt|).
 Expected Auxiliary Space: O(|txt|).
'''

'''
Constraints:-
 1 ≤ |txt| ≤ 10^6
 1 ≤ |pat| < |S|
Both the strings consists of lowercase English alphabets.
'''

'''
User function Template for python3
'''

class Solution:
    def search(self, pat, txt):
        M = len(pat)
        N = len(txt)
        lps = [0]*M
        j = 0
        self.computeLPSArray(pat, M, lps)
        i = 0
        res = []
        while i < N:
            if pat[j] == txt[i]:
                i += 1
                j += 1
            if j == M:
                res.append(i-j+1)
                j = lps[j-1]
            elif i < N and pat[j] != txt[i]:
                if j != 0:
                    j = lps[j-1]
                else:
                    i += 1
        return res

    def computeLPSArray(self, pat, M, lps):
        len = 0
        lps[0] = 0
        i = 1
        while i < M:
            if pat[i] == pat[len]:
                len += 1
                lps[i] = len
                i += 1
            else:
                if len != 0:
                    len = lps[len-1]
                else:
                    lps[i] = 0
                    i += 1