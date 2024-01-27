'''
Task:- 
Given an array p[] of length n used to denote the dimensions of a series of matrices such that dimension of i'th matrix is p[i] * p[i+1]. There are a total of n-1 matrices. Find the most efficient way to multiply these matrices together. 
The problem is not actually to perform the multiplications, but merely to decide in which order to perform the multiplications such that you need to perform minimum number of multiplications. There are many options to multiply a chain of matrices because matrix multiplication is associative i.e. no matter how one parenthesize the product, the result will be the same. Please see examples for more clarifications.
'''

'''
Example 1:- 
Input: 
n = 5
p[] = {1, 2, 3, 4, 5}
Output: 
True
Explaination: 
The solution returned the string (((AB)C)D), which performs minimum multiplications. The total number of multiplications are (1*2*3) + (1*3*4) + (1*4*5) = 6 + 12 + 20 = 38.
'''

'''
Example 2:- 
Input: 
n = 3
p = {3, 3, 3}
Output: 
True
Explaination: 
The solution returned the string (AB), which performs minimum multiplications. The total number of multiplications are (3*3*3) = 27.
'''

'''
Complexity:- 
 Expected Time Complexity: O(n^3)
 Expected Auxiliary Space: O(n^2)
'''

'''
Constraints:-
 2 ≤ n ≤ 26 
 1 ≤ p[i] ≤ 500 
'''

'''
User function Template for python3
'''

from math import inf
class Solution:
    def matrixChainOrder(self, p, n):
        cost = [[inf for j in range(n)] for i in range(n)]
        bracket = [['' for j in range(n)] for i in range(n)]
        
        for i in range(n-1):
            cost[i][i+1] = 0 
            bracket[i][i+1] = chr(ord('A') + i)
        
        for c in range(2, n):
            for i in range(n-c):
                j = i + c
                for k in range(i+1, j):
                    if cost[i][j] > cost[i][k] + cost[k][j] + p[i] * p[j] * p[k]:
                        cost[i][j] = cost[i][k] + cost[k][j] + p[i] * p[j] * p[k]
                        bracket[i][j] = '(' + bracket[i][k] + bracket[k][j] + ')'

        return bracket[0][n-1]










