# 함수/클래스
class Node():
    def __init__(self):
        self.data = None
        self.link = None

def print_node(start):
    current = start
    print(current.data, end = ' ')
    while current.link != None:
        current = current.link
        print(current.data, end = ' ')
    print()
    
def insert_node(findData, insertData):
    global Memory, head, current, pre
    if findData == head.data:
        node = Node()
        node.data = insertData
        node.link = head
        head = node
        return
    current = head
    while current.link != None:
        pre = current
        current = current.link
        if current.data == findData:
            node = Node()
            node.data = insertData
            node.link = current
            pre.link = node
            return
    node = Node()
    node.data = insertData
    current.link = node

def delete_node(deleteData):
    global Memory, head, current, pre
    # 첫 노드 삭제
    if head.data == deleteData:
        current = head
        head = head.link
        del(current)
        return
    
    # 첫 노드 이외의 노드 삭제
    current = head
    while current.link != None:
        pre = current
        current = current.link
        if current.data == deleteData:
            pre.link = current.link
            del(current)
            return
    

# 전역
Memory = []
head, current, pre = None, None, None

data_array = ['다현', '정연', '쯔위', '사나', '지효']


# 메인
## 첫번째 노드 생성
node = Node()
node.data = data_array[0]
head = node
Memory.append(node)

## 나머지 노드 생성
for data in data_array[1:]:
    pre = node
    node = Node()
    node.data = data
    pre.link = node
    Memory.append(node)

print_node(head)
insert_node('다현', '화사')
print_node(head)
insert_node('사나', '솔라')
print_node(head)
insert_node('ㅇ', '문별')
print_node(head)
delete_node('화사')
print_node(head)