'''
Task:- 
Given a string s and a dictionary of n words dictionary, find out if a s can be segmented into a space-separated sequence of dictionary words. Return 1 if it is possible to break the s into a sequence of dictionary words, else return 0. 
'''

'''
Example 1:- 
Input:
n = 6
s = "ilike"
dictionary = { "i", "like", "sam", "sung", "samsung", "mobile"}
Output:
1
Explanation:
The string can be segmented as "i like".
'''

'''
Example 2:- 
Input:
n = 6
s = "ilikesamsung"
dictionary = { "i", "like", "sam", "sung", "samsung", "mobile"}
Output:
1
Explanation:
The string can be segmented as 
"i like samsung" or "i like sam sung".
'''

'''
Complexity:- 
 Expected Time Complexity: O(len(s)^2)
 Expected Space Complexity: O(len(s))
'''

'''
Constraints:- 
 1 ≤ n ≤ 12
 1 ≤ len(s) ≤ 1100
'''

'''
User function Template for python3
'''

class Solution:
    def wordBreak(self, line, dictionary):
        
        '''
        Complete this function
        '''
        
        from functools import lru_cache
        dictionary = set(dictionary)
        @lru_cache(None)
        def ok(word, i):
            if i >= len(word):
                return True
            for k in range(i, len(word)):
                if word[i:k+1] not in dictionary:
                    continue
                if ok(word, k+1):
                    return True
            return False
        return ok(line, 0)