
def heapify(arr,i,heapsize):


    l = i * 2 + 1
    r = i * 2 + 2
    maxi=i

    if l< heapsize and arr[l]>arr[maxi]:
        maxi=l
    if r<heapsize and arr[r]>arr[maxi]:
        maxi = r


    if maxi !=i:
        arr[maxi],arr[i]=arr[i],arr[maxi]
        heapify(arr,maxi,heapsize)

def buildheap(arr):
    for i in range(len(arr)//2,-1,-1):
        heapify(arr,i,len(arr))


def heapsort(arr):
    buildheap(arr)

    for i in range(len(arr)-1,0,-1):
        arr[0],arr[i]=arr[i],arr[0]
        heapify(arr,0,i)












def main():
    arr=[4,6,3,6,3,543,32,52,32,7,2]
    heapsort(arr)
    print(arr)


if __name__ == '__main__':
    main()