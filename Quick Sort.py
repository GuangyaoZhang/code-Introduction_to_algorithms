import random
def randomizedPartition(A,p,r):
    i = random.randint(p,r)
    t = A[i]
    A[i] = A[r]
    A[r] = t

    s = p
    for i in range(p,r,1):
        if(A[i]<A[r]):
            t = A[s]
            A[s]=A[i]
            A[i] = t
            s+=1
    t = A[r]
    A[r] = A[s]
    A[s] = t

    return s


def quickSort(A,p,r):
    if r>p:
        q = randomizedPartition(A,p,r)
        quickSort(A,p,q)
        quickSort(A,q+1,r)

A = [4,5,5,7,8,234,746,23425,352345,3]

quickSort(A,0,len(A)-1)
print(A)
