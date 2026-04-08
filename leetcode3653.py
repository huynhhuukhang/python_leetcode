MOD = 10**9+7

def xor_after_queries(nums, queries)->int:
    for l,r,k,v in queries:
        for i in range(l,r+1,k):
            nums[i]=(nums[i]*v)%MOD
        res=0
    for x in nums:
        res^=x
    return res

n=int(input())
nums=list(map(int,input().split()))
q=int(input())
queries= [list(map(int,input().split())) for _ in range(q)]
print(xor_after_queries(nums,queries))