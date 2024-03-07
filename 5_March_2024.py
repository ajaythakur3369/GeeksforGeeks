'''
Task:- 
Given an array a of n positive integers. The task is to find the maximum of j - i subjected to the constraint of a[i] ≤ a[j] and i ≤ j.
'''

'''
Example 1:- 
Input:
n = 2
a[] = {1, 10}
Output:
1
Explanation:
a[0] ≤ a[1] so (j-i) is 1-0 = 1.
'''

'''
Example 2:- 
Input:
n = 9
a[] = {34, 8, 10, 3, 2, 80, 30, 33, 1}
Output:
6
Explanation:
In the given array a[1] < a[7] satisfying the required condition(a[i] ≤ a[j]) thus giving the maximum difference of j - i which is 6(7-1).
'''

'''
Complexity:- 
 Expected Time Complexity: O(N)
 Expected Auxiliary Space: O(N)
'''

'''
Constraints:- 
 1 ≤ n ≤ 10^6
 0 ≤ a[i] ≤ 10^9
'''

'''
User function Template for python3
'''

class Solution:
    def maxIndexDiff(self, a, n):
        if n <= 1:
            return 0

        left_min = [0] * n
        right_max = [0] * n

        left_min[0] = a[0]
        for i in range(1, n):
            left_min[i] = min(left_min[i - 1], a[i])

        right_max[n - 1] = a[n - 1]
        for i in range(n - 2, -1, -1):
            right_max[i] = max(right_max[i + 1], a[i])

        max_diff = 0
        i = j = 0

        while i < n and j < n:
            if left_min[i] <= right_max[j]:
                max_diff = max(max_diff, j - i)
                j += 1
            else:
                i += 1

        return max_diff