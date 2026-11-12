def longestMonotonicSubarray(nums:List[int])->int:
    tang=1
    giam=1
    maxlen=1
    for i in range(1,len(nums)):
        if nums[i]>nums[i-1]:
            tang+=1
            giam=1
        if nums[i]<nums[i-1]:
            giam+=1
            tang=1
        if nums[i]==nums[i-1]:
            tang=1
            giam=1

        result=max(tang,giam,maxlen)

    return result

nums=[1,4,3,3,2]
print(longestMonotonicSubarray(nums))
nums1=[3,3,3,3,3]
print(longestMonotonicSubarray(nums1))