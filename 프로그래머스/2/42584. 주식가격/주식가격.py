from collections import deque

def solution(prices):
    answer = []
    q = deque(prices)
    while q:
        time = 0
        price = q.popleft()
        for p in q:
            time+=1
            if price > p:
                break
        answer.append(time)
    return answer