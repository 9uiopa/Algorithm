def solution(s):
    answer = [0,0]
    
    while s != '1':
        c = sum(list(map(int,s))) # s에 있는 1의 개수
        answer[0] += 1
        answer[1] += len(s) - c # 0의 개수
        s = format(c,'b')
        
    return answer