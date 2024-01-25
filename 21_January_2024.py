'''
Task:- 
Vertex cover of an undirected graph is a list of vertices such that every vertex not in the vertex cover shares their every edge with the vertices in the vertex cover. In other words, for every edge in the graph, atleast one of the endpoints of the graph should belong to the vertex cover. You will be given an undirected graph G, and your task is to determine the smallest possible size of a vertex cover.
'''

'''
Example 1:- 
Input:
N=5
M=6
edges[][]={{1,2}
           {4, 1},
           {2, 4},
           {3, 4},
           {5, 2},
           {1, 3}}
Output:
3
Explanation:
{2, 3, 4} forms a vertex cover
with the smallest size.
'''

'''
Example 2:- 
Input:
N=2
M=1
edges[][]={{1,2}} 
Output: 
1 
Explanation: 
Include either node 1 or node 2
in the vertex cover.
'''

'''
Complexity:- 
 Expected Time Complexity: O(M*2^N)
 Expected Auxiliary Space: O(N^2)
'''

'''
Constraints:- 
 1 <= N <= 16
 1 <= M <= N*(N-1)/2
 1 <= edges[i][0], edges[i][1] <= N
 '''
 
from typing import List

class Solution:
    def vertexCover(self, n : int, edges : List[List[int]]) -> int:
        def solve(edges):
            if len(edges)==0:
                return 0
            ed0=[]
            ed1=[]
            for i in edges:
                if not(i[0]==edges[0][0] or i[1]==edges[0][0]):
                    ed0.append(i)
                if not(i[0]==edges[0][1] or i[1]==edges[0][1]):
                    ed1.append(i)
            ans0=1+solve(ed0)
            ans1=1+solve(ed1)
            return min(ans0,ans1)
        return solve(edges)