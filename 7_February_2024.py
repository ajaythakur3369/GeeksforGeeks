'''
Task:- 
Given a binary tree with n nodes and two node values, a and b, your task is to find the minimum distance between them. The given two nodes are guaranteed to be in the binary tree and all node values are unique.
'''

'''
Example 1:- 
Input:
        1
      /  \
     2    3
a = 2, b = 3
Output: 
2
Explanation: 
We need the distance between 2 and 3. Being at node 2, we need to take two steps ahead in order to reach node 3. The path followed will be: 2 -> 1 -> 3. Hence, the result is 2.
'''

'''
Example 2:- 
Input:
        11
      /   \
     22  33
    /  \  /  \
  44 55 66 77
a = 77, b = 22
Output: 
3
Explanation: 
We need the distance between 77 and 22. Being at node 77, we need to take three steps ahead in order to reach node 22. The path followed will be: 77 -> 33 -> 11 -> 22. Hence, the result is 3.
'''

'''
Complexity:- 
 Expected Time Complexity: O(n).
 Expected Auxiliary Space: O(Height of the Tree).
'''

'''
Constraints:- 
 2 <= n <= 10^5
 0 <= Data of a node <= 10^9
'''

'''
User function Template for python3
'''

'''
 Node Class:
class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    dist=0
    def lca(self,root,n1,n2):
        if root==None or root.data==n1 or root.data==n2:
            return root
        ln=self.lca(root.left,n1,n2)
        rn=self.lca(root.right,n1,n2)
        if rn==None:
            return ln
        if ln==None:
            return rn
        return root
    def find_dis(self,root,n,level):
        if not root:
            return 0
        if root.data==n:
            self.dist=self.dist+level
            return level
        self.find_dis(root.left,n,level+1)
        self.find_dis(root.right,n,level+1)
    def findDist(self,root,a,b):
        lca_root=self.lca(root,a,b)
        self.find_dis(lca_root,a,0)
        self.find_dis(lca_root,b,0)
        return self.dist