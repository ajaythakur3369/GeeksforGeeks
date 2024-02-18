'''
Task:- 
Given a Binary Search Tree with n nodes, find the sum of all leaf nodes. BST has the following property (duplicate nodes are possible):

 The left subtree of a node contains only nodes with keys less than the node’s key.
 The right subtree of a node contains only nodes with keys greater than or equal to the node’s key.
Your task is to determine the total sum of the values of the leaf nodes.
'''

'''
Example 1:- 
Input:
n = 6
arr = {67, 34, 82, 12, 45, 78}
Output:
135
Explanation:
In first test case, the BST for the given input will be-
                67
             /     \
           34       82
          /   \    /
         12   45  78

Hence, the required sum= 12 + 45 + 78 = 135
'''

'''
Example 2:- 
Input:
n = 1
arr = {45}
Output:
45
Explanation:
As the root node is a leaf node itself, 
the required sum will be 45
'''

'''
Complexity:- 
 Expected Time Complexity: O(n)
 Expected Auxiliary Space: O(1)
'''

'''
Constraints:- 
 1 <= n <= 10^4
 1 <= Value of each node <= 10^5
'''

'''
User function Template for python3
 Structure of node
'''

'''
class Node:
    def __init__(self, data=0):
        self.data=0
        self.left=None
        self.right=None
'''

class Solution:
    def sumOfLeafNodes(self, root):
        
        '''
        Your code here
        '''
        
        if not root:
            return 0
        elif not root.right and not root.left:
            return root.data
        return self.sumOfLeafNodes(root.left)+self.sumOfLeafNodes(root.right)