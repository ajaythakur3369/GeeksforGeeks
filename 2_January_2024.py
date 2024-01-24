'''
Task:- 
Given an array a of length n and a number k, find the largest sum of the subarray containing at least k numbers. It is guaranteed that the size of array is at-least k.
'''

'''
Example 1:- 
Input : 
n = 4
a[] = {1, -2, 2, -3}
k = 2
Output : 
1
Explanation :
The sub-array of length at-least 2
that produces greatest sum is {1, -2, 2}
'''

'''
Example 2:- 
Input :
n = 6 
a[] = {1, 1, 1, 1, 1, 1}
k = 2
Output : 
6
Explanation :
The sub-array of length at-least 2
that produces greatest sum is {1, 1, 1, 1, 1, 1}
'''

'''
Complexity:- 
 Expected Time Complexity: O(n)
 Expected Auxiliary Space: O(n)
'''

'''
Constraints:- 
1 <= n <= 10^5
-10^5 <= a[i] <= 10^5
1 <= k <= n
'''

'''
User function Template for python3
'''

class Solution():
    def maxSumWithK(self, a, n, k):
        # Code here
        s,m=0,float('-inf')
        l,r=0,0
        st=0
        while r < n :
            s += a[r]
            if r-l +1 == k :
                m=max(m,s)
            if r-l +1 > k :
                m=max(m,s)
                st += a[l]
                l +=1
                if st < 0 :
                    s -=st
                    st =0
                m=max(m,s)
            r +=1
        return m

'''
Driver Code Starts
Initial Template for Python 3
'''

def main():
    T = int()
    while(T > 0):
        n = int(input())
        a = [int(x) for x in input().strip().split()]
        k = int(input())
        
        ob = Solution()
        print(ob.maxSumWithK(a, n, k))

        T-=1


if __name__ == "__main__":
    main()





