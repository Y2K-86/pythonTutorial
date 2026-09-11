# 1. 리스트(List): 순서가 있고, 수정 가능한(Mutable) 자료구조
print("--- 1. 리스트 기본 및 데이터 수정 ---")
fruits = ["사과", "바나나", "체리"]

# 요소 추가
fruits.append("오렌지")
# 요소 삭제
fruits.remove("바나나")

print(f"현재 과일 목록: {fruits}")
print(f"첫 번째 과일: {fruits[0]}")  # 인덱싱 (0부터 시작)
print(f"총 과일 개수: {len(fruits)}")


# 2. 리스트 슬라이싱 (Slicing): [시작:끝+1]
print("\n--- 2. 리스트 슬라이싱 ---")
numbers = [10, 20, 30, 40, 50, 60, 70]
print(f"전체 리스트: {numbers}")
print(f"인덱스 1부터 3까지 (20, 30, 40): {numbers[1:4]}")
print(f"처음부터 3개: {numbers[:3]}")
print(f"마지막 요소: {numbers[-1]}")


# 3. 튜플(Tuple): 순서는 있지만, 수정 불가능한(Immutable) 자료구조
# 읽기 전용 데이터나 변경되지 않아야 할 좌표, 설정값 등에 사용
print("\n--- 3. 튜플 활용 ---")
location = (37.5665, 126.9780)  # 서울 위도/경도
print(f"서울 좌표 (위도, 경도): {location}")

# location[0] = 38.0  # ⚠️ 이 주석을 풀면 에러 발생 (튜플은 수정 불가!)


# 4. 리스트와 튜플 변환
print("\n--- 4. 타입 변환 ---")
my_list = list(location)  # 튜플 -> 리스트 (수정 가능한 상태로 변경)
my_list.append("서울시청")
print(f"변환 후 수정된 리스트: {my_list}")
