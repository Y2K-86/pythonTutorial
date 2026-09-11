# 1. 변수 선언 및 기본 데이터 타입 (Data Types)
# 파이썬은 변수의 타입을 자동으로 판단합니다.

name = "우분투"       # 문자열 (str)
age = 25             # 정수 (int)
height = 175.5       # 실수 (float)
is_student = True    # 불리언 (bool: True/False)

# 2. type() 함수: 변수의 데이터 타입 확인
print("--- 1. 데이터 타입 확인 ---")
print("name의 타입:", type(name))
print("age의 타입:", type(age))
print("is_student의 타입:", type(is_student))

# 3. f-string 출력 (가장 자주 쓰는 문자열 포맷팅)
print("\n--- 2. f-string 출력 ---")
print(f"안녕하세요! 제 이름은 {name}이고, 나이는 {age}세입니다.")
print(f"내년에는 {age + 1}세가 됩니다.")

# 4. 형 변환 (Type Casting)
# input()으로 입력을 받거나 데이터 타입을 바꿀 때 사용합니다.
str_num = "100"
int_num = int(str_num)  # 문자열 "100"을 정수 100으로 변환

print("\n--- 3. 형 변환 결과 ---")
print(f"변환된 값: {int_num}, 타입: {type(int_num)}")
