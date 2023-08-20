import random


def partition(A, l, r):
    rand_pivot = random.randint(l,r)
    A[l], A[rand_pivot] = A[rand_pivot], A[l]
    pivot = A[l]
    last_min = l
    for j in range(l, r+1):
        if A[j] < pivot:
            last_min += 1
            A[last_min], A[j] = A[j], A[last_min]
    A[l], A[last_min] = A[last_min], A[l]
    return last_min

def randomize_quick_sort(A, l, r):
    if l < r:
        q = partition(A, l, r)
        randomize_quick_sort(A, l, q-1)
        randomize_quick_sort(A, q+1, r)

def main():
    A = [5,8,1,9,14,3,56,782,1,5,1,7]
    print("The list is: ", A)
    randomize_quick_sort(A, 0, len(A)-1)
    print("The sorted list is: ",  A)



if __name__ == '__main__':
    main()