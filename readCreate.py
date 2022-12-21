# 파일 읽고쓰기
# 새파일.txt 앞에 C:/python/새파일.txt로 절대경로 지정 가능
# open에 r은 읽기모드(파일을 읽기만 할 때 사용) / w는 Write 쓰다를 의미(파일에 내용을 쓸 때 사용) / a는 추가모드(파일의 마지막에 새로운 내용을 추가 시킬 때 사용)
# open의 마지막 인자에 encoding="UTF=8"를 사용하면 한글깨짐 해결됨
# 파일을 open하면 항상 close로 닫아줘야 함

# 쓰기
# f = open("새파일.txt", 'w', encoding="UTF=8")
# for i in range(1, 11):
#     data = "%d번째 줄입니다.\n" % i
#     f.write(data)
# f.close()

# 읽기
# readline는 한줄씩 읽어주는 함수
# f = open("새파일.txt", 'r', encoding="UTF=8")
# 여러줄 읽기1
# while True:
#     line = f.readline()
#     if not line:
#         break
#     print(line)

# 여러줄 읽기2
# strip()은 매개변수에 들어가는 값을 없에줌
# lines = f.readlines()
# for line in lines:
#     print(line.strip("\n"))

# read()는 파일의 모든것을 읽어옴
# data = f.read()
# print(data)

# f.close

# 추가
# f = open("새파일.txt", 'a', encoding="UTF=8")
# for i in range(11, 20):
#     data = "%d번째 줄입니다\n" % i
#     f.write(data)
# f.close()

# 축약
# with open("새파일.txt", 'w') as f:
#     f.write("추가")
