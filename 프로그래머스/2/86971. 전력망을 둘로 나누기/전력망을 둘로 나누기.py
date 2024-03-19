import sys
from collections import deque
def solution(n, wires):
    def get_diff(wires_sep): # 송전탑 개수의 차이 반환
        visited = set()
        count = 1
        q = deque()
        q.append(wires_sep[0][0])
        visited.add(wires_sep[0][0])    
        while q:
            node = q.popleft()
            for i, (a,b) in enumerate(wires_sep):
                if a == node and b not in visited:
                    q.append(b)
                    visited.add(b)
                    count+=1
                elif b == node and a not in visited:
                    q.append(a)
                    visited.add(a)
                    count+=1
        return abs(n-(count*2)) # 개수의 차이
    
    ans = sys.maxsize
    
    for i in range(len(wires)):
        wires_sep = wires[:i] + wires[i+1:]  # 전선이 하나 끊긴 상태 : wires_sep
        
        d = get_diff(wires_sep)
        ans = min(d,ans) 

    return ans

