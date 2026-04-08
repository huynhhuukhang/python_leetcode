from typing import List
nums=list(map(int,input().split()))

k=int(input())

def kLengthApart(nums:List[int], k:int)->bool:
    count=k
    for num in nums:
        if num==1:
            if count<k:
                return False

            count=0
        else:
            count+=1
    return True


print(kLengthApart(nums,k))