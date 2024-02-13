'''
Task:- 
Given a binary tree having n nodes. Check whether all of its nodes have the value equal to the sum of their child nodes. Return 1 if all the nodes in the tree satisfy the given properties, else it return 0.

For every node, data value must be equal to the sum of data values in left and right children. Consider data value as 0 for NULL child.  Also, leaves are considered to follow the property.
'''

'''
Example 1:- 
Input:
Binary tree
       35
      /   \
     20  15
    /  \  /  \
   15 5 10 5
Output: 
1
Explanation: 
Here, every node is sum of its left and right child.
'''

'''
Example 2:- 
Input:
Binary tree
       1
     /   \
    4    3
   /  
  5    
Output: 
0
Explanation: 
Here, 1 is the root node and 4, 3 are its child nodes. 4 + 3 = 7 which is not equal to the value of root node. Hence, this tree does not satisfy the given condition.
'''

'''
Complexity:- 
 Expected Time Complexiy: O(n).
 Expected Auxiliary Space: O(Height of the Tree).
'''

'''
Constraints:- 
 1 <= n <= 10^5
 1 <= Data on nodes <= 10^5
'''

'''
User function Template for python3
'''

'''
 Node Class:
class Node:
    def init(self,val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    
    '''
    Function to check whether all nodes of a tree have the value 
    equal to the sum of their child nodes.
    '''
    
    def isSumProperty(self, root):
        
        '''
        Code here
        '''
        
        def dfs(node=root):
            if not node:
                return 0,True
            left=dfs(node.left)
            right=dfs(node.right)
            return node.data,(True if not node.left and not node.right else node.data==left[0]+right[0]) and left[1] and right[1]
        return 1 if dfs()[1] else 0