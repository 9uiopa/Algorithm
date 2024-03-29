import heapq

def solution(jobs):
    answer, now, i = 0, 0, 0 # now : 현재 시각
    start = -1 
    heap = []
    
    # while(heap) 에서 시간 조건 추가됨
    while i < len(jobs): # 처리된 작업 수가 전체 작업 수보다 작을 때 반복
        # 현재 시점에서 처리할 수 있는 작업을 heap에 저장
        for j in jobs:
            if start < j[0] <= now: # 0번 : 요청 시점, 요청한 이후에 작업 가능하니까.
                heapq.heappush(heap, [j[1], j[0]]) # 소요시간(cost), 요청시점
        
        if len(heap) > 0: # 처리할 작업이 있는 경우
            cur = heapq.heappop(heap)
            start = now
            now += cur[0]
            answer += now - cur[1] # 작업 요청시간부터 종료시간까지의 시간 계산
            i +=1 # 처리된 작업 표시용
        else: # 처리할 작업이 없는 경우 다음 시간을 넘어감
            now += 1
                
    return answer // len(jobs)
