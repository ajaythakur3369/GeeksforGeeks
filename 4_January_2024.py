'''
Task:- 
Given an array of integers arr[] of length N, every element appears thrice except for one which occurs once.
Find that element which occurs once.
'''

'''
Example 1:- 
Input:
N = 4
arr[] = {1, 10, 1, 1}
Output:
10
Explanation:
10 occurs once in the array while the other
element 1 occurs thrice.
'''

'''
Example 2:- 
Input:
N = 10
arr[] = {3, 2, 1, 34, 34, 1, 2, 34, 2, 1}
Output:
3
Explanation:
All elements except 3 occurs thrice in the array.
'''

'''
Complexity:- 
 Expected Time Complexity: O(N).
 Expected Auxiliary Space: O(1).
'''

'''
Constraints:- 
 1 ≤ N ≤ 10^5
 -10^9 ≤ A[i] ≤ 10^9
'''

'''
User function Template for python3
'''

class Solution:
    def singleElement(self, arr, N):
        ones = 0
        twos = 0
        for i in range(N):
            
            '''
            The expression "ones & arr[i]" gives the bits that are there in both 'ones' and new element from arr[]. We add these bits to 'twos' using bitwise OR
            '''
            
            twos = twos | (ones & arr[i])
            
            '''
            XOR the new bits with previous 'ones' to get all bits appearing odd number of times
            '''
            
            ones = ones ^ arr[i]
            
            '''
            The common bits are those bits which appear third time. So these bits should not be there in both 'ones' and 'twos'. common_bit_mask contains all these bits as 0, so that the bits can be removed from 'ones' and 'twos'
            '''
            
            common_bit_mask = ~(ones & twos)
            ones &= common_bit_mask
            twos &= common_bit_mask
        return ones















