# 1. 딕셔너리 생성 및 기본 조회
# 중괄호 {}를 사용하며, Key와 Value를 콜론(:)으로 연결합니다.
user_profile = {
    "name": "우분투",
    "age": 25,
    "skills": ["Python", "Git", "Linux"],
    "is_active": True,
}

print("--- 1. 기본 조회 ---")
print(f"이름: {user_profile['name']}")
print(f"보유 기술: {user_profile['skills']}")


# 2. 안전하게 데이터 가져오기 (.get() 메서드)
# 대괄호 조회 [key]는 존재하지 않는 키 접근 시 에러가 나지만,
# .get()을 쓰면 에러 대신 None 또는 기본값을 반환하여 안전합니다.
print("\n--- 2. 안전한 조회 (.get) ---")
email = user_profile.get("email", "이메일 없음")  # 키가 없으면 '이메일 없음' 반환
print(f"이메일: {email}")


# 3. 데이터 추가, 수정, 삭제
print("\n--- 3. 수정 및 추가 ---")
user_profile["age"] = 26  # 기존 값 수정
user_profile["location"] = "Seoul"  # 새로운 키-값 추가
del user_profile["is_active"]  # 키-값 삭제

print(f"수정된 프로필: {user_profile}")


# 4. 딕셔너리 순회 (keys, values, items)
print("\n--- 4. 딕셔너리 순회 (for문) ---")
# .items()를 사용하면 Key와 Value를 동시에 가져옵니다. (튜플 언패킹 활용)
for key, value in user_profile.items():
    print(f"키: {key} -> 값: {value}")
