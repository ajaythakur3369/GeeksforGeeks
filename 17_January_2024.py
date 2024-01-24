'''
Task:- 
Given an array arr[] of length n. Find all possible unique permutations of the array in sorted order. A sequence A is greater than sequence B if there is an index i for which Aj = Bj for all j<i and Ai > Bi.
'''

'''
Example 1:- 
Input: 
n = 3
arr[] = {1, 2, 1}
Output: 
1 1 2
1 2 1
2 1 1
Explanation:
These are the only possible unique permutations
for the given array.
'''

'''
Example 2:- 
Input: 
n = 2
arr[] = {4, 5}
Output: 
Only possible 2 unique permutations are
4 5
5 4
'''

'''
Complexity:- 
Expected Time Complexity:  O(n*n!)
Expected Auxilliary Space: O(n*n!)
'''

'''
Constraints:- 
1 ≤ n ≤ 9
1 ≤ arri ≤ 9
'''

''''
User function Template for python3
'''

class Solution:
    def uniquePerms(self, arr, n):
        
        '''
        Code here 
        '''
        
        from itertools import permutations
        return sorted(set(permutations(arr)))