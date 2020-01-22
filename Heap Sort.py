def PARENT(i):
    return (i+1)/2-1
def LEFT(i):
    return (i+1)*2-1
def RIGHT(i):
    return (i+1)*2

def maxHeapify(A,i,heap_size):
    left = LEFT(i)
    right = RIGHT(i)

    largest = i
    if left<heap_size and A[left]>A[i]:
        largest = left
    if right<heap_size and A[right]>A[largest]:
        largest = right
    if(largest !=i):
        t = A[largest]
        A[largest] = A[i]
        A[i] = t
        maxHeapify(A,largest,heap_size)

def buildMaxHeap(A,heap_size):
    for i in range(int(heap_size/2)-1,-1,-1):
        maxHeapify(A,i,heap_size)

def heapSort(A):
    heap_size = len(A)
    buildMaxHeap(A,heap_size)
    for i in range(heap_size-1,0,-1):
        t = A[i]
        A[i] = A[0]
        A[0] = t
        heap_size -=1
        maxHeapify(A,0,heap_size)


a = [1,2,34,3]
heapSort(a)

print(a)