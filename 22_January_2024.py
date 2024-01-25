'''
Task:- 
Given a Binary tree and a sum S, print all the paths, starting from root, that sums upto the given sum. Path not necessarily end on a leaf node.
'''

'''
Example 1:- 
Input : 
sum = 8
Input tree
         1
       /   \
     20      3
           /    \
         4       15   
        /  \     /  \
       6    7   8    9      

Output :
1 3 4
Explanation : 
Sum of path 1, 3, 4 = 8.
'''

'''
Example 2:- 
Input : 
sum = 38
Input tree
          10
       /     \
     28       13
           /     \
         14       15
        /   \     /  \
       21   22   23   24
Output :
10 28
10 13 15  
Explanation :
Sum of path 10, 28 = 38 and
Sum of path 10, 13, 15 = 38.
'''

'''
Complexity:- 
 Expected Time Complexity: O(N)
 Expected Space Complexity: O(N2)
'''

'''
Constrains:- 
 1 <= N <= 2*10^3
 -10^3 <= sum, Node.key <= 10^3
'''

'''
User function Template for python3
'''

'''
Tree Node
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
'''

class Solution:
    def printPaths(self, root, S):
        ans = 0
        nodes_list = []
    
        def dfs(node, path):
            nonlocal ans
            nonlocal nodes_list
        
            ans += node.data
            path.append(node.data)
        
            if ans == S:
                nodes_list.append(path[:])
        
            if node.left:
                dfs(node.left, path)
        
            if node.right:
                dfs(node.right, path)
        
            ans -= node.data
            path.pop()
    
        dfs(root, [])
        return nodes_list