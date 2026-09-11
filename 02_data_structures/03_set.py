# 1. 집합 생성 및 중복 자동 제거
# 중괄호 {}를 사용하지만, 딕셔너리와 달리 Key 없이 값만 넣습니다.
numbers = {1, 2, 2, 3, 3, 3, 4, 5}
print("--- 1. 중복 제거 확인 ---")
print(f"원본 집합: {numbers}")  # {1, 2, 3, 4, 5} 만 남음


# 2. 리스트의 중복 요소 한 줄로 제거하기 (실무 활용 Tip)
raw_users = ["kim", "lee", "kim", "park", "lee", "choi"]
unique_users = list(set(raw_users))  # list -> set(중복제거) -> list

print("\n--- 2. 리스트 중복 제거 ---")
print(f"중복 제거된 유저 목록: {unique_users}")


# 3. 데이터 추가 및 삭제
my_set = {"Python", "Git"}
my_set.add("Linux")  # 한 개 추가
my_set.remove("Git")  # 삭제 (없는 값 삭제 시 에러 발생)
my_set.discard("Docker")  # 안전한 삭제 (없는 값이어도 에러 안 남)

print("\n--- 3. 요소 추가/삭제 ---")
print(f"현재 집합: {my_set}")


# 4. 집합 연산 (합집합, 교집합, 차집합)
dev_a = {"Python", "Linux", "Docker"}
dev_b = {"Python", "AWS", "Kubernetes"}

print("\n--- 4. 집합 연산 ---")
print(
    f"교집합 (둘 다 할 줄 아는 것): {dev_a & dev_b}"
)  # 또는 dev_a.intersection(dev_b)
print(f"합집합 (전체 기술 목록): {dev_a | dev_b}")  # 또는 dev_a.union(dev_b)
print(f"차집합 (A만 할 줄 아는 것): {dev_a - dev_b}")  # 또는 dev_a.difference(dev_b)
