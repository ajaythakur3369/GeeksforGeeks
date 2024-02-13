'''
Task:- 
A function F is defined as follows F(n)= (1) +(2*3) + (4*5*6) ... upto n terms (look at the examples for better clarity). Given an integer n, determine the F(n).
'''

'''
Example 1:- 
Input: n = 5
Output: 365527
Explanation: 
F(5) = 1 + 2*3 + 4*5*6 + 7*8*9*10 + 11*12*13*14*15 = 365527.
'''

'''
Example 2:- 
Input: n = 7
Output: 6006997207
Explanation: 
F(7) = 1 + 2*3 + 4*5*6 + 7*8*9*10 + 11*12*13*14*15 + 
16*17*18*19*20*21 + 22*23*24*25*26*27*28 = 6006997207.
6006997207 % 109+7 = 6997165
'''

'''
Complexity:- 
 Expected Time Complexity: O(n^2)
 Expected Space Complexity: O(1)
'''

'''
Constraints:- 
 1 ≤ n ≤ 10^3
'''

'''
User function Template for python3
'''

class Solution:
    def sequence(self, n):
        
        '''
        Code here
        '''
        
        res=0
        x=1
        for i in range(1,n+1):
            sum=1
            for n in range(1,i+1):
                sum=sum*x
                x=x+1
            res+=sum
        return (res%1000000007)
