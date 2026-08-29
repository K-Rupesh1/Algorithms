'''def MoveZeroes(nums):
    if nums==0:
        return False
    n=len(nums)
    l=0
    for r in range(0,n):
        if nums[r]!=0:
            nums[l],nums[r]=nums[r],nums[l]
            l+=1
    return nums
            '''
            
# Using Slicing 
def MoveZeroes(nums):
    if not nums:
        return False
    non_zero=[x for x in nums if x!=0]
    zero=[x for x in nums if x==0]
    nums[:]=non_zero + zero
    return nums
            
    
    
    
    
nums=[1,0,2,0,3,4]
result=MoveZeroes(nums)
print(result)