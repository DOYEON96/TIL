import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
# from matplotlib import font_manager as fm
from matplotlib import rc # 차트 전체 내역 관리

# plt.plot([10, 20, 30, 40])
# plt.show()

####
# x = [1,2,3,4,5]
# y = [22, 13, 15, 48, 16]

# plt.plot(x, y)
# plt.show()

####

# plt.plot([33, 12, 22, 9, 45], label = "abc", color="skyblue", marker='o') # 1번 차트
# plt.plot([50, 40, 30, 20, 10], 'pink', label = "cba", marker='*') # 2번 차트

# plt.title("plotting") # 차트 제목
# plt.xlabel("X-label")
# plt.ylabel("y-label")
# plt.legend()    # 범례 출력 (칼럼명)

# plt.show()

###########

# plt 차트에서 한글 사용하는 방법(차트 전체 적용)

# font_path="C:/Windows/Fonts/malgun.ttf" # 사용할 한글 폰트 경로
# font_name=fm.FontProperties(fname=font_path).get_name() # 폰트 속성 변경
# plt.rc('font', family=font_name)

# plt.plot([33, 12, 22, 9, 45], label = "abc", color="skyblue", marker='o', linestyle="--") # 1번 차트

# plt.title("차트 그리기 실습") # 차트 제목
# plt.xlabel("X-label")
# plt.ylabel("y-label")
# plt.legend()    # 범례 출력 (칼럼명)

# plt.show()

# 2 각 label에 폰트를 직접 적용하는 방법

# font_path="C:/Windows/Fonts/malgun.ttf" # 사용할 한글 폰트 경로
# font_name=fm.FontProperties(fname=font_path, size = 18) # 폰트 속성 변경
# font_name2=fm.FontProperties(fname=font_path, size = 13) # 폰트 속성 변경

# plt.plot([33, 12, 22, 9, 45], label = "abc", color="skyblue", marker='o', linestyle="--") # 1번 차트

# plt.title("차트 그리기 실습", fontproperties=font_name) # 차트 제목에 바로 폰트 적용
# plt.xlabel("X-label", fontproperties=font_name2)
# plt.ylabel("y-label")
# plt.legend()    # 범례 출력 (칼럼명)

# plt.show()

