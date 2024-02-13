'''
Task:- 
Given a binary tree with n nodes and a non-negative integer k, the task is to count the number of special nodes.
A node is considered special if there exists at least one leaf in its subtree such that the distance between the node and leaf is exactly k.
'''

'''
Example 1:- 
Input:
Binary tree
        1
      /   \
     2     3
   /  \   /  \
  4   5  6    7
          \ 
          8
k = 2
Output: 
2
Explanation: 
There are only two unique nodes that are at a distance of 2 units from the leaf node. (node 3 for leaf with value 8 and node 1 for leaves with values 4, 5 and 7) Note that node 2 isn't considered for leaf with value 8 because it isn't a direct ancestor of node 8.
'''

'''
Example 2:- 
Input:
Binary tree
          1
         /
        3
       /
      5
    /  \
   7    8
         \
          9
k = 4
Output: 
1
Explanation: 
Only one node is there which is at a distance of 4 units from the leaf node.(node 1 for leaf with value 9) 
'''

'''
Complexity:- 
 Expected Time Complexity: O(n).
 Expected Auxiliary Space: O(Height of the Tree).
'''

'''
Constraints:- 
 1 <= n <= 10^5
'''

'''
User function Template for python3
'''

'''
@input - 
node - root node of given tree
k = distance of nodes required 

class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
'''

from collections import deque
class Solution:
    
    '''
    Function to return count of nodes at a given distance from leaf nodes.
    '''
    
    def printKDistantfromLeaf(self, root, k):
        
        '''
        Code here
        '''
        
        queue = deque([(root, [])])
        leafpaths = []

        while queue:
            node, path = queue.popleft()
            
            if node.left:
                queue.append((node.left, path + [node]))

            if node.right:
                queue.append((node.right, path + [node]))

            if not node.left and not node.right:
                leafpaths.append((path + [node]))

        res = set() 

        for path in leafpaths:
            
            '''
            Check if the length of the path is greater than or equal to k + 1
            (k + 1 because the path includes the leaf node itself)
            '''
            
            if len(path) >= k + 1:
                
                '''
                Add the node at a distance of k from the leaf to the 'res' set
                '''
                
                res.add(path[-k - 1])
        return len(res)