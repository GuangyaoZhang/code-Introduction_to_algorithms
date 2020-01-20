def insertSort(A:list):
    for j in range(2,len(A)):
        for i in range(j-1,0,-1):
            if(A[i]>A[i+1]):
                t = A[i]
                A[i] = A[i+1]
                A[i+1] = t
    return A

A = [4,5,5,7,8,234,746,23425,352345,3]
A = insertSort(A)
print(A)