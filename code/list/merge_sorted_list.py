def merge_lists(nums1, nums2):

    # Replace this placeholder return statement with your code
    merged_array=[]
    l1= len(nums1)
    l2= len(nums2)
    i=0
    j=0
    print(f"l1 : {l1}")
    while (i< l1) and (j < l2) :
            
            if(nums1[i] < nums2[j]):
                merged_array.append(nums1[i])
                i = i+1
            else:
                merged_array.append(nums2[j] )
                j = j+1  
    print(f"i : {i}")
    print(f"j : {j}")            
    while(i<l1):
        merged_array.append(nums1[i])
        i = i+1
    while(j<l2):
        merged_array.append(nums2[j])
        j = j+1
        
    return merged_array
    
print(merge_lists([1,2,3,4],[3,4,6,8]))
