from typing import List
nums = [6,2,6,5,1,2]
nums.sort()
sum_min=0
n=len(nums)
for i in range(0,n,2):
    sum_min+=min(nums[i],nums[i+1])

print(sum_min)
