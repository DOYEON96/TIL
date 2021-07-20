# 함수
def isqueuefull():
    global SIZE, queue, front, rear
    if (rear+1) % SIZE == front:
        return True
    else:
        return False

def enqueue(data):
    global SIZE, queue, front, rear
    if isqueuefull():
        print('큐가 가득찼습니다.')
        return
    rear = (rear+1) % SIZE
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
    front = (front + 1) % SIZE
    print(f'{queue[front]} 추출')
    data = queue[front]
    queue[front] = None
    return data
    


# 전역변수
SIZE = 5
queue = [None for _ in range(SIZE)]
front, rear = -1, -1

# 메인
enqueue('화사')
print(queue)
enqueue('솔라')
print(queue)
enqueue('문별')
print(queue)
enqueue('휘인')
print(queue)
enqueue('화사')
print(queue)
enqueue('솔라')
print(queue)
