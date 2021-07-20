# 함수


# 전역변수
SIZE = 5
queue = [None for _ in range(SIZE)]
front, rear = -1, -1


# 메인

# enqueue (삽입)

rear += 1
queue[rear] = '화사'
rear += 1
queue[rear] = '솔라'
print('출구 : ', queue, ': 입구')

# dequeue (추출)
front += 1
retData = queue[front]
queue[front] = None
print('출구 : ', queue, ': 입구')

