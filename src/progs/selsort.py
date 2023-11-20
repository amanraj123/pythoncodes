def selsort(nums):
    for i in range(len(nums) -1):
        minpos = i
        for j in range(i, len(nums)):
            # change min pos only
            if nums[j] < nums[minpos]:
                minpos = j
        if i != minpos:

            temp = nums[i]
            nums[i] = nums[minpos]
            nums[minpos] = temp

        print(nums)

nums = [ 5,3,8,6,7,2]
selsort(nums)
print("\n",nums)