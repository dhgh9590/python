# for
# for i in num은 num(리스트)의 갯수만큼 반복하고 num의 값을 i로 하나씩 뺌
# break를 사용하면 while을 빠져나감 (return과 같음)
# continue를 만나게 되면 밑에 코드를 실행하지 않고 다시 위로 돌아가서 코드를 재실행함

# 기본적인 for문
# num = [1, 2, 3]
# for i in num:
#     print(i)

# 리스트의 2개의 값을 출력 하는 방법
# a = [(1, 2), (3, 4), (5, 6)]
# for (first, last) in a:
#     print(first, last)

# 리스트의 값을 조건문으로 거르기
# marks = [90, 25, 67, 45, 80]
# number = 0
# for mark in marks:
#     number += 1
#     if (mark >= 60):  # mark는 marks리스트의 값이 하나씩 담김
#         print("%d번 학생은 합격 입니다." % number)
#     else:
#         print("%d번 학생은 불합격 입니다." % number)

# 숫자만큼 반복
# sum = 0
# for i in range(1, 11):  # range는 x부터 y미만 까지 반복
#     sum += i
# print(sum)

# 이중 for문
# for i in range(2, 10):
#     for j in range(1, 10):
#         print(i*j, end="")  # end는 print의 옵션 / end를 사용하면 다음줄로 넘어가지 않고 이어서 써짐
#     print('')  # 줄넘기기를 위해 사용
