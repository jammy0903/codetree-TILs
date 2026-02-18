


N = int(input())
cmd = []
for i in range(N):
    cmd.append(input())
    
    
stack = []
for i in range(N):
    if cmd[i].startswith('push'):
        tmp=cmd[i].split()
        stack.append(int(tmp[1]))
    elif cmd[i] == 'pop':
        if len(stack) == 0 :
            print(-1)
        else:
            print(stack[-1])
            stack.pop()
    elif cmd[i] == 'size':
        print(len(stack))
    elif cmd[i] == 'empty':
        if len(stack) == 0 :
            print(1)
        else:
            print(0)
    elif cmd[i] == 'top':
        if len(stack) == 0 :
            print(-1)
        else:
            print(stack[-1])
            
            

