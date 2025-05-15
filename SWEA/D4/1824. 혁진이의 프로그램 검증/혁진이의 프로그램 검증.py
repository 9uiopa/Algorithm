# 내 풀이
from collections import deque
T = int(input())

def execute():
    def get_next(r, c, di):
        # 다음 좌표(nr, nc) 결정, 범위 초과 시 처리        
        dr, dc = di
        nr, nc = r + dr, c + dc
        if nr < 0 : nr = R-1
        if nr >= R : nr = 0
        if nc < 0 : nc = C-1
        if nc >= C : nc = 0
        return nr, nc
    while q :
        r, c, memo, di = q.popleft()
        # 기존 방문 여부 확인
        if (r, c, memo, di) in visited:
            continue
        else : visited.add((r, c, memo,di))
      
        # 현재 명령어 처리
        curr = coms[r][c]
        if curr == '@' :
            return True
        elif curr == '.' : pass
        elif curr in change_di.keys() : # 방향키 명령어 처리
            di = change_di[curr]
        elif curr == '_' :
            if memo == 0 : di = (0,1)
            else : di = (0,-1)
        elif curr == '|' :
            if memo == 0 : di = (1,0)
            else : di = (-1,0)
        elif curr == '-' :
            if memo == 0:
                memo = 15
            else : memo -= 1
        elif curr == '+' :
            if memo == 15:
                memo = 0
            else : memo += 1
        elif curr.isdigit():
            memo = int(curr)
        elif curr== "?":
            for d in direction:
                nr, nc = get_next(r,c,d)
                q.append((nr,nc,memo,d))
            continue
        nr,nc = get_next(r,c,di)
        q.append((nr,nc,memo,di))
    return False

for test_case in range(1, T + 1):
    R, C = map(int, input().split())
    coms = [input() for _ in range(R)]
    change_di = dict()
    direction = [(0,1),(0,-1), (-1,0) , (1,0)]
    change_di['>'] = direction[0]
    change_di['<'] = direction[1]
    change_di['^'] = direction[2]
    change_di['v'] = direction[3]
    q = deque()
    visited = set()

    # '@' 명령어가 있는지 확인
    has_terminate = False
    for r in range(R):
        if has_terminate : break
        for c in range(C):
            if coms[r][c] == '@':
                has_terminate = True
                break

    # '@' 명령어가 없으면 종료 불가능
    if not has_terminate:
        print('#' + str(test_case), "NO")
        continue
    q.append((0, 0, 0, (0,1))) # (r, c, memo , di)
    if execute() : print('#' + str(test_case), 'YES')
    else : print('#' + str(test_case), "NO")