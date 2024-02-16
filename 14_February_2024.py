'''
Task:- 
A critical connection refers to an edge that, upon removal, will make it impossible for certain nodes to reach each other through any path. You are given an undirected connected graph with v vertices and e edges and each vertex distinct and ranges from 0 to v-1, and you have to find all critical connections in the graph. It is ensured that there is at least one such edge present.
'''

'''
Example 1:- 
Output:
0 1
0 2
Explanation:
On removing edge (0, 1), you will not be able to
reach node 0 and 2 from node 1. Also, on removing
edge (0, 2), you will not be able to reach node 0
and 1 from node 2.
'''

'''
Example 2:-
Output:
2 3
Explanation:
The edge between nodes 2 and 3 is the only
Critical connection in the given graph.
'''

'''
Complexity:- 
 Expected Time Complexity: O(v + e)
 Expected Auxiliary Space: O(v)
'''

'''
Constraints:- 
 1 ≤ v, e ≤ 10^4
'''

'''
User function Template for python3
'''

class Solution:
    def criticalConnections(self, v, adj):
        
        '''
        Code here
        '''
        
        disc = [-1 for i in range(V)]
        low = [-1 for i in range(V)]
        self.time = 0
        bridges = []

        def SCC(u, par = -1):
            disc[u] = self.time
            low[u] = self.time
            self.time += 1

            for v in adj[u]:
                if v == par:
                    continue
                if disc[v] == -1:
                    SCC(v, u)
                    low[u] = min(low[u], low[v])
                    if low[v] > disc[u]:
                        if v > u:
                            bridges.append([u, v])
                        else:
                            bridges.append([v, u])
                else:
                    low[u] = min(low[u], disc[v])

        for i in range(V):
            if disc[i] == -1:
                SCC(i)
        bridges.sort()
        return bridges
