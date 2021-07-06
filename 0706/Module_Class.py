class Cal_cls():
    def sum(a, b, c, d):
        print(a + b + c + d)

class Cal():

    def __init__(self):  #생성자
        self.result = 0  # Cal 클래스의 속성

    def add(self, num1): # 메소드
        self.result = self.result + num1
        return self.result

    def sub(self, num1): # 메소드
        self.result = self.result - num1
        return self.result
        
    def mul(self, num1): # 메소드
        self.result = self.result * num1
        return self.result

    def Div(self, num1): # 메소드
        self.result = self.result / num1
        return self.result


if __name__ == '__main__': 
    aa = Cal()
    print(aa.result)

    ab = Cal()
    aa.add(10)
    print(aa.result)
    print(ab.result)