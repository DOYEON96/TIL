import matplotlib.pyplot as plt
import numpy as np

data_lst = list(np.random.randint(10, 50, 10))
data_lst2 = list(np.random.randint(10, 50, 10))

# fig = plt.figure()

# print(data_lst)
# print(data_lst2)

### 여러개 차트 한 화면에 출력(두 개의 행으로 출력)
# ax1 = fig.add_subplot(2, 1, 1)  # subplot의 파라미터 (행, 열, 순서)
# ax2 = fig.add_subplot(2, 1, 2)

# ax1.plot(data_lst, 'k')
# ax2.plot(data_lst2, 'r')

# plt.show()

### 여러개 차트 한 화면에 출력(두 개의 열로 출력)
# fig=plt.figure(figsize=(12,6))

# ax1 = fig.add_subplot(3, 2, 1)
# ax2 = fig.add_subplot(3, 2, 2)
# ax3 = fig.add_subplot(3, 1, 2)
# ax4 = fig.add_subplot(3, 3, 7)
# ax5 = fig.add_subplot(3, 3, 8)
# ax5 = fig.add_subplot(3, 3, 9)

# ax1.plot(data_lst, 'k')
# ax2.plot(data_lst2, 'r')
# ax3.plot(data_lst)
# ax4.pie(data_lst2)

# plt.show()

# 다른 방법

# fig = plt.figure()

fig, ax_lst = plt.subplots(2, 2)

ax_lst[0][0].plot(data_lst)
ax_lst[1][1].plot(data_lst2)

plt.show()