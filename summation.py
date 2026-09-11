# 1. range in loop
for num in range(1, 10):
    pass


# 2. try-exception-finally
try:
    number = int(input("짝수를 입력하세요: "))
except ValueError:
    print("숫자를 입력해야 합니다.")
else:
    # 에러가 없을 때만 실행
    if number % 2 == 0:
        print(f"올바른 입력입니다! 입력한 짝수: {number}")
    else:
        print("숫자는 입력했지만 짝수가 아닙니다.")
finally:
    # 에러가 나든 안 나든 항상 실행
    print("프로그램 검사를 종료합니다.")

# 3. list - tuple - dictionary - set
# 4. comprehension

# 5. file io - with open, readlines, enumerate
with open(file_path, "r", encoding="utf-8") as f:
    lines = f.readlines()  # 각 줄을 요소로 가지는 리스트 반환
    for idx, line in enumerate(lines, 1):
        pass
