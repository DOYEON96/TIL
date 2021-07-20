#함수
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


#전역
katok = []
select = -1 # 1. 추가 2. 삽입 3. 삭제 4. 종료

#메인
if __name__ == '__main__':
    while select != 4:
        select = int(input('작업을 선택해주세요(1. 추가 2. 삽입 3. 삭제 4. 종료) : '))

        if select == 1:
            friend = input('추가할 이름을 입력해주세요 : ')
            add_data(friend)
            print(katok)
        elif select == 2:
            friend = input('삽입할 이름을 입력해주세요 : ')
            pos = int(input('삽입할 위치(인덱스)를 입력해주세요 : '))
            insert_data(pos, friend)
            print(katok)
        elif select == 3:
            pos = int(input('삭제할 위치(인덱스)를 입력해주세요 : '))
            delete_data(pos)
            print(katok)
        elif select == 4:
            print(katok)
            print('작업을 종료합니다.')
            exit()
        else:
            pass

    