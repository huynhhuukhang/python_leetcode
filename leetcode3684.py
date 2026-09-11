from typing import List

nums = [84,93,100,77,90]
print("nhap k")
k=int(input())

def maxKDistinct(nums: List[int], k: int) -> List[int]:
        res=[]
        nums.sort()
        cnt=0
        for i in range(len(nums)-1,-1,-1):
            if cnt==k:break
            else:
                if nums[i] in res: continue
                else:
                    res.append(nums[i])
                    cnt+=1
        
        return res

print(maxKDistinct(nums,k))