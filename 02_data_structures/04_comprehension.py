# 1. 일반 for문 vs 리스트 컴프리헨션 (List Comprehension)
# 목표: 1부터 10까지의 숫자 중 짝수의 제곱 리스트 만들기

# [방식 A] 일반 for문 사용 시 (4줄)
even_squares_old = []
for i in range(1, 11):
    if i % 2 == 0:
        even_squares_old.append(i**2)

# [방식 B] 리스트 컴프리헨션 사용 시 (단 1줄!)
# 문법 구조: [ 표현식 for 변수 in 반복가능객체 if 조건식 ]
even_squares_new = [i**2 for i in range(1, 11) if i % 2 == 0]

print("--- 1. 리스트 컴프리헨션 결과 ---")
print(f"일반 for문 결과: {even_squares_old}")
print(f"컴프리헨션 결과: {even_squares_new}")


# 2. 문자열 리스트 가공예제 (실무 필터링/가공)
print("\n--- 2. 문자열 가공 ---")
words = ["python", "is", "awesome", "data", "structure"]

# 4글자 이상인 단어만 대문자로 바꿔서 새 리스트 만들기
uppercase_words = [word.upper() for word in words if len(word) >= 4]
print(f"가공된 단어 목록: {uppercase_words}")


# 3. 딕셔너리 컴프리헨션 (Dictionary Comprehension)
# 문법 구조: { key_표현식 : value_표현식 for 변수 in 반복가능객체 }
print("\n--- 3. 딕셔너리 컴프리헨션 ---")
students = ["Kim", "Lee", "Park"]
scores = [85, 92, 78]

# 두 리스트를 묶어서 딕셔너리로 즉시 생성
score_dict = {student: score for student, score in zip(students, scores)}
print(f"학생 점수 딕셔너리: {score_dict}")

# 80점 이상인 학생만 추출
pass_students = {student: score for student, score in score_dict.items() if score >= 80}
print(f"합격자 목록: {pass_students}")
