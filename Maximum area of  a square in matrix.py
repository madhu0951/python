def max_area(M):
    res = 0
    for i in range(len(M)):
        res = max(res, M[i][0])
    for i in range(len(M[0])):
        res = max(res, M[0][i])
    for i in range(1, len(M)):
        for j in range(1, len(M[0])):
            if M[i][j] == 1:
                M[i][j] = min(M[i][j - 1], M[i - 1][j], M[i - 1][j - 1]) + 1

                res = max(res, M[i][j])
    return res * res


matrix = [
    [1, 0, 0, 0, 0, 1, 1],
    [0, 0, 0, 0, 0, 1, 1],
    [0, 1, 1, 1, 1, 0, 0],
    [0, 1, 1, 1, 1, 0, 0],
    [0, 1, 1, 1, 1, 0, 0],
    [0, 1, 1, 1, 1, 0, 0],
]
print(max_area(matrix))