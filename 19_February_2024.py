'''
Task:- 
Given a string s of lowercase alphabets and a number k, the task is to print the minimum value of the string after removal of k characters. The value of a string is defined as the sum of squares of the count of each distinct character present in the string. 
'''

'''
Example 1:- 
Input: 
s = abccc, k = 1
Output: 
6
Explaination:
We remove c to get the value as 1^2 + 1^2 + 2^2
'''

'''
Example 2:- 
Input: 
s = aabcbcbcabcc, k = 3
Output: 
27
Explaination: 
We remove two 'c' and one 'b'. Now we get the value as 3^2 + 3^2 + 3^2.
'''

'''
Expected Time Complexity:- 
 O(n+klog(p)) where n is the length of string and p is number of distinct alphabets and k number of alphabets to be removed. 
'''

'''
Expected Auxiliary Space:- 
 O(n)
'''

'''
Constraints:-
 0 ≤ k ≤ |string length| ≤ 10^5
'''

'''
User function Template for python3
'''

from collections import Counter
from heapq import heappop, heappush, heapify

class Solution:
    def minValue(self, s, k):
        
        '''
        Code here
        '''
        
        C = [-num for num in Counter(s).values()]
        heapify(C)
        while k:
            val = -heappop(C)
            val -= 1
            heappush(C, -val)
            k -= 1
            
        return sum(num ** 2 for num in C)