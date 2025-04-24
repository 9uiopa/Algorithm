def move(r,c):
    if r==0:
        return c
    if c>0 and board[r][c-1] == 1 : #왼쪽
        board[r][c] = 0 # 방문처리
        return move(r,c-1)
    elif c<99 and board[r][c+1] == 1: #오른쪽
        board[r][c] = 0
        return move(r, c+1)
    elif board[r-1][c] == 1: # 위쪽
        return move(r-1,c)

for test_case in range(1,11):
    t = input()
    board = [list(map(int, input().split())) for _ in range(100)]
    end_idx = board[-1].index(2)
    ans = move(99, end_idx)
    print("#"+str(test_case) + " " + str(ans))