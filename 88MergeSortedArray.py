#The reason we want to not create a new list is because 
#   that could would be a bit less space complexity

#They want the answer in num1 

#One solution to this problem is by creating a temp list and putting 
#   sorted values into the temp list and then changing the num1 list into
#   the temp, neet code says that this would grant a time and space 
#   complexity of O(n)

#Let's at least try and figure out that solution, so this is my solution
#   that kind of just brute forces it and I guess has a time complexity of 
#   like 5n or something, let's figure out what space complexity is now 
#   hold on

#so we did it, but we decided to skip the optimized space solution, lets come back to that 

def merge(ls1, ls2, m, n):
    if ls2 == []:
        return ls1
    boolean = False
    for i in ls1:
        if i != 0:
            boolean = True
    if boolean == False:
        for i in range(len(ls1)):
            ls1[i] = ls2[i]
        return ls1
    
    temp_ls = []
    i = j = 0
    while len(ls1) - n > i and len(ls2) > j:
        if ls1[i] <= ls2[j]:
            temp_ls.append(ls1[i])
            i += 1 
        if ls1[i] > ls2[j]:
            temp_ls.append(ls2[j])
            j += 1 
    
    while len(ls1) - n > i:
        temp_ls.append(ls1[i])
        i += 1 

    while len(ls2) > j:
        temp_ls.append(ls2[j])
        j += 1

    for p in range(len(ls1)):
        ls1[p] = temp_ls[p]
    
    return ls1


def merge2(nums1, m, nums2, n):
    """
    :type nums1: List[int]
    :type m: int
    :type nums2: List[int]
    :type n: int
    :rtype: None Do not return anything, modify nums1 in-place instead.
    """
    # if nums2 == []:
    #     return 
    # boolean = False
    # for i in nums1:
    #     if i != 0:
    #         boolean = True
    # if boolean == False:
    #     for i in range(len(nums1)):
    #         nums1[i] = nums2[i]
    #     return

    #temp_ls = []
    i = j = k = 0
    while len(nums1) - n > i and len(nums2) > j:
        if nums1[i] <= nums2[j]:
            nums1[k] = nums1[i]
            i += 1 
            k += 1 
        elif nums1[i] > nums2[j]:
            nums2[j] = nums1[i]
            nums1[k] = nums2[j]
            j += 1 
            k += 1

    while len(nums1) - n > i:
        nums1[k] = nums1[i]
        i += 1 
        k += 1 

    while len(nums2) > j:
        nums1[k] = nums2[j]
        j += 1 
        k += 1


    #for p in range(len(nums1)):
        #nums1[p] = temp_ls[p]
    
    return

def merge3(nums1, m, nums2, n):
    """
    :type nums1: List[int]
    :type m: int
    :type nums2: List[int]
    :type n: int
    :rtype: None Do not return anything, modify nums1 in-place instead.
    """
    # if nums2 == []:
    #     return 
    # boolean = False
    # for i in nums1:
    #     if i != 0:
    #         boolean = True
    # if boolean == False:
    #     for i in range(len(nums1)):
    #         nums1[i] = nums2[i]
    #     return

    #temp_ls = []
    k = len(nums1) - 1
    while k > 0:
        if n == 0:
            if nums1[m-1] <= nums2[n]:
                nums1[k] = nums2[n]
                n -= 1 
                k -= 1 
            elif nums1[m-1] > nums2[n]:
                nums1[k] = nums1[m-1]
                m -= 1 
                k -= 1 
        elif m == 0:
            if nums1[m] <= nums2[n-1]:
                nums1[k] = nums2[n-1]
                n -= 1 
                k -= 1 
            elif nums1[m] > nums2[n-1]:
                nums1[k] = nums1[m]
                m -= 1 
                k -= 1 
        else:
            if nums1[m-1] <= nums2[n-1]:
                nums1[k] = nums2[n-1]
                n -= 1 
                k -= 1 
            elif nums1[m-1] > nums2[n-1]:
                nums1[k] = nums1[m-1]
                m -= 1 
                k -= 1 
        

    # while len(nums1) - n > i:
    #     nums1[k] = nums1[i]
    #     i += 1 
    #     k += 1 

    # while len(nums2) > j:
    #     nums1[k] = nums2[j]
    #     j += 1 
    #     k += 1


    #for p in range(len(nums1)):
        #nums1[p] = temp_ls[p]
    
    return

if __name__ == "__main__":
    ls1 = [1, 2, 3, 0, 0, 0]
    ls2 = [2, 5, 6]
    merge3(ls1, 3 , ls2 , 3 )
    print(ls1)
    