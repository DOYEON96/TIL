# 함수
def isqueuefull():
    global SIZE, queue, front, rear
    if rear == SIZE -1:
        return True
    else:
        return False

def enqueue(data):
    global SIZE, queue, front, rear
    if isqueuefull():
        print('큐가 가득찼습니다.')
        return
    rear +=1
    queue[rear] = data

def isqueueempty():
    global SIZE, queue, front, rear
    if rear != SIZE-1:
        return False
    elif (rear == SIZE-1) and (front == -1):
        return True
    else:
        for i in range(front+1, SIZE, 1):
            queue[i-1] = queue[i]
            queue[i] = None
        front -=1
        rear -=1
        return False

def dequeue():
    global SIZE, queue, front, rear
    if isqueueempty():
        print('큐가 비었습니다.')
        return
    front += 1
    print(f'{queue[front]} 추출')
    queue[front] = None
    


# 전역변수
SIZE = 5
queue = [None for _ in range(SIZE)]
front, rear = -1, -1

# 메인