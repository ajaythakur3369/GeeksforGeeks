'''
Task:- 
Given an array arr[] of N elements and a number K., split the given array into K subarrays such that the maximum subarray sum achievable out of K subarrays formed is minimum possible. Find that possible subarray sum.
'''

'''
Example 1:- 
Input:
N = 4, K = 3
arr[] = {1, 2, 3, 4}
Output: 4
Explanation:
Optimal Split is {1, 2}, {3}, {4}.
Maximum sum of all subarrays is 4,
which is minimum possible for 3 splits. 
'''

'''
Example 2:- 
Input:
N = 3, K = 2
A[] = {1, 1, 2}
Output:
2
Explanation:
Splitting the array as {1,1} and {2} is optimal.
This results in a maximum sum subarray of 2.
'''

'''
Complexity:- 
 Expected Time Complexity: O(N*log(sum(arr))).
 Expected Auxiliary Space: O(1).
'''

'''
Constraints:- 
 1 ≤ N ≤ 10^5
 1 ≤ K ≤ N
 1 ≤ arr[i] ≤ 10^4
'''

'''
User function Template for python3
'''

class Solution:
    def splitArray(self, arr, N, K):
        def is_valid(arr, N, K, mid):
            count = 1
            sum = 0
            for i in range(N):
                sum += arr[i]
                if sum > mid:
                    count += 1
                    sum = arr[i]
                if count > K:
                    return False
            return True
        
        left = max(arr)
        right = sum(arr)
        while left < right:
            mid = (left + right) // 2
            if is_valid(arr, N, K, mid):
                right = mid
            else:
                left = mid + 1
        return left






