'''
Task:- 
Given an array arr of size n, the task is to check if the given array can be a level order representation of a Max Heap.
'''

'''
Example 1:- 
Input:
n = 6
arr[] = {90, 15, 10, 7, 12, 2}
Output: 
1
Explanation: 
The given array represents below tree
       90
     /    \
   15      10
  /  \     /
7    12  2
The tree follows max-heap property as every
node is greater than all of its descendants.
'''

'''
Example 2:- 
Input:  
n = 6
arr[] = {9, 15, 10, 7, 12, 11}
Output:
0
Explanation:
The given array represents below tree
       9
     /    \
   15      10
  /  \     /
7    12  11
The tree doesn't follows max-heap property 9 is
smaller than 15 and 10, and 10 is smaller than 11. 
'''

'''
Complexity:- 
 Expected Time Complexity: O(n)
 Expected Auxiliary Space: O(1)
'''

'''
Constraints:- 
 1 ≤ n ≤ 10^5
 1 ≤ arri ≤ 10^5
'''

class Solution:
    def isMaxHeap(self,arr,n):
        
        '''
        Your code goes here
        '''
        
        q = [0]
        while q:
            i = q.pop()
            k1, k2 = 2*i+1, 2*i+2
            if k1 < n:
                if arr[k1] > arr[i]:
                    return False
                q.append(k1)
            if k2 < n:
                if arr[k2] > arr[i]:
                    return False
                q.append(k2)
        return True