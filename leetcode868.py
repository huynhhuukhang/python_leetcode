n=int(input())
def binaryGap(n:int)->int:
    K=[]
    for i in range(32):
        if(n >> i)&1: 
            K.append(i)
    ans=0
    for i in range(len(K)-1):
        ans=max(ans,K[i+1]-K[i])
    return ans
print(binaryGap(n))