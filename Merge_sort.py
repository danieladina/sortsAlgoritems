def mergeb(A, B):
    c = []
    a = 0
    b = 0
    while a < len(A) and b < len(B):
        if A[a] < B[b]:
            c.append(A[a])
            a = a + 1
        else:
            c.append(B[b])
            b = b + 1
    if a == len(A):
        while b < len(B):
            c.append(B[b])
            b = b + 1
    else:
        while a < len(A):
            c.append(A[a])
            a = a + 1
    return c


def mergerec(A, L, R):  # 0,a,len(A)-1
    if L == R:
        return [A[L]]
    M = (L + R) // 2
    left = mergerec(A, L, M)
    right = mergerec(A, M + 1, R)
    return mergeb(left, right)


def main():
    i = 0
    c = [8, 5, 60, 7, 10, 7, 4, 6]
    d = [3, 4, 6, 8]
    print(mergerec(c, 0, 7))


if __name__ == '__main__':
    main()