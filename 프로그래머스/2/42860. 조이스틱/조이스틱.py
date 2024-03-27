# 통과 되는 코드
# 매 이동마다 가능한 총 좌우이동값 3가지 중에 최소값을 구한다.
def solution(name):
    answer = 0
    name = list(name)
    min_move = len(name) - 1
    for i in range(len(name)):
		    # 상하 방향 이동 값은 어차피 고정이므로 for문 돌면서 다 합한다.
        answer += min(ord(name[i]) - ord('A') , ord('Z') - ord(name[i]) + 1)
        next_d = i + 1 #index
        while next_d < len(name) and name[next_d] == 'A': # A인 칸은 건드릴 필요 없으니 index+=1
            next_d += 1
        # min_move는 좌우 방향의 총 이동량임. 이 값이 최소가 되어야 결과값도 최소임. 총 세가지 경우 중에서 최솟값을 결정
        # 기존 min_move 값 vs '현재 인덱스에서 역순으로 되돌아가서 맨 뒤부터 처리할 때'
        min_move = min(min_move, i + i + len(name) - next_d, (len(name)-next_d) * 2 + i) # 현재까지 순서대로 처리한 move + 그만큼 되돌아가기 + 뒤에서부터의 거리
        # 윗줄의 결과 vs '처음부터 왼쪽으로 가서 맨뒤부터 역순으로 진행하던걸 다시 정순으로 되돌려 맨 앞부터 처리할 때'
        # 현재까지 역순으로 처리한 move + 되돌아가기 + 앞에서부터의 거리
    
    answer += min_move
        
    return answer