# 함수
def findMinIndex(ary):
    minIdx=0
    for i in range(1, len(ary)):
        if ary[minIdx] > ary[i]:
            minIdx = i
    return minIdx

# 전역
import random
before = [random.randint(50, 200) for _ in range(10)]
after = []



# 메인
print('정렬전 : ', before)


for i in range(len(before)):
    minPos = findMinIndex(before)
    after.append(before[minPos])
    del(before[minPos])

print('정렬후 : ', after)