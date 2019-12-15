def copy(inp):
    return [inp[asdf] for asdf in range(len(inp))]

def swap(arr,i,j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp

def selectionSort(inp):
    arr = inp
    seq = []
    n = len(arr)

    for i in range(n):
        k = i
        minIndex = k
        while k<n:
            if arr[k]<arr[minIndex]:
                minIndex = k
            seq.append(copy(arr))
            k += 1
        swap(arr,i,minIndex)
        seq.append(copy(arr))
    
    return seq


def bubbleSort(inp):
    arr = inp
    seq = []
    n = len(arr)

    for i in range(1,n):
        k = 0
        while k<n-i:
            if arr[k]>arr[k+1]:
                swap(arr,k,k+1)
            seq.append(copy(arr))
            k += 1
    
    return seq

def insertionSort(inp):
    arr = inp
    seq = []
    n = len(arr)

    for i in range(1,n):
        k=i
        while k>0 and arr[k]<arr[k-1]:
            swap(arr,k,k-1)
            seq.append(copy(arr))
            k -= 1
        seq.append(copy(arr))
    
    return seq


#TODO: Fix the merging sequence. Does sort correctly but process is wrong.
def mergeSort(inp):
    arr = inp
    seq = []
    n = len(arr)
    
    if n<=1:
        return [arr]
    print("sorting",inp)
    k = n//2
    #sort front
    frontSort = mergeSort(arr[:k])
    arr[:k] = frontSort[-1]
    seq += [x+arr[k:] for x in frontSort]
    #sort back
    backSort = mergeSort(arr[k:])
    arr[k:] = backSort[-1]
    seq += [arr[:k]+x for x in backSort]
    i = 0
    j = k
    # allow shifting for convenience

    while i<j and j<n:
        if arr[i]<=arr[j]:
            pass
        else:
            #shift
            toplace = arr[j]
            for index in reversed(range(i,j)):
                arr[index+1] = arr[index]
            arr[i] = toplace
            j += 1
        i += 1
        seq.append(copy(arr))
        print("step:",arr)
    return seq

    


