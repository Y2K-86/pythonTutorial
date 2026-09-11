# 1. 비교 연산자 및 기본 if-elif-else 문
# input()으로 받은 입력값은 항상 문자열(str)이므로 int()로 형변환합니다.
age_input = input("나이를 입력하세요: ")
age = int(age_input)

print("\n--- 1. 연령대 판별 ---")
if age >= 65:
    print("어르신 우대 대상입니다.")
elif age >= 20:
    print("성인입니다.")
elif age >= 14:
    print("청소년입니다.")
else:
    print("어린이입니다.")

# 2. 논리 연산자 (and, or, not) 사용법
# is_member = True, has_coupon = False 라면?
is_member = True
has_coupon = False

print("\n--- 2. 할인 조건 검사 (논리 연산자) ---")
# and: 둘 다 True여야 함 | or: 하나만 True여도 됨 | not: 반대로 뒤집음
if is_member and (has_coupon or age >= 65):
    print("특별 할인 혜택 대상자입니다!")
else:
    print("일반 가격이 적용됩니다.")

# 3. 삼항 연산자 (Ternary Operator) - 한 줄 조건문
# [True일 때 값] if [조건식] else [False일 때 값]
status = "성인" if age >= 20 else "미성년자"
print(f"\n--- 3. 삼항 연산자 결과: {status} ---")
