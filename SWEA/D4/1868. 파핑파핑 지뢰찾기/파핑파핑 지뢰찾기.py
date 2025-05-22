from collections import deque
T = int(input())
def check_zero(r, c):
    if dp_check_zero[r][c]==1: # 0
        return True
    elif dp_check_zero[r][c]==-1: # 0이 아님
        return False
    for dr, dc in [(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)]:
        nr, nc = r+dr, c+dc
        if 0<=nr < n and 0<=nc<n :
            if graph[nr][nc]== '*': 
                dp_check_zero[r][c]=-1
                return False
    dp_check_zero[r][c] = 1
    return True        

for t in range(1, T + 1):
    n = int(input())
    graph = [list(input()) for _ in range(n)]
    q = deque()
    zero_q = deque()
    cnt_dot = 0
    cnt_group = 0
    opened = [[False] * n for _ in range(n)]
    dp_check_zero = [[0] * n for _ in range(n)]
    
    # 0인 칸 좌표 zero_q에 저장
    for r in range(n):
        for c in range(n):
            value = graph[r][c]
            if value == '.' :
                cnt_dot +=1
                if check_zero(r, c): 
                    zero_q.append((r, c))
    if not zero_q: # 0이 하나도 없을 때
        print(f'#{t} {cnt_dot}')
        continue
    while zero_q:
        zr, zc = zero_q.popleft()
        if not opened[zr][zc]:
            q.append((zr, zc))
            opened[zr][zc] = True
            cnt_dot-=1
            cnt_group+=1
        while q:
            r, c = q.popleft() # 0나오는 좌표
            for dr, dc in [(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)]:
                nr, nc = r+dr, c+dc
                if 0<=nr < n and 0<=nc<n :
                    if not opened[nr][nc] :
                        if check_zero(nr, nc):
                            q.append((nr, nc))
                        opened[nr][nc] = True
                        cnt_dot-=1
    ans = cnt_dot + cnt_group
    print(f'#{t} {ans}')
                    
                
        
    