# 매개변수 자리에 *args를 사용하면 매개변수에 몇개가 들어오든 다 사용가능
# 매개변수 자리에 **kwargs를 사용하면 딕셔너리 형태로 여러개의 값으로 들어오는것을 처리할 수 있음
# 매개변수에 True를 사용하면 호출시 인자를 안넘겨도 True 구분함 / 인자값으로 False를 넘기면 False로 구분됨 / 기본값을 설정하면 순서는 맨 끝으로 가야함 /  (man=True)
# return값에 ,로 구분하면 튜플형태로 반환함 / return a+b,a*b
# 함수 호출시 인자를 줄때 인자 순서를 변경하려면 매개변수 이름을 같이 적어줘야 함 / 1,2 -> a=1,b=2
# global a를 사용하게되면 지역변수도 글로벌변수에 접근할 수 있음
# lambda 함수 축약 / add = lambda a,b : a+b

# 사용자 정의 일반 함수
# def sum(a, b):  # 매개변수는 입력값
#     result = a + b  # 실행값
#     return result  # 출력값
# print(sum(1, 2))

# 입력함수
# number = input("숫자를 입력해주세요")
# print(number)
