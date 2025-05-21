from collections import deque
T = int(input())

for t in range(1, T + 1):
    n = int(input())
    graph = [list(map(int, input())) for _ in range(n)]
    sr =sc =0
    end = (0,0)
    visited = set()
    ans = 0
    for r in range(n):
        for c in range(n):
            if graph[r][c] ==2:
                sr, sc = r, c
            elif graph[r][c] ==3:
                end = (r,c)
    q = deque()
    q.append((sr, sc, 0))
    while q:
        r, c, cnt = q.popleft()
        visited.add((r, c))
        for dr, dc in [(-1,0), (1,0), (0,-1), (0,1)]:
            nr, nc = r + dr, c + dc
            if 0<=nr < n and 0<= nc < n and graph[nr][nc] != 1 :
                if (nr, nc) == end: # 도착
                    ans = cnt
                    q.clear()
                    break
                if (nr, nc) not in visited :
                    q.append((nr, nc, cnt + 1))
                    
    print(f'#{t} {ans}')
                
        
        
        
        
        
        
        
        