'''
Task:- 
Given an array arr containing N integers and a positive integer K, find the length of the longest sub array with sum of the elements divisible by the given value K.
'''

'''
Example 1:- 
Input:
N = 6, K = 3
arr[] = {2, 7, 6, 1, 4, 5}
Output: 
4
Explanation:
The subarray is {7, 6, 1, 4} with sum 18, which is divisible by 3.
'''

'''
Example 2:- 
Input:
N = 7, K = 3
arr[] = {-2, 2, -5, 12, -11, -1, 7}
Output: 
5
Explanation:
The subarray is {2,-5,12,-11,-1} with sum -3, which is divisible by 3.
'''

'''
Complexity:- 
 Expected Time Complexity: O(N).
 Expected Auxiliary Space: O(N).
'''

'''
Constraints:- 
 1 <= N <= 10^5
 1 <= K <= 10^9
 -10^9 <= A[i] <= 10^9 
'''

'''
User function Template for python3
'''

class Solution:
    def longSubarrWthSumDivByK(self, arr, n, K):
        
'''
Complete the function
'''

        m = {}
        mod_arr = [0] * n
        ans = 0
        sum = 0
        for i in range(n):
            sum += arr[i]
            mod_arr[i] = ((sum % K) + K) % K
        for i in range(n):
            if mod_arr[i] == 0:
                ans = i + 1
            elif mod_arr[i] not in m:
                m[mod_arr[i]] = i
            else:
                if ans < (i - m[mod_arr[i]]):
                    ans = i - m[mod_arr[i]]
        return ans








