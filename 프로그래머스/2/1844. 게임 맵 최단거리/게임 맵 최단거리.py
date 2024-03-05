# 최단 거리 - bfs
from collections import deque
def solution(maps):
    answer = 0
    q = deque()
    h = len(maps)
    w = len(maps[0])
    maps[0][0] += 1
    q.append((0,0))
    while q:
        r,c = q.popleft()
        if r == h-1 and c ==w-1: # 도착
            return maps[r][c]-1
        
        if r+1 < h and maps[r+1][c]==1:
            maps[r+1][c] += maps[r][c] 
            q.append((r+1,c))#하
        if c+1 < w and maps[r][c+1]==1:
            maps[r][c+1] += maps[r][c] 
            q.append((r,c+1))#우
        if r-1 >= 0 and maps[r-1][c]==1:
            maps[r-1][c] += maps[r][c] 
            q.append((r-1,c))#상
        if c-1 >= 0 and maps[r][c-1]==1:
            maps[r][c-1] += maps[r][c] 
            q.append((r,c-1))#좌
        
    return -1