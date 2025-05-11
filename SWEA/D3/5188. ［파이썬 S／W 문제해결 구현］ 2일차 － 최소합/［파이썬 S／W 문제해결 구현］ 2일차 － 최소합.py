T = int(input())
for test_case in range(1, T + 1):
    n = int(input())
    board = [list(map(int, input().split())) for _ in range(n)]
    dp = [[0] * n for _ in range(n)]
    for r in range(n):
        for c in range(n):
            top = left = 251 # 문제 조건상 dp[r][c]의 최댓값+1
            if r==0 and c==0:
                dp[r][c] = board[r][c]
                continue
            if r > 0 :
                top = dp[r-1][c] + board[r][c]
            if c > 0 :
                left = dp[r][c-1] + board[r][c]
            dp[r][c] = min(top, left)
    print("#" + str(test_case) + " " + str(dp[n-1][n-1]))