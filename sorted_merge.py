def sorted_merge(A: list, B: list):
    tmp = [None] * len(A)
    aPtr = 0
    bPtr = 0
    for i in range(len(A)):
        if bPtr>= len(B):
            tmp[i] = A[i]
        else:
            if A[aPtr] <= B[bPtr]:
                tmp[i] = A[aPtr]
                aPtr += 1
            else:
                tmp[i] = B[bPtr]
                bPtr += 1
    return tmp

A = [1,4,6,9, 999, 999, 999, 999, 999]
B = [2,5,7,8,10]
print(sorted_merge(A, B))
                