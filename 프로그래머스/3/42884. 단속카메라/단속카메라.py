from collections import deque
def solution(routes):
    answer = 0
    routes.sort(key=lambda x: x[1]) # 진출지점 기준 오름차순 정렬 - 한쪽 방향으로 풀어야 중복 안됨
    q = deque(routes)
    
    while q:
        enter, out = q.popleft()
        answer += 1
        while q and q[0][0] <= out: # 두 범위가 겹칠 조건
            q.popleft()

    return answer