'''
Task:- 
Given a string s of length n, find the longest repeating non-overlapping substring in it. In other words find 2 identical substrings of maximum length which do not overlap. Return the longest non-overlapping substring. Return "-1" if no such string exists.
'''

'''
Example 1:- 
Input:
n = 9
s = "acdcdacdc"
Output:
"acdc"
Explanation:
The string "acdc" is the longest Substring of s which is repeating but not overlapping.
'''

'''
Example 2:- 
Input:
n = 7
s = "heheheh"
Output:
"heh"
Explanation:
The string "heh" is the longest Substring of s which is repeating but not overlapping.
'''

'''
Complexity:- 
 Expected Time Complexity: O(n^2)
 Expected Auxiliary Space: O(n^2)
'''

'''
Constraints:- 
 1 <= n <= 10^3
'''

'''
User function Template for python3
'''

class Solution: 
    @staticmethod 
    def longestSubstring(S, N): 
        max_len = 0 
        ans = "-1" 
        i = 0 
        j = 0

        while i < N and j < N:
            sub_string = S[i:j+1]
            if S.find(sub_string, j+1) != -1:
                length = len(sub_string)
                if length > max_len:
                    ans = sub_string
            else:
                i += 1
            j += 1
        
        return ans