def countingSort(A,k):
    C = []
    for i in range(k+1):
        C.append(0)

    B = list(A)

    for i in A:
        C[i]+=1
    for i in range(1,k):
        C[i]+=C[i-1]
    for i in range(len(A)-1,-1,-1):
        B[C[A[i]]-1]=A[i]
        C[A[i]]-=1
    return B


A = [1,2,4,7,3,5,8,2,4,9,1,6,2,5]
B = countingSort(A,10)
print(B)