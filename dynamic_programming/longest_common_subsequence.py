def longest_common_subsequence(str1, str2):
    if str1 == str2:
        return len(str1)
    lcs = [[0 for _ in range(len(str1) + 1)] for _ in range(len(str2) + 1)]
    for i in range(1, len(str2) + 1):
        for j in range(1, len(str1) + 1):
            # print(str1[j], str2[i])
            if str1[j-1] == str2[i-1]:
                lcs[i][j] = 1 + lcs[i-1][j-1]
            else:
                lcs[i][j] = max(lcs[i][j-1], lcs[i-1][j])

    print(lcs)
