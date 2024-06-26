'''
Task:- 
Given weights and values of N items, we need to put these items in a knapsack of capacity W to get the maximum total value in the knapsack.
'''

'''
Example 1:- 
Input:
N = 3, W = 50
value[] = {60,100,120}
weight[] = {10,20,30}
Output:
240.000000
Explanation:
Take the item with value 60 and weight 10, value 100 and weight 20 and split the third item with value 120 and weight 30, to fit it into weight 20. so it becomes (120/30)*20=80, so the total weight becomes 60+100+80.0=240.0
Thus, total maximum value of item we can have is 240.00 from the given capacity of sack. 
'''

'''
Example 2:- 
Input:
N = 2, W = 50
value[] = {60,100}
weight[] = {10,20}
Output:
160.000000
Explanation:
Take both the items completely, without breaking.
Total maximum value of item we can have is 160.00 from the given capacity of sack.
'''

'''
Complexity:- 
 Expected Time Complexity : O(NlogN)
 Expected Auxilliary Space: O(1)
'''

'''
Constraints:-
 1 <= N <= 10^5
 1 <= W <= 10^9
 1 <= valuei, weighti <= 10^4
'''
 
'''
User function Template for python3
'''

class Item:
    def __init__(self,val,w):
        self.value = val
        self.weight = w
        
class Solution: 
    
    '''
    Function to get the maximum total value in the knapsack.
    '''
    
    def fractionalknapsack(self, W,arr,n):
        
        '''
        Code here
        '''
        
        vpw=[]
        for i in range(len(arr)):
            vpw.append((arr[i].value/arr[i].weight,i))
        vpw.sort(reverse=True)
        
        ans=0.0
        for i in vpw:
            ii=i[1]
            if arr[ii].weight<=W:
                ans+=arr[ii].value
                W-=arr[ii].weight
            else:
                ans+=i[0]*W
                break
        return ans