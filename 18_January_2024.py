'''
Task:- 
A gallery with plants is divided into n parts, numbered 0, 1, 2, 3, ..., n-1. There are provisions for attaching water sprinklers in every division. A sprinkler with range x at division i can water all divisions from i-x to i+x.

Given an array gallery[] consisting of n integers, where gallery[i] is the range of the sprinkler at partition i (a power of -1 indicates no sprinkler attached), return the minimum number of sprinklers that need to be turned on to water the entire gallery. If there is no possible way to water the full length using the given sprinklers, print -1.
'''

'''
Example 1:- 
Input:
n = 6
gallery[] = {-1, 2, 2, -1, 0, 0}
Output:
2
Explanation: 
Sprinklers at index 2 and 5
can water the full gallery, span of
sprinkler at index 2 = [0,4] and span
of sprinkler at index 5 = [5,5].
'''

'''
Example 2:- 
Input:
n = 9
gallery[ ] = {2, 3, 4, -1, 2, 0, 0, -1, 0}
Output:
-1
Explanation: 
No sprinkler can throw water
at index 7. Hence all plants cannot be
watered.
'''

'''
Example 3:- 
Input:
n = 9
gallery[ ] = {2, 3, 4, -1, 0, 0, 0, 0, 0}
Output:
3
Explanation: 
Sprinkler at indexes 2, 7 and
8 together can water all plants.
'''

'''
Complexity:- 
 Expected Time Complexity: O( nlog(n) )
 Expected Auxiliary Space: O( n )
'''

'''
Constraints:- 
 1 ≤ n ≤ 10^5
 gallery[i] ≤ 50
'''

class Solution:
    def min_sprinklers(self, gallery, n):
        spk = []

        for i in range(n):
            if gallery[i] != -1:
                spk.append((max(0, i - gallery[i]), min(n - 1, i + gallery[i])))

        spk.sort()

        start = 0
        i = 0
        ans = 0

        while start < n:
            maxr = -1e9
            while i < len(spk):
                if spk[i][0] > start:
                    break
                
                maxr = max(maxr, spk[i][1])
                i += 1

            if maxr < start:
                return -1

            ans += 1
            start = maxr + 1

        return ans
        










