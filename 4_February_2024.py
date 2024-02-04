'''
Task:- 
You are given two linked lists that represent two large positive numbers. From the two numbers represented by the linked lists, subtract the smaller number from the larger one. Look at the examples to get a better understanding of the task.
'''

'''
Example 1:- 
Input:
L1 = 1->0->0
L2 = 1->2
Output: 88
Explanation:  
First linked list represents 100 and the
second one represents 12. 12 subtracted from 100
gives us 88 as the result. It is represented
as 8->8 in the linked list.
'''

'''
Example 2:- 
Input:
L1 = 0->0->6->3
L2 = 7->1->0
Output: 647
Explanation: 
First linked list represents 0063 => 63 and 
the second one represents 710. 63 subtracted 
from 710 gives us 647 as the result. It is
represented as 6->4->7 in the linked list.
'''

'''
Complexity:- 
 n and m are the length of the two linked lists respectively.
 Expected Time Complexity:  O(n+m)
 Expected Auxiliary Space: O(n+m)
'''

'''
Constrains:- 
 1 <= n <= 10000
 0 <= values represented by the linked lists < 10^n
 0 <= values represented by the linked lists < 10^m
'''

'''
User function Template for python3
'''

class Solution:
    def subLinkedList(self, l1, l2): 
        
        '''
        Code here
        return head of difference list
        '''
        
        def to_num(l):
            r = 0
            while l:
                r = r*10 + l.data
                l = l.next
            return r
            
        n1 = to_num(l1)
        n2 = to_num(l2)

        s = str(n1-n2) if n1 > n2 else str(n2-n1)
        
        dummy = Node(-1)
        w = dummy
        for e in s:
            n = ord(e)-ord('0')
            w.next = Node(n)
            w = w.next
            
        return dummy.next