# 함수
def push(data):
    global SIZE, stack, top
    if stackisfull() == True:
        print('스택이 가득찼습니다.')
        return
    top += 1
    stack[top] = data
    
def stackisfull():
    global SIZE, stack, top
    if top >= SIZE-1:
        return True
    else:
        return False

def pop():
    global SIZE, stack, top
    if stackisempty() == True:
        print('스택이 비어있습니다.')
        return
    print(f'{stack[top]}추출')
    stack[top] = None
    top-=1
    
def stackisempty():
    global SIZE, stack, top
    if top == -1:
        return True    
    else:
        return False

def peek():
    global SIZE, stack, top
    if stackisempty() == True:
        print('스택이 비어있습니다.')
        return
    print(f'현재 top데이터는 {stack[top]}입니다.')
    

# 전역변수
SIZE = int(input('스택 크기를 입력해주세요 : '))
stack = [None for _ in range(SIZE)]
top = -1
select = -1


# 메인
while(select != 'X' or select != 'X'):
    select = input('I(삽입), E(추출), V(확인), X(종료) : ')
    if select == 'I' or select == 'i':
        data = input('삽입할 데이터를 입력해주세요 : ')
        push(data)
        print(stack)
    elif select == 'E' or select == 'e':
        pop()
        print(stack)
    elif select == 'V' or select == 'v':
        peek()
        print(stack)
    elif select == 'X' or select == 'x':
        exit()
    else:
        print('다시입력해주세요')
        pass