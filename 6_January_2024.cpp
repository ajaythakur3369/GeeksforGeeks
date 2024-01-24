/******************************************************************************
Task:- 
A Techfest is underway, and each participant is given a ticket with a unique number. Organizers decide to award prize points to everyone who has a ticket ID between a and b (inclusive). The points given to a participant with ticket number x will be the sum of powers of the prime factors of x.

For instance, if points are to be awarded to a participant with ticket number 12, the amount of points given out will be equal to the sum of powers in the prime factorization of 12 (2^2 × 3^1), which will be 2 + 1 = 3.

Given a and b, determine the sum of all the points that will be awarded to the participants with ticket numbers between a and b (inclusive).
*******************************************************************************/

/******************************************************************************
Example 1:- 
Input: 
a = 9
b = 12
Output: 
8
Explanation: 
For 9, prime factorization is:3^2 
So, sum of the powers of primes is: 2
For 10, prime factorization is : 2^1x5^1 
So, sum of the powers of primes is: 2
For 11, prime factorization is : 11^1 
So, sum of the powers of primes is: 1
For 12, prime factorization is : 2^2x 3^1 
So, sum of powers of primes is: 3
Therefore the total sum is 2+2+1+3=8.
*******************************************************************************/

/******************************************************************************
Example 2:- 
Input: 
a = 24, b = 27
Output: 
11
Explanation: 
For 24, prime factorization is: 2^3x3^1 
So, sum of the powers of primes is: 4
For 25, prime factorization is : 5^2 
So, sum of the powers of primes is: 2
For 26, prime factorization is : 13^1x2^1 
So, sum of the powers of primes is: 2
For 27, prime factorization is : 3^3  
So, sum of powers of primes is: 3
Therefore the total sum is 4+2+2+3=11.
*******************************************************************************/

/******************************************************************************
Complexity:- 
 Expected Time Complexity: O( b*log(b) )
 Expected Space Complexity: O( b*log(b) )
*******************************************************************************/

/******************************************************************************
Constraints:-
 1 <= a <= b <= 2x10^5
 1 <= b-a <= 10^5
*******************************************************************************/

class Solution {
public:
	int sumOfPowers(int a, int b){
	    int ans = 0;
        for(int i = a; i <= b; i++){
            int num = i;
            for(int j = 2; j*j <= i; j++){
                while(num%j == 0){
                    ans++;
                    num /= j;
                }
            }
            if(num > 1){
                ans++;
            }
        }
        return ans;
	}









