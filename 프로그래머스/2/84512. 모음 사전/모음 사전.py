# 

def solution(word): # word 수 - 5*6^4 = 6500 보다 작다. 중간에 ''가 들어간 경우는 사전에 없으므로
    answer = 0
    aeiou = ['','A','E','I','O','U']
    dictionary = [] 
    for a in ['A','E','I','O','U']:
        for b in aeiou:
            if b == '':
                dictionary.append(a)
                continue
            for c in aeiou:
                if c == '':
                    dictionary.append(a+b)
                    continue
                for d in aeiou:
                    if d == '':
                        dictionary.append(a+b+c)
                        continue
                    for e in aeiou:
                        dictionary.append(a+b+c+d+e)

    return dictionary.index(word)+1