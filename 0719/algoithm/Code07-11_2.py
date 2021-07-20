## 함수
def isQueueFull() :
    global SIZE, queue, front, rear
    if ( (rear+1)%SIZE == front) :
        return True
    else :
        return False

def enQueue(data) :
    global SIZE, queue, front, rear
    if (isQueueFull()) :
        print('큐 꽉!')
        return
    rear = (rear + 1) % SIZE
    queue[rear] = data

def isQueueEmpty() :
    global SIZE, queue, front, rear
    if (front == rear) :
        return True
    else :
        return False

def deQueue() :
    global SIZE, queue, front, rear
    if (isQueueEmpty()) :
        print('큐 텅!')
        return None
    front = (front + 1) % SIZE
    data = queue[front]
    queue[front] = None
    return data

## 전역
SIZE = 5
queue = [ None for _ in range(SIZE)]
front, rear = -1, -1

## 메인

enQueue('값1');enQueue('값2');enQueue('값3')
enQueue('값4')
print('출구<--', queue, '<--입구')
enQueue('값5')
print('출구<--', queue, '<--입구')
deQueue(); deQueue()
print('출구<--', queue, '<--입구')
enQueue('새값1')
print('출구<--', queue, '<--입구')
enQueue('새값2')
print('출구<--', queue, '<--입구')
enQueue('새값3')
print('출구<--', queue, '<--입구')
deQueue(); deQueue();deQueue(); deQueue()
print('출구<--', queue, '<--입구')
deQueue()