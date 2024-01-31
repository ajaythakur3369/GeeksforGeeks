'''
Task:- 
Complete the Insert and Search functions for a Trie Data Structure. 

 1. Insert: Accepts the Trie's root and a string, modifies the root in-place, and returns nothing.
 2. Search: Takes the Trie's root and a string, returns true if the string is in the Trie, otherwise false.
'''

'''
Example 1:- 
Input:
n = 8
list[] = {the, a, there, answer, any, by, bye, their}
key = the
Output: 1
Explanation: 
"the" is present in the given set of strings. 
'''

'''
Example 2:- 
Input:
n = 8
list[] = {the, a, there, answer, any, by, bye, their}
key = geeks
Output: 0
Explanation: 
"geeks" is not present in the
given set of strings.
'''

'''
Complexity:- 
 Expected Time Complexity: O(M+|key|)
 Expected Auxiliary Space: O(M)
 Here M = sum of the length of all strings which are present in the list[] 
'''

'''
Constraints:- 
 1 <= N <= 10^4
 1 <= length of list[i] <= 30
 All strings will constitute of lowercase alphabets only.
'''

'''
User function Template for python3
'''

'''
class TrieNode: 
      
    def __init__(self): 
        self.children = [None]*26
  
        # isEndOfWord is True if node represent the end of the word 
        self.isEndOfWord = False
'''

class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.isEndOfWord = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

class Solution:
    @staticmethod
    def insert(root, key):
        for ch in key:
            index = ord(ch) - ord('a')
            if not root.children[index]:
                root.children[index] = TrieNode()
            root = root.children[index]
        root.isEndOfWord = True
 
    '''
    ringewashere
    '''
    
    @staticmethod
    def search(root, key):
        for ch in key:
            index = ord(ch) - ord('a')
            if not root.children[index]:
                return False
            root = root.children[index]
        return root.isEndOfWord

 