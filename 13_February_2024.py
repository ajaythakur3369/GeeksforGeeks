'''
Task:- 
Given a connected undirected graph with n nodes and m edges, with each node having a distinct label from 0 to n-1, create a clone of the graph. Each node in the graph contains an integer val and an array (neighbors) of nodes, containing nodes that are adjacent to the current node.
'''

'''
Example 1:- 
Input:
adjList = 
{
    {1, 3},
    {0, 2},
    {1, 3},
    {0, 2}
}
Output: 1
Explanation:
1 is the output that the driver code will print in case 
you successfully cloned the given graph.
'''

'''
Example 2:- 
Input:
adjList = 
{
    {1},
    {0}
}
Output: 1
Explanation: 
1 is the output that the driver code will print in case
you successfully cloned the given graph.
'''

'''
Complexity:- 
 Expected Time Complexity: O(n + m).
 Expected Auxiliary Space: O(n).
'''

'''
Constraints:- 
 1 <= n, m <= 10^4
 1 <= Node value <= n
'''

'''
User function Template for python3
'''

'''
class Node:
    def __init__(self, val = 0, neighbors = []):
        self.val = val
        self.neighbors = neighbors
'''

class Solution():
    def cloneGraph(self, node):
        
        '''
        Your code goes here
        Fix for judge's code doing to many recursion calls
        '''
        
        import sys
        sys.setrecursionlimit(10**4)
        
        '''
        End of fix
        '''
        
        '''
        N leeks from the judge's code
        N = 10**4
        '''
        
        nodes = [Node(i, []) for i in range(N)]
        visited = [False] * N
        s = [node]
        while s:
            u = s.pop()
            if visited[u.val]:
                continue
            visited[u.val] = True
            copy_u = nodes[u.val]
            for v in u.neighbors:
                copy_u.neighbors.append(nodes[v.val])
                if not visited[v.val]:
                    s.append(v)
        return nodes[node.val]