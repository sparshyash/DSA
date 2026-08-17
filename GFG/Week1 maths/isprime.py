def isprime(n):
    if(n<=1):
        return False
    if(n==2 or n==3):
        return  True
    if(n%2==0 or n%3 == 0):
        return False
    i=5
    while(i<=math.sqrt(n)):
        if(n%i==0 or n%(i+2)==0):
            return False
        i+=6
    return True
if __name__=="__main__":
    n=7
    ans=isprime(n)
    print(ans)