'''
Task:-
Given a string S consisting of the characters 0, 1 and 2. Your task is to find the length of the smallest substring of string S that contains all the three characters 0, 1 and 2. If no such substring exists, then return -1.
'''

'''
Example 1:- 
Input:
S = 10212
Output:
3
Explanation:
The substring 102 is the smallest substring
that contains the characters 0, 1 and 2.
'''

'''
Example 2:- 
Input: 
S = 12121
Output:
-1
Explanation: 
As the character 0 is not present in the
string S, therefor no substring containing
all the three characters 0, 1 and 2
exists. Hence, the answer is -1 in this case.
'''

'''
Complexity:- 
 Expected Time Complexity: O( length( S ) )
 Expected Auxiliary Space: O(1)
'''

'''
Constraints:- 
 1 ≤ length( S ) ≤ 10^5
 All the characters of String S lies in the set {'0', '1', '2'}
'''

'''
User function Template for python3
'''

class Solution:
    def smallestSubstring(self, S):
        
        '''
        Code here
        '''
        
        n = len(S)
        count = [0] * 3
        ans = n + 1
        start = 0
        for i in range(n):
            count[ord(S[i]) - ord('0')] += 1
            while (count[0] > 0 and count[1] > 0 and count[2] > 0):
                ans = min(ans, i - start + 1)
                count[ord(S[start]) - ord('0')] -= 1
                start += 1
        if ans == n + 1:
            return -1
        return ans








