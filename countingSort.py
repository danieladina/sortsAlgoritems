#  מיון של n איברים שידוע מראש שהערכים מ0 עד 9
def counting_sort(A):
    B = [0] * 10
    C = [0] * (len(A) + 1)

    for a in A:
        B[a % 10] += 1
    for i in range(1, len(B)):
        B[i] = B[i] + B[i - 1]
    for a in A[::-1]:
        digit = a % 10
        C[B[digit]] = a
        B[digit] -= 1
    return C[1:]


def main():
    A = [1, 5, 8, 7, 4, 6, 9, 8, 5, 2, 6, 4, 7, 8, 5, 0, 1, 5, 4]
    A_sorted = counting_sort(A)
    print(A_sorted)

if __name__ == '__main__':
    main()