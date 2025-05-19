T = int(input())

def get_factor(num): # 인수 구하기
    factors = []
    for i in range(2, int(num**(0.5))+1):
        if num % i == 0 and num != i and can_make(i) : # i가 인수이고 문자열로 만들 수 있을때.  
            small = i
            big = num // i
            factors.append((small,big))
    return factors
          
def dfs(small, big):
    global ans
    flag = can_make(big)
    result = float('inf')

    if flag:
        result = len(str(small)) + 1 + flag
        if small * big == x:
            ans = min(ans, result)
        return result
    else:
        for s, b in get_factor(big):
            temp = dfs(s, b)
            if temp:
                result = len(str(small)) + 1 + temp
                if small * big == x:
                    ans = min(ans, result)
    return result if result != float('inf') else 0

def can_make(num):  # 문자열 합치기로 만들 수 있는지 판단, 가능하면 문자열크기 반환
    s = str(num)
    temp = 0
    for c in s:
        if int(c) in nums : temp+=1
    if temp == len(s) : 
        return temp
    return 0
    
for test_case in range(1, T + 1):
    idx = list(map(int, input().split()))
    nums = []
    for i in range(0,10):
        if idx[i] : nums.append(i)    
    x = int(input())
    ans = float('inf')

    # x를 문자열로 바로 만들수 있는지 확인. 
    if can_make(x):
        ans = can_make(x) +1
        print(f"#{test_case} {ans}")
        continue
            
    # 인수 찾기 + 횟수찾기
    factors = get_factor(x)
    for small, big in factors:
        dfs(small, big)
    if ans == float('inf'):
        ans = -1
    else : ans+=1 # 마지막 =
    print(f"#{test_case} {ans}")
    