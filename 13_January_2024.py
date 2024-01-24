'''
Task:- 
Given a singly linked list, sort the list (in ascending order) using insertion sort algorithm.
'''

'''
Example 1:- 
Input:
N = 10
Linked List = 30->23->28->30->11->14->19->16->21->25 
Output : 
11 14 16 19 21 23 25 28 30 30 
Explanation :
The resultant linked list is sorted.
'''

'''
Example 2:- 
Input : 
N = 7
Linked List=19->20->16->24->12->29->30 
Output : 
12 16 19 20 24 29 30 
Explanation : 
The resultant linked list is sorted.
'''

'''
Complexity:- 
 Expected Time Complexity : O(n^2)
 Expected Auxiliary Space : O(1)
'''

'''
Constraints:- 
0 <= n <= 5*10^3
'''

'''
User function Template for python3
'''

'''
Node Class
'''

'''
Initial Template for Python 3
'''

'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
'''

class Solution:
    def insertionSort(self, head):
        
        '''
        Base case: if the linked list is empty or has only one node
        '''

        if not head or not head.next:
            return head

        '''
        Head of the sorted linked list
        '''

        sorted_head = None 

        while head:
            current = head
            head = head.next

            '''
            If the current node is the first node in the sorted list or
            its data is smaller than the head of the sorted list
            '''

            if not sorted_head or current.data < sorted_head.data:
                current.next = sorted_head
                sorted_head = current
            else:
                
                '''
                Locate the node before the point of insertion
                '''

                temp = sorted_head
                while temp.next and temp.next.data < current.data:
                    temp = temp.next

                '''
                Insert the current node after temp
                '''

                current.next = temp.next
                temp.next = current

        return sorted_head

'''
Example usage:
Create a linked list from the given input and call the insertionSort method
Display the sorted linked list
'''

def display_linked_list(head):
    while head:
        print(head.data, end=" ")
        head = head.next
    print()




        

