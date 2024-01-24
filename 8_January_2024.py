'''
Task:- 
Given two linked lists of size N and M, which are sorted in non-decreasing order. The task is to merge them in such a way that the resulting list is in non-increasing order.
'''

'''
Example 1:- 
Input:
N = 2, M = 2
list1 = 1->3
list2 = 2->4
Output:
4->3->2->1
Explanation:
After merging the two lists in non-increasing order, we have new lists as 4->3->2->1.
'''

'''
Example 2:- 
Input:
N = 4, M = 3
list1 = 5->10->15->40 
list2 = 2->3->20
Output:
40->20->15->10->5->3->2
Explanation:
After merging the two lists in non-increasing order, we have new lists as 40->20->15->10->5->3->2.
'''

'''
Complexity:- 
 Expected Time Complexity : O(N+M)
 Expected Auxiliary Space : O(1)
'''

'''
Constraints:- 
 0 <= N, M <= 10^4
'''

'''
User function Template for python3
'''

'''
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
'''

class Solution:
  def mergeResult(self, node1, node2):
    if node1 is None and node2 is None:
        return None
    present = None
    while node1 is not None and node2 is not None:
        if node1.data <= node2.data:
            temp = node1.next
            node1.next = present
            present = node1
            node1 = temp
        else:
            temp = node2.next
            node2.next = present
            present = node2
            node2 = temp
    while node1 is not None:
        temp = node1.next
        node1.next = present
        present = node1
        node1 = temp
    while node2 is not None:
        temp = node2.next
        node2.next = present
        present = node2
        node2 = temp
    return present








