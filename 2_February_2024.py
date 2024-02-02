'''
Task:- 
Given a string, s, the objective is to convert it into integer format without utilizing any built-in functions. If the conversion is not feasible, the function should return -1.
'''

'''
Example 1:- 
Input:
s = "-123"
Output: 
-123
Explanation:
It is possible to convert -123 into an integer 
and is so returned in the form of an integer
'''

'''
Example 2:- 
Input:
s = "21a"
Output: 
-1
Explanation: 
The output is -1 as, due to the inclusion of 'a',
the given string cannot be converted to an integer.
'''

'''
Complexity:- 
 |s| = length of string str.
 Expected Time Complexity: O( |s| ), 
 Expected Auxiliary Space: O(1)
'''

'''
Constraints:- 
 1 ≤ |s| ≤ 10
'''

'''
User function template for Python
'''

class Solution:
    
    '''
    Your task is to complete this function
    Function should return an integer
    '''
    
    def atoi(self,s):
      result = 0
      if not s:
        return -1
      negative = False
      if s[0] == '-':
        negative = True
        s = s[1:]
      for c in s:
        if c.isdigit():
          result = result * 10 + int(c)
        else:
          return -1
      return -result if negative else result
