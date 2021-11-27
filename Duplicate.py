nums = [1,2,3,4,4,5]
n = len(nums)

for i in range(n-1):

    if nums[i] == nums[i+1]:
        print (nums[i])