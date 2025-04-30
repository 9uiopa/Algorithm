T = int(input())
for test_case in range(1, T + 1):
    s1,s2 = input().split()
    dp = [[0]*(len(s2)+1) for _ in range(len(s1)+1)]
    for i in range(1, len(s1)+1):
        for j in range(1, len(s2)+1):
            if s1[i-1] == s2[j-1]:
                dp[i][j] = dp[i-1][j-1] +1
            else :
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    ans = dp[len(s1)][len(s2)]
    print("#" + str(test_case) + " " + str(ans))
            