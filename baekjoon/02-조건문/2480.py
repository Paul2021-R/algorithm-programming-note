# 주사위 세개 성공
# 시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
# 1 초	128 MB	229322	107364	90908	46.877%
# 문제
# 1에서부터 6까지의 눈을 가진 3개의 주사위를 던져서 다음과 같은 규칙에 따라 상금을 받는 게임이 있다.

# 같은 눈이 3개가 나오면 10,000원+(같은 눈)×1,000원의 상금을 받게 된다.
# 같은 눈이 2개만 나오는 경우에는 1,000원+(같은 눈)×100원의 상금을 받게 된다.
# 모두 다른 눈이 나오는 경우에는 (그 중 가장 큰 눈)×100원의 상금을 받게 된다.
# 예를 들어, 3개의 눈 3, 3, 6이 주어지면 상금은 1,000+3×100으로 계산되어 1,300원을 받게 된다. 또 3개의 눈이 2, 2, 2로 주어지면 10,000+2×1,000 으로 계산되어 12,000원을 받게 된다. 3개의 눈이 6, 2, 5로 주어지면 그중 가장 큰 값이 6이므로 6×100으로 계산되어 600원을 상금으로 받게 된다.

# 3개 주사위의 나온 눈이 주어질 때, 상금을 계산하는 프로그램을 작성 하시오.

# 입력
# 첫째 줄에 3개의 눈이 빈칸을 사이에 두고 각각 주어진다.

# 출력
# 첫째 줄에 게임의 상금을 출력 한다.

# 예제 입력 1 
# 3 3 6
# 예제 출력 1 
# 1300
# 예제 입력 2 
# 2 2 2
# 예제 출력 2 
# 12000
# 예제 입력 3 
# 6 2 5
# 예제 출력 3 
# 600
# 출처
# Olympiad > 한국정보올림피아드 > 한국정보올림피아드시․도지역본선 > 지역본선 2010 > 중등부 1번

# 데이터를 추가한 사람: aname, tkdring3
# 잘못된 데이터를 찾은 사람: sait2000
# 알고리즘 분류
# 수학
# 구현
# 사칙연산
# 많은 조건 분기

# 구버전
dice = [0] * 6
a, b, c = list(map(int, input().split()))
dice[a - 1] += 1
dice[b - 1] += 1
dice[c - 1] += 1
max_num = 1
for j in dice:
  if max_num < j:
    max_num = j 

if max_num == 1:
  print(max(a, max(b, c)) * 100)
elif max_num == 2:
  print(1000 + (a*100)) if a == c else print(1000 + (b*100))
else :
  print(10000 + (a*1000))

# 개선 버전
dice = [0] * 7
a, b, c = list(map(int, input().split()))
dice[a] += 1
dice[b] += 1
dice[c] += 1

answer = ""
max_num = max(dice)

if max_num == 1:
    answer = max(a, max(b, c)) * 100
elif max_num == 2:
    if a == c:
        answer = 1000 + (a*100)
    else: 
        answer = 1000 + (b*100)
else :
    answer = 10000 + (a*1000)
print(answer)