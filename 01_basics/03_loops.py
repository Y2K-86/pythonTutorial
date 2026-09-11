# 1. for문: range() 함수를 이용한 정해진 횟수 반복
print("--- 1. range()를 활용한 for문 ---")
# range(시작, 끝+1, 증감) -> 1부터 5까지 1씩 증가
for i in range(1, 6):
    print(f"{i}번째 반복 중입니다.")

# 2. for문: 리스트 요소 순회 (가장 많이 쓰이는 형태)
print("\n--- 2. 리스트 요소 순회 ---")
fruits = ["사과", "바나나", "체리"]
for fruit in fruits:
    print(f"맛있는 {fruit}")

# 3. while문: 조건이 참(True)인 동안 계속 반복
print("\n--- 3. while문과 카운트다운 ---")
count = 3
while count > 0:
    print(f"카운트다운: {count}")
    count -= 1  # count = count - 1 과 동일
print("발사!")

# 4. break와 continue 제어문
print("\n--- 4. break와 continue ---")
for num in range(1, 10):
    if num % 2 == 0:
        continue  # 짝수일 때는 아래 코드를 건너뛰고 다음 반복으로 넘어감
    if num > 7:
        break  # 7보다 크면 반복문을 즉시 완전 종료함
    print(f"홀수 출력: {num}")
