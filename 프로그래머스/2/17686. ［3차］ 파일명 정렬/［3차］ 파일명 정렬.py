# HEAD는 사전순
# number는 숫자앞의 0무시, 
# tail은 정렬과 무관

'''
files를 for문 돌려서 (10^5? )
새 리스트에 넣는데   (index, head value, num value) 형태가 한 요소.
이 때 0012 를 12로 넣는다.

그래서 튜플 리스트 만든다음, 튜플리스트 sort.(nlogn)
거기서 얻은 인덱스 순서로 원래 files를 정렬. (n)
'''

def solution(files):
    answer = []
    t_list = []
    
    # t_list 만들기
    for i,file in enumerate(files) :
        head = ""
        num = ""
        hasnum = False
        for c in file:
            if c.isdigit():
                hasnum = True
                num+=c
            elif not c.isdigit() and not hasnum:
                head+=c
            elif not c.isdigit() and hasnum:
                break
        while num.startswith("0") and len(num)>1:
            num = num[1:]
        num = int(num)
        head = head.lower()
        t_list.append((i,head,num))
        
    # 정렬
    t_list.sort(key=lambda x:(x[1],x[2]))
    
    # 정답
    for t in t_list:
        i = t[0]
        answer.append(files[i])
          
    return answer