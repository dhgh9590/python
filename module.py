# 모듈은 함수를 다른곳에서도 사용하기 위함
# mod1.py 라는 파일 안에는 아래의 add 함수가 있음
def add(a, b):
    return a + b

# add함수를 사용하고 싶은 파일에서
# import mod1을 임포트 해주고
# print(add(1,3))을 사용할 수 있음
# mod1.py파일에 함수가 여러개라면 import 하는 방식이 다름 / from mod1 import add를 사용하면 해당 파일에서 특정 함수만 임포트함
# mod1.py이 같은 경로에 있을 경우만 위에 임포트 방식이 가능
# mod1.py가 다른 경로에 있다면 import sys /줄바꿈/ sys.path.append("경로") /줄바꿈/ import mod1을 해주면 됨

# 패키지는 모듈을 모아놓은것
# 임포트1 / import game.sound.echo / 경로를 .으로 구분
# 임포트2 / from game.sound import echo
# 임포트3 / from game.sound import * / *는 모든것을 가지고옴
# ..sound.echo의 ..은 이전 경로를 뜻함
