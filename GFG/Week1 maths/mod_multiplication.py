def modmul(a, b, M):
    
    return (a % M) * (b % M) % M

if __name__ == "__main__":
    a = 5
    b = 3
    M = 11
    print(modmul(a, b, M))