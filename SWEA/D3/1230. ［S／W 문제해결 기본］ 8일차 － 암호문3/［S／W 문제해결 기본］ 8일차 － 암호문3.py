for test_case in range(1, 11):
    pw_len = int(input())
    data = input().split()
    com_len = int(input())
    command = input().split()
    i = 0
    while i < len(command):
        if command[i]=='I':
            x = int(command[i+1])
            y = int(command[i+2])
            data = data[:x] + command[i+3 : i+3+y] + data[x:]
            i+=3+y
        elif command[i]=='D':
            x = int(command[i+1])
            y = int(command[i+2])
            data = data[:x] + data[x+y:]
            i+=3
        elif command[i]=='A':
            y = int(command[i+1])
            data = data + command[i+2 : i+2+y]
            i+=2+y
            
        else:
            i+=1
    print("#" + str(test_case) + " " + " ".join(data[:10]))