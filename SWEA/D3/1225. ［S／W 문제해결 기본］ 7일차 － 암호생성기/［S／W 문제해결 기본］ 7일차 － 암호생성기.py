from collections import deque

for test_case in range(1, 11):
    t = int(input())
    q = deque(list(map(int, input().split())))
    while q[-1] != 0:
        for i in range(1,6):
            num = q.popleft()
            n = num - i
            q.append(n)
            if n<= 0 : 
                q.pop()
                q.append(0)
                break
    ans = " ".join(map(str, q))
    print("#" + str(t)+" "+ ans )
    
       
    
