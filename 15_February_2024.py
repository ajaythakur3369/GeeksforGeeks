'''
Task:- 
You are presented with an undirected connected graph consisting of n vertices and connections between them represented by an adjacency matrix. Your objective is to determine whether it is possible to start traversing from a node, x, and return to it after traversing all the vertices at least once, using each edge exactly once.
'''

'''
Example 1:- 
Input: 
paths = 0 1 1 1 1
        1 0 0 1 0
        1 0 0 1 0
        1 1 1 0 1
        1 0 0 1 0
        
Output: 1
Explanation: 
One can visit the vertices in the following way:
1->3->4->5->1->4->2->1 (assuming 1-based indexing)
Here all the vertices has been visited and all
paths are used exactly once.
'''

'''
Example 2:- 
Input: 
paths = 0 1 1 0
        1 0 1 1
        1 1 0 0
        0 1 0 0
Output: 0
Explanation: 
There exists no such vertex from which all the 
vertices could be visited and all edges are used 
exactly once.
'''

'''
Complexity:- 
 Expected Time Complexity: O(n^2)
 Expected Space Compelxity: O(1)
'''

'''
Constraints:- 
 1 <= n <= 100
 0 <= paths[i][j] <= 1
'''

'''
User function Template for python3
'''

class Solution:
    def isPossible(self, paths):
        
        '''
        Code here
        '''
        
        return int(all(sum(r)%2 == 0 for r in paths))