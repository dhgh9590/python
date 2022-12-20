# x or y / x와 y 둘중에 하나만 참이면 참
# x and y / x와 y 모두 참이어야 참
# not x / x가 거짓이면 참이다(반대를 뜻함 /js !와 같음)
# if 1 in [1,2,3]: / 오른쪽의 리스트 값중 1이 있냐? 있으면 True 없으면 False와 같음
# if 1 not in [1,2,3]: / 오른쪽의 리스트 값중 1이 없냐? 없으면 True 있으면 False와 같음
# 조건문 실행값에 pass를 넣으면 그냥 지나감(js의 return과 비슷함)
# 조건문 여러개 사용하려면 elif를 사용

a = 1
b = 2
c = True

if a > b:
    pass
elif c:
    print('c')
else:
    print("false")

# 조건부 표현식(삼향연산자와 비슷함) / 성공의 조건을 먼저 작성 / else 값은 무조건 있어야 함
# message = "success" if a < b else "failure"
# print(message)
