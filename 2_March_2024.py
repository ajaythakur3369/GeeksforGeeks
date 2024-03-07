'''
Task:- 
Given an array of n integers. Find the first element that occurs atleast k number of times. If no such element exists in the array, then expect the answer to be -1.
'''

'''
Example 1:- 
Input :
n = 7, k = 2
a[] = {1, 7, 4, 3, 4, 8, 7}
Output :
4
Explanation :
Both 7 and 4 occur 2 times. But 4 is first that occurs twice.
As at index = 4, 4 has occurred twice whereas 7 appeared twice
at index 6.
'''

'''
Example 2:-
Input :
n = 10, k = 3
a[] = {3, 1, 3, 4, 5, 1, 3, 3, 5, 4}
Output :
3
Explanation :
Here, 3 is the only number that appeared atleast 3 times in the array.
'''

'''
Complexity:- 
 Expected Time Complexity: O(n).
 Expected Auxiliary Space: O(n).
'''

'''
Constraints:- 
 1 <= n <= 10^4
 1 <= k <= 100
 0 <= a[i] <= 200
'''

'''
User function Template for python3
'''

class Solution:
    def firstElementKTime(self, n, k, a):
        
        '''
        Code here
        '''
        
        d={}
        x=1
        for i in a:
            if i not in d.keys():
                d[i]=x
            else:
                d[i]+=1
            if d[i]==k:
                return i
        else :
            return -1