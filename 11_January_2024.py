'''
Task:- 
Given a non-negative integer S represented as a string, remove K digits from the number so that the new number is the smallest possible.
'''

'''
Example 1:- 
Input:
S = "149811", K = 3
Output: 
111
Explanation: 
Remove the three digits 
4, 9, and 8 to form the new number 111
which is smallest.
'''

'''
Example 2:- 
Input:
S = "1002991", K = 3
Output: 
21
Explanation: 
Remove the three digits 1(leading
one), 9, and 9 to form the new number 21(Note
that the output must not contain leading
zeroes) which is the smallest.
'''

'''
Complexity:- 
 Expected Time Complexity: O(|S|).
 Expected Auxiliary Space: O(|S|).
'''

'''
Constraints:
 1<= K <= |S|<=10^6
'''

'''
User function Template for python3
'''

class Solution:
  def removeKdigits(self, S, K):

'''
Code here
'''

    n = len(S)
    if n == K:
        return "0"
    store = []
    for i in range(n):
        while K and store and store[-1] > S[i]:
            store.pop()
            K -= 1
        store.append(S[i])
    while K:
        store.pop()
        K -= 1
    ans = ""
    while store:
        ans += store.pop()
    ans = ans[::-1]
    for i in range(len(ans)):
        if ans[i] != '0':
            return ans[i:]
    return "0"






