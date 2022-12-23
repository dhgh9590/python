# try를 사용하면 에러가 나도 프로그램이 종료되지 않음

f = open("foo.text", 'w')
try:
    4/0
except Exception as e:  # 무슨 에러가 발생할지 모르면 Exception을 사용하면 됨 / 모든 에러의 부모격 / except는 여러개의 에러 조건을 걸 수 있음
    print(e)  # 에러 내용
else:  # try값이 참이 아닌경우 실행
    print("hello")
finally:  # 오류가 발생하건 말건 상관없이 무조건 마지막에 실행함
    f.close()
