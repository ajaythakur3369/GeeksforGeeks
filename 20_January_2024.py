'''
Task:- 
Given a binary tree with N nodes, in which each node value represents number of candies present at that node. In one move, one may choose two adjacent nodes and move only one candy from one node to another (the move may be from parent to child, or from child to parent.) 
The task is to find the minimum number of moves required such that every node has exactly one candy.
Note that the testcases are framed such that it is always possible to achieve a configuration in which every node has exactly one candy, after some moves.
'''

'''
Example 1:- 
Input :      3
           /   \
          0     0 
Output : 2
Explanation: 
From the root of the tree, we move one 
candy to its left child, and one candy to
its right child.
'''

'''
Example 2:- 
Input :      0
           /   \
          3     0  
Output : 3
Explanation : 
From the left child of the root, we move 
two candies to the root [taking two moves]. 
Then, we move one candy from the root of the 
tree to the right child.
'''

'''
Complexity:- 
 Expected Time Complexity: O(N)
 Expected Auxiliary Space: O(height of the tree)
'''

'''
Constraints:- 
 1 <= N <= 10^4
 0 <= Value of each node <= 10^4
'''

'''
User function Template for python3
'''

'''
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
'''

class Solution:
    def __init__(self):
        
        '''
        Variable to keep track of total moves
        '''
        
        self.total_moves = 0

    def distributeCandy(self, root):
        
        '''
        Helper function to recursively distribute candy
        '''
        
        def distribute_helper(node):
            
            '''
            Base case: If the node is None, return 0
            '''
            
            if not node:
                return 0
           
            '''
            Recursive calls for left and right subtrees
            '''
            
            left_count = distribute_helper(node.left)
            right_count = distribute_helper(node.right)
           
            '''
            Calculate moves for the current node
            '''
            
            self.total_moves += abs(left_count) + abs(right_count)
           
            '''
            Return the total candy count for the current node
            '''
            
            return left_count + node.data + right_count - 1

        '''
        Start the candy distribution process
        '''
        
        distribute_helper(root)
       
        '''
        Return the total moves required
        '''
        
        return self.total_moves




