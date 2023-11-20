def bsort(nums):
    size = len(nums)
    for i in range(size -1 , 0, -1):
        for j in range(i):
            if nums[j] > nums[j+1]:
                #swap
               # temp = nums[j]
                #nums[j] = nums[j+1]
                #nums[j+1] = temp
                nums[j], nums[j+1] = nums[j+1], nums[j]


nums = [ 5,3,8,6,7,2]
bsort(nums)
print("\n",nums)