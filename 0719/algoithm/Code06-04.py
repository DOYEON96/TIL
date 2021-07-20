# 함수
def isStackFull():
    global SIZE, stack, top
    if (top >= SIZE-1):
        return True
    else:
        return False

def push(data):
    global SIZE, stack, top
    if (isStackFull() == True):
        print('스택 가득참')
        return
    top+=1
    stack[top] = data

def pop():
    global SIZE, stack, top
    if isStackEmpty() == True:
        print('스택에 데이터가 없습니다.')
        return None
    print(top)
    stack[top] = None
    top-=1
    return '데이터'

def isStackEmpty():
    global SIZE, stack, top
    if top == -1:
        return True
    else:
        return False

def peek():
    global SIZE, stack, top
    if isStackEmpty() == True:
        print('스택에 데이터가 없습니다.')
        return None
    return stack[top]

# 전역변수
SIZE = 5
stack = [None for _ in range(SIZE)]
top = -1


# 메인

push('커피')
push('콜라')
push('환타')
push('꿀물')
push('포카리스웨트')
print(stack)
push('게토레이')
print(stack)
pop()
pop()
print(stack)
pop()
pop()
print(stack)
pop()
pop()
pop()
print(stack)
peek()