# 알고리즘

## 스택 자료구조

- 먼저 들어온 데이터가 나중에 나가는 형식(선입후출)의 자료구조.
- 입구와 출구가 동일한 형태로 스택을 시각화할 수 있다. (박스 쌓기)



### 스택 구현 예제(python)

```python
stack = []
stack.append(5)
stack.append(2)
stack.append(3)
stack.append(7)
stack.pop()
stack.append(1)
stack.append(4)
stack.pop()

print(stack[::-1]) # 최상단 원소부터 출력
print(stack) # 최하단 원소부터 출력

[1, 3, 2, 5]
[5, 2, 3, 1]
```



## 큐 자료구조

- 먼저 들어온 데이터가 먼저 나가는 형식(선입선출)의 자료구조.
- 큐는 입구와 출구가 모두 뚫려있는 터널과 같은 형태로 시각화 할 수 있다.

```python
from collections import deque
# queue 구현을 위해 deque 라이브러리 사용
queue = deque()

queue.append(5)
queue.append(2)
queue.append(3)
queue.append(7)
queue.popleft()
queue.append(1)
queue.append(4)
queue.popleft()

print(queue) # 먼저들어온 순서대로 출력
queue.reverse() # 역순으로 변경
print(queue) # 나중에 들어온 원소부터 출력

deque([3, 7, 1, 4])
deque([4, 1, 7, 3])
```



### 우선순위 큐(Priority Queue)

- 우선순위 큐는 우선순위가 가장 높은 데이터를 가장 먼저 삭제하는 자료구조입니다.
- 우선수위 큐는 데이터를 우선순위에 따라 처리하고 싶을 때 사용합니다.
  - 예시) 물건 데이터를 자료구조에 넣었다가 가치가 높은 물건부터 꺼내서 확인해야 하는 경우

| 자료구조    |       추출되는데이터        |
| ----------- | :-------------------------: |
| 스택        |  가장 나중에 삽입된 데이터  |
| 큐          |   가장 먼저 삽입된 데이터   |
| 우선순위 큐 | 가장 우선순위가 높은 데이터 |

- 우선순위 큐를 구현하는 방법
  - 단순히 리스트를 이용하여 구현
  - 힙(heap)을 이용하여 구현
- 데이터의 개수가 n개일 때, 구현 방식에 따라서 시간 복잡도를 비교한 내용

| 우선순위 큐 구현 방식 | 삽입시간 | 삭제시간 |
| --------------------- | -------- | -------- |
| 리스트                | O(1)     | O(N)     |
| 힙(heap)              | O(logN)  | O(logN)  |

- 단순히 n개의 데이터를 힙에 넣었다가 모두 꺼내는 작업은 정렬과 동일(힙 정렬)
  - 이 경우 시간 복잡도는 O(NlogN)입니다.

### 힙(heap)의 특징

- 힙은 완전 이진 트리 자료구조의 일종
- 힙에서는 항상 루트노드를 제거
- 최소힙
  - 루트 노드가 가장 작은 값을 가짐
  - 값이 작은 데이터가 가장 우선적으로 제거
- 최대힙
  - 루트 노드가 가장 큰 값을 가집니다.
  - 따라서 값이 큰 데이터가 우선적으로 제거



### 완전 이진 트리(Complete Binary Tree)

- 완전 이진 트리란 루트  노드부터 시작하여 왼쪽 자식노드, 오른쪽 자식노드 순으로 데이터가 차례대로 삽입되는 트리.

### 

### 최소 힙 구성 함수: Min-Heapify()

- (상향식) 부모 노드로 거슬러 올라가며, 부모보다 자신의 값이 더 작은 경우에 위치를 교체합니다.



### 힙에 새로운 원소가 삽입될 때

- 새로운 원소가 삽입 되었을 때 O(logN)의 시간복잡도로 힙 성질을 유지할 수 있도록 할 수 있습니다.



###  힙에서 원소가 제거될 때

- 원소가 제거되었을 때 O(logN)의 시간 복잡도로 힙 성질을 유지하도록 할 수 있다.
  - 이후에 루트 노드에서부터 하향식으로 Heapify()를 진행한다.



### 우선순위 큐 라이브러리를 활용한 힙 정렬 구현 예제(python)

```python
import sys
import headq # 파이썬 heap 라이브러리는 default 최소힙
input = sys.stdin.readline

def heapsort(iterable):
    h=[]
    result=[]
    # 모든 원소를 차례대로 힙에 삽입
    for value in iterable:
        headq.heappush(h, value)
    # 힙에 삽입된 모든 원소를 차례대로 꺼내어 담기
    for i in range(len(h)):
        result.append(headq.heappop(h))
    return result

n = int(input())
arr = []

for i in range(n):
    arr.append(int(input()))
    
res = heapsort(arr)

for i in range(n):
    print(res[i])
```



## 트리 (Tree)

- 트리는 가계도와 같은 계층적인 구조를 표현할 때 사용할 수 있는 자료구조입니다.
- 트리 관련용어
  - 루트 노드 : 부모가 없는 최상위 노드
  - 단말 노드 : 자식이 없는 노드
  - 크기 : 트리에 포함된 모든 노드의 개수
  - 높이 : 깊이 중 최대값
  - 차수 : 각 노드의 간선(자식방향) 개수
- 기본적으로 트리의 크기가 N일 때, 간선의 개수는 N-1개입니다.



### 이진 탐색 트리 (Binary Search Tree)

- 이진 탐색이 동작할 수 있도록 고안된 효율적인 탐색이 가능한 자료구조의 일종입니다.
- 이진탐색 트리의 특징 : 왼쪽 자식노드 < 부모노드 < 오른쪽 자식노드
  - 부모 노드보다 왼쪽자식 노드가 작다.
  - 부모 노드보다 오른쪽자식 노드가 크다.



###  트리의 순회 (Tree Traversal)

- 트리 자료구조에 포함된 노드를 특정한 방법으로 한 번씩 방문하는 방법을 의미합니다.
  - 트리의 정보를 시각적으로 확인할 수 있습니다.

- 대표적인 트리 순회의 방법
  - 전위 순회(pre-order traverse) : 루트를 먼저 방문
  - 중위 순회(in-order traverse) : 왼쪽 자식을 방문한 뒤에 루트를 방문
  - 후위 순회(post-order traverse) : 왼쪽자식, 오른쪽 자식을 방문한 뒤에 루트를 방문

![image-20210703085912150](C:\Users\김도연\AppData\Roaming\Typora\typora-user-images\image-20210703085912150.png)



### 트리의 순회 구현 예제

```python
Class Node:
    def __init__(self, data, left_node, right_node):
        self.data = data
        self.left_node = left_node
        self.right_node = right_node
        
# 전위 순회
def pre_order(node):
    print(node.data, end=' ')
    if node.left_node != None:
        pre_order(tree[node.left_node])
    if node.right_node != None:
        pre_order(tree[node.right_node])
        
# 중위 순회
def in_order(node):
    if node.left_node != None:
        in_order(tree[node.left_node])
    print(node.data, end=' ')
    if node.right_node != None:
        in_order(tree[node.right_node])

# 후위 순회
def post_order(node):
    if node.left_node != None:
        post_order(tree[node.left_node])
    if node.right_node != None:
        post_order(tree[node.right_noe])
    print(node.data, end=' ')

n = int (input()) # 트리의 크기 지정
tree = {} # 빈 트리 선언

for i in range(n): # 트리의 크기만큼 반복하며 각 부모노드에 자식노드 삽입
    data, left_node, right_node = input().split()
    if left_node == 'None':
        left_node = None
    if right_node == 'None':
        right_node = None
    tree[data] = Node(data, left_node, right_node)

pre_order(tree['A']) # 
print()
inorder(tree['A'])
print()
post_order(tree['A'])
```



###  바이너리 인덱스 트리(Binary Indexed Tree)





## 정렬 알고리즘

- 정렬(Sorting)이란 데이터를 특정한 기준에 따라 순서대로 나열하는 것을 말합니다.
- 일반적으로 문제 상황에 따라서 적절한 정렬 알고리즘이 공식처럼 사용됨.



### 선택정렬

- 처리되지 않은 데이터 중에서 가장 작은 데이터를 선택해 맨 앞에 있는 데이터와 바꾸는 것을 반복



#### 선택정렬 소스코드(python)

```python
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(len(array)):
    min_index = i
    for j in range(i + 1, len(array)):
        if array[min_index] > array[j]:
            min_index = j
    array[i], array[min_index] = array[min_index], array[i] # 스와프 
    #array[i]와 array[min_index] 값을 스왑
    
print(array)


[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
```



####  선택정렬의 시간 복잡도

- 선택 정렬은 N번 만큼 가장 작은 수를 찾아서 맨 앞으로 보내야 합니다.
- 구현 방식에 따라서 사소한 오차는 있을 수 있지만, 전체 연산 횟수는 다음과 같습니다.
  - N + (N-1) + (N-2) + ... + 2
- 이는 (N<sup>2</sup> + N - 2) / 2로 표현할 수 있는데, 빅오 표기법에 따라서 O(N<sup>2</sup>)라고 작성합니다.



### 삽입 정렬

- 처리되지 않은 데이터를 하나씩 골라 적절한 위치에 삽입합니다.
- 선택 정렬에 비해 구현 난이도가 높은 편이지만, 일반적으로 더 효율적으로 동작합니다.



- 첫번째 데이터를 정렬이 되어있다고 가정하고 두번째 데이터가 첫번째 데이터의 왼쪽이나 오른쪽에 들어갈지 판단합니다.



#### 삽입정렬 소스코드(python)

```python
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(1, len(array)):
    for j in range( i, 0, -1): # i부터 1씩 감소하며 반복
        if array[j] < array[j-1]:	# 한 칸씩 왼쪽으로 이동
            array[j], array[j - 1] = array[j- 1], array[j]
        else: # 자신보다 작은 데이터를 만났을 때 그 위치에 멈춤
            break
            
print(array)


[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
```



####  삽입 정렬의 시간 복잡도

- 삽입 정렬의 시간 복잡도는 O(N<sup>2</sup>이며, 선택 정렬과 마찬가지로 반복문이 두 번 중첩되어 사용됩니다.)
- 삽입정렬은 현재 리스트의 데이터가 거의 정렬되어 있는 상태라면 매우 빠르게 동작합니다.
  - 최선의 경우 O(N)의 시간 복잡도를 가집니다.





### 퀵 정렬

- 기준 데이터를 설정하고 그 기준보다 큰 데이터와 작은 데이터의 위치를 바꾸는 방법
- 일반적인 상황에서 가장 많이 사용되는 정렬 알고리즘 중 하나
- 병합 정렬과 더불어 대부분의 프로그래밍 언어의 정렬 라이브러리의 근간이 되는 알고리즘
- 가장 기본적인 퀵 정렬은 첫 번째 데이터를 기준 데이터(Pivot)으로 설정합니다



- 피벗값의 왼쪽으로부터 피벗값보다 큰 수를 설정, 맨 오른쪽부터 피벗값보다 작은 값을 선택하여 값을 각각 스왑

![image-20210703114802362](C:\Users\김도연\AppData\Roaming\Typora\typora-user-images\image-20210703114802362.png)

- 첫 번째 수행 이후 다시한번 왼쪽부터 피벗값보다 큰 수, 오른쪽부터 피벗값보다 작은 수를 찾아 스왑

![image-20210703114907503](C:\Users\김도연\AppData\Roaming\Typora\typora-user-images\image-20210703114907503.png)

- 각각 작은 수, 큰 수 탐색 중 위치가 교차되었을 때, 작은 값의 위치를 **피벗**과 스왑합니다.

![image-20210703114951980](C:\Users\김도연\AppData\Roaming\Typora\typora-user-images\image-20210703114951980.png)

- 피벗의 스왑이 이루어졌을 때, 피벗의 위치기준 왼쪽은 전부 피벗값보다 작은 값으로, 오른쪽은 피벗값보다 큰 수로 나누어지게 되고, 피벗을 기준으로 나누는 작업을 **분할(Divide)**라고 합니다.

![image-20210703115341717](C:\Users\김도연\AppData\Roaming\Typora\typora-user-images\image-20210703115341717.png)

- 이후 왼쪽 묶음과, 오른쪽 묶음에서 각각 퀵정렬을 다시 실행하게 됩니다. (재귀)



#### 퀵 정렬의 시간 복잡도

- 퀵 정렬은 평균의 경우 O(NlogN)의 시간 복잡도를 가집니다.
- 하지만 최악의 경우 O(N<sup>2</sup>)의 시간 복잡도를 가집니다.



```python
array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort(array, start, end):
    if start >= end: #원소가 1개인 경우 종료
        return
    pivot = start # 피벗은 첫번째 원소
    left = start + 1
    right = end
    while(left <= right):
        # 피벗보다 큰 데이터를 찾을 때까지 반복
        while(left <= end and array[left] <= array[pivot]):
            left += 1
        # 피벗보다 작은 데이터를 찾을 때까지 반복
        while(right > start and array[right] >= array[pivot]):
            right -= 1
        if(left > right): # 교차되었을때 피벗과 작은 데이터를 교체
            array[right], array[pivot] = array[pivot], array[right]
        else: # 엇갈리지 않았다면 작은 데이터와 큰 데이터를 교체
            array[left], array[right] = array[right], array[left]
    #분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬 수행
    quick_sort(array, start, right - 1)
    quick_sort(array, right +1 , end)
    
quick_sort(array, 0, len(array) - 1)
print(array)


[0, 1, 2, 3, 4 ,5, 6, 7, 8, 9]
```



#### 퀵 정렬 소스코드 (python) 파이썬의 장점을 살린 방식

```python
array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort(array):
    # 리스트가 하나 이하의 원소만을 담고 있다면 종료
    if len(array) <= 1:
        return array
    pivot = array[0]
    tail = array[1:]
    
    left_side = [x for x in tail if x <= pivot] # 분할된 왼쪽부분
    right_side = [x for x in tail if x > pivot] # 분할된 오른쪽 부분
    
    #분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬 수행하고, 전체 리스트 반환
    return quick_sort(left_side) + [pivot] + quick_sort(right_side)

print(quick_sort(array))


[0, 1, 2, 3, 4, 5, 6, 7, 8 , 9]
```



### 계수 정렬

- 특정한 조건이 부합할 때만 사용할 수 있지만 매우 빠르게 동작하는 정렬 알고리즘
  - 계수 정렬은 데이터의 크기 범위가 제한되어 정수 형태로 표현할 수 있을 때 사용 가능
- 데이터의 개수가 N, 데이터(양수)중 최댓값이 K일 때 최악의 경우에도 수행시간 O(N + K)를 보장합니다.



#### 계수 정렬 코드

```python
# 모든 원소의 값이 0보다 크거나 같다고 가정
array = [7, 5, 9, 0, 3, 1, 6, 2, 9, 1, 4, 8, 0, 5, 2]
# 모든 범위를 포함하는 리스트 선언(모든 값은 0으로 초기화)
count = [0] * (max(array) + 1)

for i in range(len(array)):
    count[array[i]] += 1 # 각 데이터에 해당하는 인덱스의 값 증가
    
for i in range(len(count)): # 리스트에 기록된 정렬 정보 확인
    for j in range(count[i]):
        print(i, end=' ') # 띄어쓰기를 구분으로 등장한 횟수만큼 인덱스 출력
        
        
0 0 1 1 2 2 3 4 5 5 6 7 8 9 9
```



#### 계수 정렬 시간 복잡도

- 계수 정렬의 시간 복잡도와 공간 복잡도는 모두 O(N + K)입니다.
- 계수 정렬은 때에 따라서 심각한 비효율성을 초래할 수 있다.
  - ex) 데이터가 0과 999,999로 단 2개만 존재하는 경우.
- 계수 정렬은 **동일한 값을 가지는 데이터가 여러 개 등장할 때** 효과적으로 사용할 수 있다.
  - 성적의 경우 100점을 맞은 사람이 여러명일 수 있기 때문에 계수 정렬이 효과적이다.



## 정렬 알고리즘 비교

| 정렬 알고리즘 |             평균 시간 복잡도              | 공간 복잡도 |                             특징                             |
| :-----------: | :---------------------------------------: | :---------: | :----------------------------------------------------------: |
|   선택 정렬   |             O(N<sup>2</sup>)              |    O(N)     |                     아이디어가 매우 간단                     |
|   삽입 정렬   |             O(N<sup>2</sup>)              |    O(N)     |          데이터가 거의 정렬 되어있을 경우 가장 빠름          |
|    퀵 정렬    | O(NlogN)     최악의 경우 O(N<sup>2</sup>) |    O(N)     |          대부분의 경우에 가장 적합, 대체적으로 빠름          |
|   계수 정렬   |                 O(N + K)                  |  O(N + K)   | 데이터의 크기가 한정적인 경우에만 사용가능 하지만 속도가 매우 빠르다. |



## 그래프 탐색

### DFS (Depth-Fist Search)

- DFS는 **깊이 우선 탐색**이라고 부르며 그래프에서 **깊은 부분을 우선적으로 탐색하는 알고리즘**입니다.
- DFS는 **스택 자료구조(혹은 재귀 함수)**를 이용하며, 구체적인 동작 과정은 다음과 같습니다.
  1. 탐색 시작 노드를 스택에 삽입하고 방문처리.
  2. 스택의 최상단 노드에 방문하지 않은 인접한 노드가 하나라도 있으면 그 노드를 스택에 넣고 방문 처리합니다. 방문하지 않은 인접 노드가 없으면 스택에서 최상단 노드를 꺼냅니다.
  3. 더 이상 2번의 과정을 수행할 수 없을 때까지 반복합니다.



### DFS 동작예시

- 노션 DFS동작예시 부분 참고



### DFS 소스코드 예제(python)

```python
# DFS 메소드 정의
def dfs(graph, v, visited):
    # 현재 노드를 방문 처리
    visited[v] = True
    print(v, end=' ')
    # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)
# 각 노드가 연결된 정보를 표현            
graph = [
    [], # 1번부터 사용하기 위해 0번 index를 비워두고 사용
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1,7]
]

# 각 노드가 방문된 정보를 표현
visited = [False] * 9 # 0번 index를 이용하지 않기 위해 한개 더 선언

# 함수 호출
dfs(graph, 1, visited)



1 2 7 6 8 3 4 5
```



### BFS(Breadth-First Search)

- BFS는 **너비 우선 탐색**이라고도 부르며, 그래프에서 **가까운 노드부터 우선적으로 탐색하는 알고리즘**입니다.
- BFS는 **큐 자료구조**를 이용하며, 구체적인 동작 과정은 다음과 같습니다.
  1. 탐색 시작 노드를 큐에 삽입하고 방문 처리
  2. 큐에서 노드를 꺼낸 뒤에 해당 노드의 인접 노드 중에서 방문하지 않은 노드를 모두 큐에 삽입하고 방문처리.
  3. 더 이상 2번의 과정을 반복할 수 없을 때 까지 반복



#### BFS 동작 예시

- Notion BFS동작예시 참고



#### BFS 소스코드 예제(python)

```python
from collections import deque

# BFS 메소드 정의
def bfs(graph, start, visited):
    # 큐 구현을 위해 deque라이브러리 사용
    queue = deque([start])
    # 현재 노드 방문처리
    visited[start] = True
    # 큐가 빌 때까지 반복
    while queue:
        # 큐에서 하나의 원소를 뽑아 출력
        v = queue.popleft()
        print(v, end=' ')
        # 아직 방문하지 않은 인접한 원소들을 큐에 삽입
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
                
graph = [ # 각노드가 연결된 정보 표현 (2차원 리스트)
    [], # 1번부터 사용하기 위해 0번 index를 비워두고 사용
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

# 각 노드가 방문된 정보를 표현
visited = [False] * 9 # 0번 index를 이용하지 않기 위해 한개 더 선언

# 함수 호출
bfs(graph, 1, visited)



1 2 3 8 7 4 5 6
```

