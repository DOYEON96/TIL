# 함수/클래스
class Node:
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

def addNode(addData):
    global Memory, head, current, pre
    if len(Memory) == 0:
        node = Node()
        node.data = addData
        head = node
        Memory.append(node)
    else:
        current = head
        while current.link !=None:
            current = current.link
        node = Node()
        node.data = addData
        current.link = node
        Memory.append(node)

def insertNode(findData, insertData):
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

def deleteNode(deleteData):
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

def findNode(findData):
    global Memory, head, current, pre
    current = head
    if head.data == findData:
        print(f'{findData}는 0번째에 있습니다.')
        return
    current = head
    for i in range(1, len(Memory), 1):
        pre = current
        current = current.link
        if current.data == findData:
            print(f'{findData}는{i}번째에 있습니다.')
            return

# 전역 변수
Memory = []
head, current, pre = None, None, None

select = -1 # 1. 추가 2. 삽입 3. 삭제 4. 찾기 5. 종료

# 메인

while (select != 5):
    select = input('원하는 함수를 입력해주세요 (1. 추가 2. 삽입 3. 삭제 4. 찾기 5. 종료) : ')
    if int(select) == 1:
        adddata = input('추가할 데이터 입력 : ')
        addNode(adddata)
        print_node(head)
    elif int(select) == 2:
        findData = input('추가할 데이터 위치 입력 : ')
        insertData = input('추가할 데이터 입력 : ')
        insertNode(findData, insertData)
        print_node(head)
    elif int(select) == 3:
        deleteData = input('추가할 데이터 위치 입력 : ')
        deleteNode(deleteData)
        print_node(head)
    elif int(select) == 4:
        findData = input('찾을 데이터 입력 : ')
        findNode(findData)
    elif int(select) == 5:
        print_node(head)
        exit()
    else:
        pass
