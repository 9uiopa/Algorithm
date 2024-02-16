def solution(nums):
    pok = set()
    max = len(nums)/2
    for num in nums:
        pok.add(num)
    answer = len(pok)
    
    if answer > max:
        answer = max
    return answer