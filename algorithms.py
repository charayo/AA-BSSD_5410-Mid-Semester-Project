# Original code accessed on: 2/22/22; from:
# https://www.geeksforgeeks.org/longest -common-subsequence-dp-4/
# This code is contributed by Nikhil Kumar Singh (nickzuck_007)
# Dynamic Programming implementation of LCS problem

# Dynamic Programming implementation of LCS problem
def lcs(X, Y):
    # find the length of the strings
    m = len(X)
    n = len(Y)
    # declaring the array for storing the dp values
    L = [[None] * (n + 1) for i in range(m + 1)]
    """Following steps build L[m+1][n+1] in bottom up fashion
    Note: L[i][j] contains length of LCS of X[o..¡-1] and Y[o..¡-1]"""
    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0 or j == 0:
                L[i][j] = 0
            elif X[i - 1] == Y[j - 1]:
                L[i][j] = L[i - 1][j - 1] + 1
            else:
                L[i][j] = max(L[i - 1][j], L[i][j - 1])
    # L[m] [n] contains the length of LCS of X[o..n-1] & Y[O..m-1]
    return L[m][n]
# end of function lcs

