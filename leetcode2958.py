from typing import List
import collections

nums=list(map(int,input().split()))
k=int(input())
def maxSubarrayLength(nums: List[int], k: int) -> int:
    best=0
    f=collections.Counter()
    left=0
    n=len(nums)
    for right in range(n):
        f[nums[right]]+=1
        while f[nums[right]]>k:
            f[nums[left]]-=1
            left+=1

        best=max(best, right-left+1)

    return best


print(maxSubarrayLength(nums,k))
