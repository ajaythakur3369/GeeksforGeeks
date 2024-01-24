'''
Task:- 
Given a boolean matrix of size RxC where each cell contains either 0 or 1, find the row numbers (0-based) of row which already exists or are repeated.
'''

'''
Example 1:- 
Input:
R = 2, C = 2
matrix[][] = {{1, 0},
            {1, 0}}
Output: 
1
Explanation:
Row 1 is duplicate of Row 0.
'''

'''
Example 2:- 
Input:
R = 4, C = 3
matrix[][] = {{ 1, 0, 0},
            { 1, 0, 0},
            { 0, 0, 0},
            { 0, 0, 0}}
Output: 
1 3 
Explanation:
Row 1 and Row 3 are duplicates of Row 0 and 2 respectively. 
'''

'''
Complexity:- 
 Expected Time Complexity: O(R * C)
 Expected Auxiliary Space: O(R * C)
'''

'''
Constraints:- 
1 ≤ R, C ≤ 10^3
0 ≤ matrix[i][j] ≤ 1
'''

'''
User function Template for python3
'''

class Solution:
    def repeatedRows(self, arr, m, n):
        seen_rows = set()
        duplicate_rows = []

        for i in range(m):
            row_hash = tuple(arr[i])

            if row_hash in seen_rows:
                duplicate_rows.append(i)
            else:
                seen_rows.add(row_hash)

        return duplicate_rows

'''
Example usage:
'''

if __name__ == "__main__":
    sol = Solution()







