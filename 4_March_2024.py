'''
Task:- 
Given an array arr of n positive integers. The task is to swap every ith element of the array with (i+2)th element.
'''

'''
Example 1:- 
Input:
n = 3
arr[] = 1 2 3
Output:
3 2 1
Explanation:
Swapping 1 and 3, makes the array 3 2 1. There is only one swap possible in this array.
'''

'''
Example 2:- 
Input:
n = 5
arr[] = 1 2 3 4 5
Output:
3 4 5 2 1
Explanation:
Swapping 1 and 3, makes the array 3 2 1 4 5.
Now, swapping 2 and 4, makes the array 3 4 1 2 5. 
Again,swapping 1 and 5, makes the array 3 4 5 2 1.
'''

'''
Complexity:- 
 Expected Time Complexity: O(n)
 Expected Auxilary Space: O(1)
'''

'''
Constraints:- 
 1 <= n <= 10^6
 0 <= arri <= 10^9
'''

'''
User function Template for python3
'''

class Solution:
    def swapElements(self, arr, n):
        
        '''
        Code here
        '''
        
        for i in range(0,n-2):
            temp = arr[i]
            arr[i] = arr[i+2]
            arr[i+2] = temp