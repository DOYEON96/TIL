class fun_cls:
    # 사용자 정의 함수 (just 실행함수)
    # 메소드 각각 fun_cls의 인스턴스 객체 
    def usr_fun(x, y, z=10): # 3개의 파라미터를 가지는 함수, z는10의 기본값을 가짐
        tot = x+y+z
        print(f'x={x}, y={y}, z={z}, 합계 = {tot}')

    # 사용자 정의 함수 생성(계산 결과 돌려주는 함수 return)
    def usr_fun2(x, y, z):
        
        tot = x + y + z
        p_tot=tot*10
        return tot, p_tot

# numpy.random.randint()

fun_cls.usr_fun(10, 10)
fun_cls.usr_fun(20, 20, 20)

fl = fun_cls

tot, p_tot = fl.usr_fun2(10, 10, 20)

# p_tot = fun2(10, 10, 10)
print(f'tot={tot}, p_tot={p_tot}')

