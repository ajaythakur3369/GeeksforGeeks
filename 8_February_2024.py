'''
Task:- 
Given a binary tree with n nodes, determine whether all the leaf nodes are at the same level or not. Return true if all leaf nodes are at the same level, and false otherwise.
'''

'''
Example 1:- 
Input:
Tree:
    1
   / \
  2   3
Output:
true
Explanation:
The binary tree has a height of 2 and the leaves are at the same level.
'''

'''
Example 2:- 
Input:
Tree:
    10
   /  \
 20   30
 /  \
 10   15
Output:
false
Explanation:
The binary tree has a height of 3 and the leaves are not at the same level.
'''

'''
Complexity:- 
 Expected Time Complexity: O(n)
 Expected Auxiliary Space: O(height of tree)
'''

'''
Constraints:- 
 1 ≤ n ≤ 10^5 
'''

'''
User function Template for python3
'''

class Solution:
    
    '''
    Your task is to complete this function
    function should return True/False or 1/0
    '''
    
    def check(self, root):
        
        '''
        Code here
        '''
        
        def dfs(node, level):
            if not node: return True
            if not node.left and not node.right: levels.add(level)
            if len(levels) > 1: return False
            
            return dfs(node.left, level + 1) and dfs(node.right, level + 1)
            
        levels = set()
        
        return dfs(root, 0)