def merge_two_sortedz_array(nums1,nums2):
    i=0
    j=0
    temp=[0]*(len(nums1)+len(nums2))
    k=0

    while (i<len(nums1) and j<len(nums2)):
        if nums1[i]<=nums2[j]:
            temp[k]=nums1[i]
            i+=1
            k+=1
        else:
            temp[k]=nums1[j]
            j+=1
            k+=1
    while j<len(nums2):
        temp[k]=nums2[j]
        j+=1
        k+=1
    while i <len(nums1):
        temp[k]=nums1[i]
        k+=1
        i+=1

    return temp 


if __name__=="__main__":
    nums1=[1,2,3]
    nums2=[4,6,9]
    print(merge_two_sortedz_array(nums1,nums2))


    
    