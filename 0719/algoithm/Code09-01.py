class Graph():
    def __init__(self, size):
        self.Size = size
        self.graph = [ [0 for _ in range(size)] for _ in range(size)]


# 전역 변수


G1 = Graph(4)
G2 = Graph(4)

# 메인
G1.graph[0][1] = 1
G1.graph[0][2] = 1
G1.graph[0][3] = 1
G1.graph[1][0] = 1
G1.graph[1][2] = 1
G1.graph[1][3] = 1
G1.graph[2][0] = 1
G1.graph[2][1] = 1
G1.graph[2][3] = 1
G1.graph[3][0] = 1
G1.graph[3][1] = 1
G1.graph[3][2] = 1

G2.graph[0][1] = 1
G2.graph[1][0] = 1
G2.graph[1][3] = 1
G2.graph[3][1] = 1
G2.graph[3][2] = 1
G2.graph[2][3] = 1

for i in range(4):
    for j in range(4):
        print(G2.graph[i][j], end= ' ')
    print()
