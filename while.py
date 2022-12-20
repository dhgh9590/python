# while
# while의 조건문이 false가 될때까지 계속 반복됨
# break를 사용하면 while을 빠져나감 (return과 같음)
# continue를 만나게 되면 밑에 코드를 실행하지 않고 다시 위로 돌아가서 코드를 재실행함
treeHit = 0
while treeHit < 10:
    treeHit += 1  # treeHit의 값 1을 증가시킴
    print("s나무를 %d번 찍었습니다." % treeHit)
    # break / 한번만 실행되고 while을 빠져나감
    if (treeHit == 10):
        print("나무 넘어 갑니다.")
