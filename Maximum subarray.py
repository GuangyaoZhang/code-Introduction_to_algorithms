#Page 41

def findMaxCrosssingSubArray(subs,low,mid,high):
    max_left = 0
    max_right = 0
    max_left_idx = mid
    max_right_idx = mid
    left_sum=0
    right_sum=0
    for i in range(mid-1,low-1,-1):
        left_sum+=subs[i]
        if(left_sum>max_left):
            max_left=left_sum
            max_left_idx=i
    for i in range(mid+1,high+1,1):
        right_sum+=subs[i]
        if(right_sum>max_right):
            max_right=right_sum
            max_right_idx=i
    return (max_left+max_right+subs[mid],max_left_idx,max_right_idx)

def findMaxSubArray(subs,low,high):
    if(low==high):
        return (subs[low],low,high)
    mid = int((low+high)/2)
    left = findMaxSubArray(subs,low,mid)
    right = findMaxSubArray(subs,mid+1,high)
    mid = findMaxCrosssingSubArray(subs,low,mid,high)

    if(left[0]>right[0] and left[0]>mid[0]):
        return left
    elif(right[0]>mid[0]):
        return right
    else:
        return mid


subs = [4, 4, -2, -4, -1, -7, -2, -2, -1]
max = findMaxSubArray(subs,0,len(subs)-1)

print(max)