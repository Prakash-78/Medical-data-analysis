def median(nums1,nums2):
    n1 = len(nums1)
    n2 = len(nums2)
    el1 = el2 = -1
    n = n1 + n2
    ind2 = n//2
    ind1 = ind2-1
    i = j = 0
    cnt = 0
    while  ((i < n1) and (j<n2)):
        if nums1[i] < nums2[j]:
            if cnt == ind1:
                el1 = nums1[i]
            if cnt == ind2:
                el2 = nums2[i]
            cnt += 1
            i += 1
        else:
            if cnt == ind1:
                el1 = nums2[j]
            if cnt == ind2:
                el2 = nums2[j]
            cnt += 1
            j += 1
    
    while i < n1:
        if cnt == ind1:
            el1 = nums1[i]
        if cnt == ind2:
            el2 = nums1[i]
        i += 1
        cnt += 1
    
    while j < n2:
        if cnt == ind1:
            el1 = nums2[j]
        if cnt == ind2:
            el2 = nums2[j]
        cnt += 1
        j += 1
    
    if n%2 == 0:
        median = (el1+el2)//2
        return median
    else:
        return el2

nums1 = [1,2]
nums2 = [3]
print(median(nums1,nums2))