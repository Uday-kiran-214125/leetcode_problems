nums=[2,0,2,1,1,0]
mid=0
low=0
high=len(nums)-1
for i in range(0,len(nums)):
    if mid>high:
        break
    if nums[i]==2:
        nums[mid],nums[high]=nums[high],nums[mid]
        high=high-1
        
    if nums[i]==0:
        nums[low],nums[mid]=nums[mid],nums[low]
        mid=mid+1
        low=low+1
        
    if nums[i]==1:
        mid=mid+1
        
    print(nums)

print(nums)