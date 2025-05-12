T = int(input())
def turn(board):
    temp = [row[:] for row in board]
    return [row[::-1] for row in list(map(list,zip(*temp)))]
for test_case in range(1, T + 1):
    n = int(input())
    board = [list(input().split()) for _ in range(n)]
    turn1 = turn(board)
    turn2 = turn(turn1)
    turn3 = turn(turn2)
    result_board = ["" for _ in range(n)]

    for i in range(n):
        for j in range(n):
            result_board[i] += turn1[i][j]
        result_board[i] += " "
        for k in range(n):
            result_board[i] += turn2[i][k]
        result_board[i] += " "
        for l in range(n):
            result_board[i] += turn3[i][l]
            
    print("#" + str(test_case))
    for line in result_board:
        print(line)
        