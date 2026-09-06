# hme array k elements jodke n bnana hai with max gcd and in strictly increasing order  

4 + 8 + 12 =24 =n and m =3 (  elements)  now 4(1+2+3) = 24  and gcd(4,8,12) =4  and 4 is max gcd possible with m=3 and n=24

sum of first n elements = n*(n+1)/2 == sum_min

gcd * sum_min =n => gcd = n/sum_min  => g<=n/sum_min or sum_min<=n/g    


import math


class Solution:
    def maxGcdSeq(self, n, m):
        # code here
        
        
        res=[]
        
        min_sum = m * (m+1)//2
        
        if n < min_sum:
            return [-1]
            
        
        
        max_g=1
        
        for d in range(1, int(math.sqrt(n))+1):
            
            if n % d==0:
                if n//d>=min_sum:
                    max_g=max(max_g,d)
                    
                paired=n//d
                if n//paired>=min_sum:    
                    max_g=max(max_g,paired)
        for i in range(1,m):
            res.append(i*max_g)
        res.append(n-sum(res))    
        return res
                
        
            
            
            
            