## NLTK 자연어 처리 패키지
# - 교육용으로 개발된 자연어 처리 및 문서 분석용 파이썬 패키지
# - 말뭉치 : 예제 파일 제공
# - 토큰 생성 : 문자열 단위를 토큰(TOKEN), 문자열을 토큰으로 나누는 작업
# - 형태소 분석 : 언어학에서 일정한 의미가 있는 가장 작은 말의 단위를 뜻 어근, 접두사, 접미사, 품사 등 다양한 언어적 속성을 파악하고 처리하는 작업
# - 품사 태깅 : 말을 문법적인 기능이나 형태, 뜻에 따라 구분한 것
# - NNP : 단수 고유명사 , VB : 동사, VBP : 현재형 동사
# - TO : to전치사, NN : 명사(단수형, 집합형), DT : 관형사



# text="Don't be fooled by the dark sounding name, Mr. Jone's Orphanage is as cheery as cheery goes for a pastry shop."
# # print(text)

# from nltk.tokenize import word_tokenize
# from nltk.tag import pos_tag
# import nltk

# # nltk.download()

# print(word_tokenize(text))

# print(pos_tag(word_tokenize(text)))

##############################################################


## 한글 형태소 분석 (Konlpy)
# KoNLPy는 다음과 같은 다양한 형태소 분석, 태깅 라이브러리를 파이썬에서 쉽게 사용할 수 있도록 모아놓았다.

# Hannanum: 한나눔. KAIST Semantic Web Research Center 개발.

# http://semanticweb.kaist.ac.kr/hannanum/

# Kkma: 꼬꼬마. 서울대학교 IDS(Intelligent Data Systems) 연구실 개발.

# http://kkma.snu.ac.kr/

# Komoran: 코모란. Shineware에서 개발.

# https://github.com/shin285/KOMORAN

# Mecab: 메카브. 일본어용 형태소 분석기를 한국어를 사용할 수 있도록 수정.

# https://bitbucket.org/eunjeon/mecab-ko

# Open Korean Text: 오픈 소스 한국어 분석기. 과거 트위터 형태소 분석기.

# https://github.com/open-korean-text/open-korean-text


# Konlpy에서 제공하는 대한민국 헌법 말뭉치
# from konlpy.corpus import kolaw
# import jpype
# print(kolaw.fileids())

# ko_txt = kolaw.open('constitution.txt').read()
# print(ko_txt[:100])

# text = 'down 창 회색으로 다 바뀌면 그냥 창 끄면 되나요'
# from konlpy.tag import Hannanum

# han = Hannanum()
# print(han.nouns(text))

from konlpy.tag import Kkma
kkma = Kkma()
# print(kkma.nouns('파이썬은 아예 안깔려 있어가지고요. 가상환경에만 있고 노트북에는 없어요'))


text = '''
방울토마토와 수박은 어떤 공통점이 있을까? 모두 몸에 좋은 항산화 성분이 풍부한 식품들이다. 몸의 손상과 노화를 늦추는데 도움을 준다. 또 하나, 토마토와 수박은 빨간 색이 특징이다. 이 빨간 색은 건강효과가 뛰어나다. 어떤 효과가 있을까? 방울토마토와 수박의 조합에 대해 알아보자.
빨간 색소의 정체.. 라이코펜 효과
채소와 과일의 건강효과를 말할 때 라이코펜(Lycopene)의 효과에 대해 언급하는 경우가 많다. 붉은색을 보이는 채소와 과일에 포함되어 있는 성분이다. 몸속의 염증을 막거나 완화하기 때문에 건강에 좋다. 국립암센터-국가암정보센터 암 정보를 보면 라이코펜이 풍부한 토마토와 수박 등은 전립선암과 심장병 예방에 도움을 준다. 토마토의 라이코펜은 숙성한 것에 더 많기 때문에 익혀서 먹는 게 좋다. 국립농업과학원 식품정보를 보면 국내에서 소비되고 있는 수박에는 라이코펜 성분이 100g 당 4.1 mg 들어 있어 토마토(3.2 mg)에 비해 30%정도 더 많이 함유되어 있다.
방울토마토와 수박, 혈관 건강에 도움
방울토마토와 수박의 라이코펜 등 기능성 물질은 혈액을 건강하게 해 혈관질환의 예방-관리에 도움을 준다. 혈관에 콜레스테롤이 많이 쌓이면 혈관이 좁아지는 동맥경화에 이어 심장병(협심증, 심근경색), 뇌졸중(뇌경색, 뇌출혈) 등 혈관질환으로 발전할 수 있다. 수박의 시트룰린(citrulline) 성분은 몸속에서 소화되면서 아르기닌(arginine)으로 바뀌고 산화질소를 증가시켜 딱딱해진 혈관을 부드럽게 하는 데 도움을 준다.
시원한 제철 식품 수박 먹을 때 주의할 점은?
수박은 수분 함량(91%)이 높고 탄수화물, 칼륨, 인, 마그네슘, 칼슘, 나트륨, 철분 등 각종 영양소가 많다. 몸속에서 흡수가 잘 되는 포도당과 과당이 들어 있어 폭염에 지친 피로를 푸는 데 도움을 준다. 하지만 과식은 금물이다. 특히 당뇨병 환자라면 더욱 조심해야 한다. 당지수(GI)가 72로 높은 편이어서 혈당을 빠르게 올릴 수 있다. 당지수는 음식이 소화되면서 얼마나 빠르게 혈당을 높이는지 표시한 수치다. 당지수가 높은 쌀밥, 면 등 탄수화물 음식을 먹은 후 후식으로 수박을 과식하면 건강한 사람이라도 혈당 조절에 좋지 않다.
수박과 방울토마토의 역할 교대
혈당 관리를 위해 시원한 수박을 무조건 멀리 할 수는 없다. 많이 먹지 말고 방울토마토에 ‘라이코펜 효과’를 넘겨주는 역할 교대도 고려할 만하다. 방울토마토는 당지수가 낮은 대표적인 식품이다. 토마토(당지수 30)는 포도(46) 복숭아(41) 사과(36) 키위(35)에 비해서도 당지수가 낮다. 70 이상이면 고당 지수, 55 이하를 저당 지수로 분류한다. 이런 식품들도 한 번에 너무 많이 먹지 말고 적정량 먹는 게 좋다.
오후 출출할 때 방울토마토 어때요?
출출할 때 먹는 오후 간식이 문제가 되는 경우가 있다. 식사량을 조절해도 과자, 빵 등을 간식으로 먹으면 다이어트 효과가 줄어들 수 있다. 이들 음식은 달고 탄수화물,  첨가물이 많은 것이 대부분이다. 작은 플라스틱 통에 방울토마토를 담아 휴대하면 사무실에서도 먹을 수 있다. 공복감을 달래고 혈당 관리, 다이어트에 좋은 최고의 건강식이 될 수 있다. 견과류까지 추가하면 포만감이 상당해 저녁 과식을 막을 수 있다.
'''
############################
# Okt활용
from konlpy.tag import Okt

t = Okt()
# nouns = t.nouns(text) # 명사
# print(nouns)

# morphs = t.morphs(text) # 형태소 추출
# print(morphs)

# pos = t.pos(text) # 품사 태깅
# print(pos)

#################################
# Hannanum
from konlpy.tag import Hannanum
h = Hannanum()
# nouns = nouns(h)
# print(h)

#####
from konlpy.tag import Komoran
k = Komoran()
pos = k.pos(text)
print(pos)

text = '아버지가방에들어가신다'

from konlpy.tag import Kkma
kk = Kkma()

from konlpy.tag import Okt
t = Okt()

from konlpy.tag import Hannanum
h = Hannanum()

# print(k.pos(text))
# print(h.pos(text))
# print(kk.pos(text))
# print(t.pos(text))

print(t.tagset)
print(kk.tagset)