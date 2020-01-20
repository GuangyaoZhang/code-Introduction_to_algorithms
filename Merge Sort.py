def merge(A,start,mid,end):
    L = A[start:mid+1]
    R = A[mid+1:end+1]

    L.append(float('inf'))
    R.append(float('inf'))
    l = 0
    r = 0
    for i in range(start,end+1,1):
        if(L[l]<R[r]):
            A[i]=L[l]
            l+=1
        else:
            A[i]=R[r]
            r+=1

def mergeSort(A,start,end):
    if(start==end):
        return
    mid = int((start+end)/2)
    mergeSort(A,start,mid)
    mergeSort(A,mid+1,end)
    merge(A,start,mid,end)
A = [0,1,1,4,2,5,6,3,21,1,-10]

mergeSort(A,0,len(A)-1)

print(A)
