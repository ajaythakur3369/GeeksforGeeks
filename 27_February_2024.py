'''
Task:- 
You are given an array arr[] of length n, you have to re-construct the same array arr[] in-place. The arr[i] after reconstruction will become arr[i] OR arr[i+1], where OR is bitwise or. If for some i, i+1 does not exists, then do not change arr[i].
'''

'''
Example 1:- 
Input :
n = 5
arr[] = {10, 11, 1, 2, 3}
Output :
11 11 3 3 3
Explanation:
At index 0, arr[0] or arr[1] = 11
At index 1, arr[1] or arr[2] = 11
At index 2, arr[2] or arr[3] = 3
...
At index 4, No element is left So, it will remain as it is.
New Array will be {11, 11, 3, 3, 3}.
'''

'''
Example 2:- 
Input :
n= 4
arr[] = {5, 9, 2, 6} 
Output :
13 11 6 6
Explanation:
At index 0, arr[0] or arr[1] = 13.
At index 1, arr[1] or arr[2] = 11.
At index 2, arr[2] or arr[3] = 6.
At index 3, No element is left So, it will remain as it is.
New Array will be {13, 11, 6, 6}.
'''

'''
Complexity:- 
 Expected Time Complexity: O(n).
 Expected Auxiliary Space: O(1).
'''

'''
Constraints:- 
 1 ≤ n ≤ 10^5
 1 ≤ arr[i] ≤ 10^7
'''

'''
User function Template for python3
'''

class Solution:
    def game_with_number (self, arr,  n) : 
        
        '''
        Complete the function
        '''
        
        for i in range(n-1):
            arr[i] = arr[i] | arr[i+1]
        return arr