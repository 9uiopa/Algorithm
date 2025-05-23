from collections import deque
T = 10
for test_case in range(1, T + 1):
    t = int(input())
    graph = [list(map(int, input())) for _ in range(100)]
    sr = sc = 0
    er = rc = 0
    result = 0
    visited = [[False]*100 for _ in range(100)]
    # 출발점 초기화
    for r in range(100):
        for c in range(100):
            if graph[r][c] == 2:
                sr, sc = r, c
            elif graph[r][c] == 3:
                er, ec = r, c
    q = deque()
    q.append((sr, sc))
    visited[sr][sc] = True
    while q:
        r, c = q.popleft()
        for dr, dc in [(-1,0), (1,0), (0,-1), (0,1)]:
            nr, nc = r+ dr, c +dc
            if 0<=nr<100 and 0<=nc<100 and not visited[nr][nc] and graph[nr][nc] !=1 :
                if graph[nr][nc] == 3:
                    result = 1
                    q.clear()
                    break
                elif graph[nr][nc] == 0:
                    q.append((nr, nc))
                    visited[nr][nc] = True
    print(f'#{t} {result}')
                    
        
        