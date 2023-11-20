def bubsort(nums):
    size = len(nums)
    for i in range(size - 1 ):
        swapped = False
        for j in range(size -1-i ):
            if nums[j] > nums[j+1]:
                nums[j] , nums[j+1] = nums[j+1], nums[j]
                swapped = True
        if  not swapped:
            break

if __name__ == '__main__':
    elements = [ 38, 9, 29, 27,2,19,26]
    #elements = [ 1,2,3]
    bubsort(elements)
    print(elements)