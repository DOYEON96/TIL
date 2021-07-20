# 함수
def binarySearch(data, fData):
    pos = -1
    start = 0
    end = len(data) -1
    while start <= end:
        mid = (start+end) // 2
        if(data[mid] == fData):
            return mid
        elif(data[mid] < fData):
            start = mid + 1
        else:
            end = mid - 1



    return pos

# 전역변수
dataAry = [50, 60, 105, 120, 150, 160, 162, 168, 177, 180]
findData = 162


# 메인
print('배열 : ', dataAry)
position = binarySearch(dataAry, findData)
if position == -1:
    print('없습니다.')
else:
    print(findData, '는', position, '위치에 있습니다')