import math
n=int(input())
def checkPerfectNumber(n:int)->bool:
    cnt=1
    if n<1:return False
    for i in range(2,math.isqrt(n)+1):
        if n%i==0:
            cnt+=i
            if i*i!=n:
                cnt+=n//i
    return cnt==n

print(checkPerfectNumber(n))