# 반복적인 행동이 필요할때 사용

class Calculator:  # class의 첫글짜는 대문자
    def __init__(self):  # self는 자기자신을 뜻함 / cal1.add 중 .앞의 cal1를 뜻함
        self.result = 0  # __init__ 선언되면 제일 먼저 실행됨

    def add(self, num):
        self.result += num
        return self.result


cal1 = Calculator()

print(cal1.add(3))
print(cal1.add(4))
