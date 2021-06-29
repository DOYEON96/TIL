### numpy 모듈을 이용해 
# - random 모듈을 이용한 난수 발생
# - random.randint(시작값, 종료값) : 시작~ 종료값 범위에 있는 정수를 임의로 발생 

import numpy as np

# print(np.random.randint(10, 20))

### 0 ~ 50 사이의 숫자를 무작위로 생성
# - 10개의 데이터.
# - 생성된 데이터는 리스트형 데이터로 저장

# alist = []
# for i in range(10):
#     alist.append(np.random.randint(1, 50))
# print(alist)

# # 위 방법을 한줄로 작성하는 방법
# alist = [np.random.randint(1, 51) for i in range(10)]
# print(alist)

# words = ["멀티캠퍼스", "티스토리", "블로그", "파이썬", "for", "프로그래밍", "반복"]
# new_words = []

# for i in words:
#     if len(i) > 3:
#         new_words.append(i)
# print(new_words)

# 한줄쓰기
# new_words=[i for i in words if len(i) > 3]
# print(new_words)

# words가 가지고 있는 단어의 길이가 4 이상인 데이터만 new_words에 리스트로 추가
# new_words = []
# words = [ [ "이중 for문", "파이썬", "프로그래밍", "스터디" ], [ "Python", "NLP", "ML", "DL" ], [ "leetCode", "BaekJoon", "HackerRank" ], [ "멀티캠퍼스", "COMPAS", "DACON", "Kaggle" ]]

# # 
# for word_lst in words:
#     for word in word_lst:
#         if len(words) > 3:
#             new_words.append(words)
# print(new_words)

### random 모듈을 이용한 리스트 값 발생
# - 기준 : 0~ 50 사이의 난수 발생
# - 1세트당 인수가 10 ~ 20 사이의 값을 갖는다.
# - 전체 세트 : 5 세트 생성

import numpy as np

# print(np.random.randint(51))
# print(np.random.randint(25, 51))
# print(np.random.randint(0, 51, 10))
# print(np.random.randint(51, size = 10))

# 요구사항: 리스트 개체를 생성하는 코드를 작성해주세요
# 리스트 개체는 총 5개의 리스트 요소를 가지고 있고 각 리스트 요소마다 10에서 20개 사의 값을 가지고 있습니다.
# 이 값은 0 ~ 50 사이의 임의의 값으로 만들어져 있습니다.
# [[0, 24, 3, ..20], [44, 14, 8, ..10], [0, 3, 12, ..13], [49, 24, 13, ..15], [0, 24, 3, ..17]]
# 문제 해결 알고리즘
# - 10~20 size 발생: random.randint(10, 21) ==> size
# - 0~50 사이값 발생: random.randint(0, 51, size=10-20)
# - 리스트 인수 5개 생성: for i range(5)

alist = []
for i in range(5):
    s = np.random.randint(10, 21)
    num = list(np.random.randint(0, 51, s))
    alist.append(num)
# print(alist)

# rd_lst=[list(np.random.randint(51,size=np.random.randint(10,21))) for i in range(5)]
# print(rd_lst)

###

### 입력된 숫자 데이터에서 최대값/ 최소값/ 합계 계산
# 1. data에 입력된 값을 기준으로 계산
# 2. 위에서 생성된 rd_lst 데이터를 이용해 계산

### 제한조건
# sum(0), max(), min() 함수 사용 금지

alist = []
for i in range(5):
    s = np.random.randint(10, 21)
    num = list(np.random.randint(0, 51, s))
    alist.append(num)

G_lst=[]
T_lst = [0, 50, 0]

for i in range(len(alist)):

    maxn = 0
    minn = 50
    sumn = 0
    for j in range(len(alist[i])):
        num = alist[i][j]
        if num > maxn:
            maxn = num
        
        if num < minn:
            minn = num

        sumn+=num
    
    if T_lst[0] < maxn:
        T_lst[0] = maxn

    if T_lst[1] > minn:
        T_lst[1] = minn
    
    T_lst[2]+=sumn

    G_lst.append([maxn,minn,sumn])

    print(f"{i+1}번 리스트 최대값 :{maxn}, 최소값 :{minn}, 합 : {sumn}")
print(G_lst)
print(T_lst)

###############################

# 파일관리·/