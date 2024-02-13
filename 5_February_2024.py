'''
Task:- 
Given a sorted circular linked list of length n, the task is to insert a new node in this circular list so that it remains a sorted circular linked list.
'''

'''
Example 1:- 
Input:
n = 3
LinkedList = 1->2->4
(the first and last node is connected, i.e. 4 --> 1)
data = 2
Output: 
1 2 2 4
Explanation:
We can add 2 after the second node.
'''

'''
Example 2:- 
Input:
n = 4
LinkedList = 1->4->7->9
(the first and last node is connected, i.e. 9 --> 1)
data = 5
Output: 
1 4 5 7 9
Explanation:
We can add 5 after the second node.
'''

'''
Complexity:- 
 Expected Time Complexity: O(n)
 Expected Auxiliary Space: O(1)
'''

'''
Constraints:- 
 0 <= n <= 10^5
'''

'''
User function Template for python3
'''

'''
class Node: 
    Constructor to initialize the node object 
    def __init__(self, data): 
        self.data = data 
        self.next = None
'''
 
class Solution:
    def sortedInsert(self, head, data):
        
        '''
        Code here
        '''
        
        if head==None:
            node = Node(data)
            node.next = node
            return node
            
        if head.data > data:
            node = Node(head.data)
            node.next = head.next
            head.data = data
            head.next = node
            return head
        
        h = head
        while True:
            if h.next.data > data or h.next==head:
                node = Node(data)
                node.next = h.next
                h.next = node
                break
            h = h.next
        return head