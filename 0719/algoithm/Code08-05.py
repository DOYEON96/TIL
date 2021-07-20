# 함수/클래스
class TreeNode():
    def __init__(self):
        self.left = None
        self.right = None
        self.data = None


# 전역변수
memory = []
root = None
name_array = ['블랙핑크', '레드벨벳', '마마무', '에이핑크', '걸스데이', '트와이스']

# 메인
# 루트노드 생성
node = TreeNode()
node.data = name_array[0]
root = node
memory.append(node)

# 두번째 이후 노드 생성
for name in name_array[1:]:
    node = TreeNode()
    node.data = name

    current = root
    while True:
        if name  < current.data:
            if current.left == None:
                current.left = node
                break
            current = current.left
        else:
            if current.right == None:
                current.right = node
                break
            current = current.right
        memory.append(node)
print('이진 탐색 트리 완료')

findName = '마마무'
current = root
while True:
    if findName == current.data:
        print('찾았습니다.')
        break
    if findName < current.data:
        if current.left == None:
            print('데이터가 없습니다.')
            break
        current = current.left
    else:
        if current.right==None:
            print('데이터가 없습니다.')
            break
        current = current.right