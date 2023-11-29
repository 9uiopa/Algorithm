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


# stack 이용 -> O(n) :
def solution2(prices):
    stack = []
    answer = [0] * len(prices)
    for i in range(len(prices)):
        if stack != []:
            while stack != [] and stack[-1][1] > prices[i]:
                past, _ = stack.pop()
                answer[past] = i - past
        stack.append([i, prices[i]])
    for i, s in stack:
        answer[i] = len(prices) - 1 - i
    return answer
