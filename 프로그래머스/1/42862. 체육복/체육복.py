def solution(n, lost, reserve):
    # 여벌의 체육복을 가져온 학생 중에 도난당한 경우를 제거
    real_lost = set(lost) - set(reserve)
    real_reserve = set(reserve) - set(lost)

    # 체육복을 빌려줄 수 있는 학생 수 계산
    for r in real_reserve:
        if r - 1 in real_lost:
            real_lost.remove(r - 1)
        elif r + 1 in real_lost:
            real_lost.remove(r + 1)

    return n - len(real_lost)