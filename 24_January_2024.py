'''
Task:- 
You are given an undirected graph of N nodes (numbered from 0 to N-1) and M edges. Return 1 if the graph is a tree, else return 0.
'''

'''
Example 1:- 
Input:
N = 4, M = 3
G = [[0, 1], [1, 2], [1, 3]]
Output: 
1
Explanation: 
Every node is reachable and the graph has no loops, so it is a tree
'''

'''
Example 2:- 
Input:
N = 4, M = 3
G = [[0, 1], [1, 2], [2, 0]]
Output: 
0
Explanation: 
3 is not connected to any node and there is a loop 0->1->2->0, so it is not a tree.
'''

'''
Complexity:- 
 Expected Time Complexity: O(N+M)
 Expected Auxiliary Space: O(N)
'''

'''
Constraints:
 1 <= N <= 2*10^5
 0 <= M <= 2*10^5
'''

'''
User function Template for python3
'''

class Solution:
    def isTree(self, n, m, edges):
        parent = list(range(n))
        rank = [0] * n
        
        def find(k):
            if parent[k] != k:
                parent[k] = find(parent[k])
            return parent[k]
        
        def union_if_different(k, l):
            parent_k, parent_l = find(k), find(l)
            if parent_k == parent_l:
                return False
            rank_k, rank_l = rank[parent_k], rank[parent_l]
            if rank_k > rank_l:
                parent[parent_l] = parent_k
            elif rank_l > rank_k:
                parent[parent_k] = parent_l
            else:
                parent[parent_l] = parent_k
                rank[parent_k] += 1
            return True
        
        for u, v in edges:
            if not union_if_different(u, v):
                return 0
        root = find(parent[0])
        return 1 if all(find(p) == root for p in parent) else 0