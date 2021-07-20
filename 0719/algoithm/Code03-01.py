katok = []

katok.append(None)
katok[0] = '다현'

katok.append(None)
katok[1] = '정연'

katok.append(None)
katok[2] = '쯔위'

katok.append(None)
katok[3] = '사나'

katok.append(None)
katok[4] = '지효'

katok.append('모모')

# 새로운 친구 삽입
katok.append(None)
katok[6] = katok[5]; katok[5] = None
katok[5] = katok[4]; katok[4] = None
katok[4] = katok[3]; katok[3] = None
katok[3] = '미나'

# 친구 삭제
katok[4] = None
katok[4] = katok[5]; katok[5] = None
katok[5] = katok[6]; katok[6] = None
del(katok[6])

print()