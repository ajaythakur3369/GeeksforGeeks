'''
Task:- 
Given a singly linked list of length n. The link list represents a binary number, ie- it contains only 0s and 1s. Find its decimal equivalent.
The significance of the bits decreases with the increasing index in the linked list.
An empty linked list is considered to represent the decimal value 0. 

Since the answer can be very large, answer modulo 10^9+7 should be printed.
'''

'''
Example 1:- 
Input:
n = 3
Linked List = {0, 1, 1}
Output:
3
Explanation:
0*2^2 + 1*2^1 + 1*2^0 =  1 + 2 + 0 = 3
'''

'''
Example 2:- 
Input:
n = 4
Linked List = {1, 1, 1, 0}
Output:
14
Explanation:
1*2^3 + 1*2^2 + 1*2^1 + 0*2^0 =  8 + 4 + 2 + 0 = 14
'''

'''
Complexity:- 
 Expected Time Complexity: O(n)
 Expected Auxiliary Space: O(1)
'''

'''
Constraints:- 
 0 <= n <= 100
 Data of each node is either 0 or 1
'''

'''
class node:
    def __init__(self):
        self.data = None
        self.next = None
'''

class Solution:
    def decimalValue(self, head):
        MOD=10**9+7
        
        '''
        Code here
        '''
        
        c = 0
        node = head
        if not node:
            return 0
        while node:
            c+=1
            node = node.next
        
        ans = 0
        while head:
            
           
            ans = ans +( (head.data)*(2**(c-1)))
            head = head.next
            c-=1
        return ans%MOD