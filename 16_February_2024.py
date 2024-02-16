'''
Task:- 
You are given a Binary Search Tree (BST) with n nodes, each node has a distinct value assigned to it. The goal is to flatten the tree such that, the left child of each element points to nothing (NULL), and the right child points to the next element in the sorted list of elements of the BST (look at the examples for clarity). You must accomplish this without using any extra storage, except for recursive calls, which are allowed.
'''

'''
Example 1:- 
Input:
          5
        /    \
       3      7
      /  \    /   \
     2   4  6     8

Output: 2 3 4 5 6 7 8
Explanation: 
After flattening, the tree looks
like this
    2
     \
      3
       \
        4
         \
          5
           \
            6
             \
              7
               \
                8
Here, left of each node points
'''

'''
Example 2:-
Input:
       5
        \
         8
       /   \
      7     9  

Output: 5 7 8 9
Explanation:
After flattening, the tree looks like this:
   5
    \
     7
      \
       8
        \
         9
'''

'''
Complexity:- 
 Expected Time Complexity: O(N)
 Expected Auxiliary Space: O(N)
'''

'''
Constraints:- 
 1 <= Number of nodes <= 10^3
 1 <= Data of a node <= 10^5
'''

'''
User function Template for python3
'''

'''
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    def flattenBST(self, root):
        
        '''
        Code here
        '''
        
        import sys
        sys.setrecursionlimit(10**6)
        head = Node(0)
        
        def walk(node, head):
            if not node:
                return head
            left, right = node.left, node.right
            node.left = node.right = None
            walk(left, head).right = node
            return walk(right, node)
        
        walk(root, head)
        return head.right