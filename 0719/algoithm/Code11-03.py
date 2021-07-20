# 함수
def selectionSort(ary):
    n = len(ary)
    for i in range(n-1):
        minIdx=i
        for j in range(i+1, len(ary)):
            if ary[minIdx] > ary[j]:
                minIdx = j
        ary[i], ary[minIdx] = ary[minIdx], ary[i]
    return ary



# 전역
import random
dataAry = [random.randint(50, 200) for _ in range(10)]


# 메인

print('정렬 전 : ', dataAry)

dataAry = selectionSort(dataAry)

print('정렬 후 : ', dataAry)