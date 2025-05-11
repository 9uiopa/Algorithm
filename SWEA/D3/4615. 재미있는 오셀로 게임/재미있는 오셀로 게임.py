T = int(input())
for test_case in range(1, T + 1):
    n, m = map(int, input().split())
    board = [[0]*n for _ in range(n)]
    half = int(n/2)
    board[half-1][half-1] = 100
    board[half-1][half] = 1
    board[half][half-1] = 1
    board[half][half] = 100
    total = 0
    
    for _ in range(m):
        c, r, color = map(int, input().split())
        c-=1
        r-=1
        if color ==2 : color = 100
        board[r][c] = color
        # 가운데 색 변경
        # 8방향 검사
        for dr, dc in [(-1,0), (1,0),(0,-1),(0,1), (-1,-1),(-1,1),(1,-1),(1,1)]:
            nr, nc = r + dr, c + dc
            temp = []

            # 반대색 돌이 연속될 경우 저장
            while 0 <= nr < n and 0 <= nc < n and board[nr][nc] not in [0, color]:
                temp.append((nr, nc))
                nr += dr
                nc += dc

            # 같은 색 돌로 끝나는 경우에만 뒤집기
            if 0 <= nr < n and 0 <= nc < n and board[nr][nc] == color:
                for tr, tc in temp:
                    board[tr][tc] = color

    # 결과 집계
    black = sum(row.count(1) for row in board)
    white = sum(row.count(100) for row in board)
    print("#" + str(test_case) + " " + str(black) + " " + str(white))
        

            
    