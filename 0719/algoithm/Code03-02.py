def add_data(friend):
    katok.append(None)
    klen = len(katok)
    katok[klen - 1] = friend

def insert_data(pos, friend):
    katok.append(None)
    klen = len(katok)
    for i in range(klen-1, pos, -1):
        katok[i] = katok[i-1]
        katok[i-1] = None
    katok[pos] = friend

def delete_data(pos):
    klen = len(katok)
    katok[pos] = None
    for i in range(pos+1, klen):
        katok[i-1] = katok[i]
        katok[i] = None
    del(katok[klen-1])

# 전역 변수
katok = []


# 코드
add_data('다현')
add_data('정연')
add_data('쯔위')
add_data('사나')
add_data('정연')
add_data('모모')

print(katok)

insert_data(3, '미나')
print(katok)

delete_data(4)
print(katok)