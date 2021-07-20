stack = [None, None, None, None, None]

top = -1

top += 1
stack[top] = '커피'
top += 1
stack[top] = '녹차'

data = stack[top]
stack[top] = None
top -= 1
print('추출-->', data)