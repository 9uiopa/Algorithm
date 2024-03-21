from itertools import permutations

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n): # 소수 판단 : 1과 자기자신을 제외한 수로 나눠보기
        if n % i == 0:
            return False
    return True

def solution(numbers):
    answer = 0
    num_list = list(numbers)
    prime_set = set()
    
    # 가능한 모든 순열 생성
    for i in range(1, len(num_list) + 1): # 순열 길이 : 1부터 len(number)까지
        perm = permutations(num_list, i) # perm : 가능한 순열의 집합
        for p in perm:
            num = int(''.join(p)) # 순열 -> int (또한 [0,1,1]도 11이 된다)
            if num in prime_set:  # 이미 확인한 숫자인 경우 스킵
                continue
            if is_prime(num):
                prime_set.add(num)
                answer += 1

    return answer