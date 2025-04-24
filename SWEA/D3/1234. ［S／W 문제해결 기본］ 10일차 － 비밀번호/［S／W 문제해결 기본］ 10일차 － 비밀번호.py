for test_case in range(1, 11):
    n, s = input().split()
    stk = []
    for num in s:
        if stk and stk[-1] == num:
            stk.pop()
            continue
        stk.append(num)
    print("#" + str(test_case) + " " + "".join(stk))
    