def copy(inp):
    return [inp[asdf] for asdf in range(len(inp))]

def swap(arr,i,j):
    arr[i], arr[j] = arr[j], arr[i]

def selectionSort(inp):
    arr = inp
    seq = []
    compared = []
    n = len(arr)

    for i in range(n-1):
        k = i+1
        while k<n:
            if arr[k]<arr[i]:
                swap(arr,i,k)
            seq.append(copy(arr))
            compared.append([i, k])
            k += 1
    
    return seq, compared


def bubbleSort(inp):
    arr = inp
    seq = []
    compared = []
    n = len(arr)

    for i in range(1,n):
        k = 0
        while k<n-i:
            if arr[k]>arr[k+1]:
                swap(arr,k,k+1)
            seq.append(copy(arr))
            compared.append([k,k+1])
            k += 1
    
    return seq, compared

def insertionSort(inp):
    arr = inp
    seq = []
    compared = []
    n = len(arr)

    for i in range(1,n):
        k=i
        while k>0 and arr[k]<arr[k-1]:
            swap(arr,k,k-1)
            seq.append(copy(arr))
            compared.append([k-1,k])
            k -= 1
    
    return seq, compared

def mergeSort(inp):
    arr = inp
    seq = []
    compared = []
    n = len(arr)
    
    if n<=1:
        return [arr]
    #print("sorting",inp)
    k = n//2
    #sort front
    frontSort = mergeSort(copy(arr[:k]))
    arr[:k] = frontSort[-1]
    seq += [x+copy(arr[k:]) for x in frontSort]
    #sort back
    backSort = mergeSort(copy(arr[k:]))
    arr[k:] = backSort[-1]
    seq += [copy(arr[:k])+x for x in backSort]
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
                seq.append(copy(arr))
            arr[i] = toplace
            j += 1
        i += 1
        seq.append(copy(arr))
        #print("step:",arr)
    #print(seq)
    return seq, compared

def quickSort(inp):
    #first element as pivot (shrugs)
    arr = inp
    seq = [copy(arr)]
    compared = []
    n = len(arr)
    
    if n<=1:
        return [arr]
    i = 1
    j = 1
    k = n
    #invariant: arr[0,i) == p and arr[i,j) < p and arr[k,n) > p
    while j<k:
        if arr[j]==arr[0]:
            swap(arr,i,j)
            i += 1
            j += 1
        elif arr[j]<arr[0]:
            j += 1
        else:
            k -= 1
            swap(arr,j,k)
        seq.append(copy(arr))
    #print(arr[:i],arr[i:j],arr[j:])
    swapRange = min(i,j-i)
    for index in range(swapRange):
        swap(arr,index,index+j-swapRange)
        seq.append(copy(arr))
    #print(arr)
    i = j-i
    frontSort = quickSort(arr[:i])
    arr[:i] = frontSort[-1]
    seq += [x+arr[i:] for x in frontSort]
    backSort = quickSort(arr[j:])
    arr[j:] = backSort[-1]
    seq += [arr[:j]+x for x in backSort]
    #print(seq)
    return seq, compared


def heapSort(inp):
    arr = inp
    seq = [copy(arr)]
    compared = []
    n = len(arr)
    if n<=1:
        return [arr]

    def children(i):
        return (2*i,2*i+1)
    def parent(i):
        return i//2

    heapSize = 1
    while heapSize<n:
        i = heapSize
        while i>0 and arr[i]>arr[parent(i)]:
            swap(arr,i,parent(i))
            i = parent(i)
            seq.append(copy(arr))
        if i==heapSize:
            seq.append(copy(arr))
        heapSize += 1
    
    #print(arr)
    
    while heapSize>1:
        heapSize -= 1
        swap(arr,0,heapSize)
        seq.append(copy(arr))
        #print("managing",arr[:heapSize])
        i = 0
        while (children(i)[0]<heapSize and arr[i]<arr[children(i)[0]]) or (children(i)[1]<heapSize and arr[i]<arr[children(i)[1]]):
            maxIndex = i
            if arr[maxIndex]<arr[children(i)[0]]:
                maxIndex = children(i)[0]
            if children(i)[1]<heapSize and arr[maxIndex]<arr[children(i)[1]]:
                maxIndex = children(i)[1]
            assert maxIndex!=i, "Something went wrong with sifting down..." + str(arr) + str(i)
            swap(arr,i,maxIndex)
            i = maxIndex
            seq.append(copy(arr))
        if i==0:
            seq.append(copy(arr))
        #print("managed:",arr[:heapSize])
    
    return seq, compared

