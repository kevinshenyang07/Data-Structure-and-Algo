def min_distance(word1, word2):
    '''
    1) definition:

    given word1 and word2, d[i][j] is the edit distance between word1[:i] and word2[:j]

    2) base case:

    d[0][j] = j
    d[i][0] = i

    3) state trasition function:

    d[i][j] = min(d[i-1][j] + 1, d[i][j-1] + 1, d[i-1][j-1])      xi = yj
            = min(d[i-1][j] + 1, d[i][j-1] + 1, d[i-1][j-1] + 1)  xi != yj

    d[i-1][j] + 1: insert a char to word1
    d[i][j-1] + 1: delete a char from word2
    d[i-1][j-1]  : distance before adding a char to each string
    '''
    m, n = len(word1), len(word2)
    dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            cost = 0 if word1[i-1] == word2[j-1] else 1
            dp[i][j] = min(dp[i-1][j] + 1, dp[i][j-1] + 1, dp[i-1][j-1] + cost)

    return dp[m][n]
