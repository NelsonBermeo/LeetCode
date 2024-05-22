def removeElement(nums, val):
    num = len(nums)
    count = 0
    i = 0
    if nums is None:
        return 0
    while i < len(nums):
        if nums[i] == val:
            nums.remove(nums[i])
            count += 1
        else:
            i+=1 
    return num-count

def removeElement2(nums, val):
    num = len(nums)
    count = 0
    i = 0
    if nums is None:
        return 0
    while i < len(nums):
        if nums[i] == val:
            nums[num-i]
            count += 1
        else:
            i+=1 
    return num-count
    
            



if __name__ == "__main__":
    arr = [1]
    val = 2
    print(removeElement(arr, val))