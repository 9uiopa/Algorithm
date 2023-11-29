from collections import deque

def solution(priorities, location):
    pri = []
    answer = []
    for i in range(len(priorities)):
        pri.append((i,priorities[i]))
    
    q = deque()
    q.extend(pri)
    while q:
        valid = True
        cur_process = q.popleft()
        for p in q:
            if cur_process[1] < p[1]:
                q.append(cur_process)
                valid = False
                break
        if valid:
            answer.append(cur_process)    
    print(answer)
    for idx in range(len(answer)):
        if answer[idx][0] == location:
            print(idx+1)
            return idx+1  