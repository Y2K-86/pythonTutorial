import os

# 파일 경로 지정
file_path = "03_modules/test_log.txt"

# 1. 파일 쓰기 ('w' 모드: Write - 기존 내용을 덮어씀)
# encoding="utf-8"을 지정해야 한글 깨짐을 방지할 수 있습니다.
print("--- 1. 파일에 글 쓰기 ('w' 모드) ---")
with open(file_path, "w", encoding="utf-8") as f:
    f.write("파이썬 학습 일지\n")
    f.write("1. 변수와 조건문 완료\n")
    f.write("2. 자료구조 완벽 이해\n")
print(f"'{file_path}' 파일이 생성되었습니다.")


# 2. 파일 이어 쓰기 ('a' 모드: Append - 기존 내용 뒤에 덧붙임)
print("\n--- 2. 파일에 내용 추가하기 ('a' 모드) ---")
with open(file_path, "a", encoding="utf-8") as f:
    f.write("3. 파일 입출력 진행 중!\n")
print("내용이 추가되었습니다.")


# 3. 파일 전체 읽기 ('r' 모드: Read)
print("\n--- 3. 파일 전체 읽기 ('r' 모드) ---")
with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()
    print(content)


# 4. 파일 줄 단위로 읽기 (.readlines())
print("--- 4. 줄 단위 순회 ---")
with open(file_path, "r", encoding="utf-8") as f:
    lines = f.readlines()  # 각 줄을 요소로 가지는 리스트 반환
    for idx, line in enumerate(lines, 1):
        # line.strip()은 줄바꿈 문자(\n)를 제거합니다.
        print(f"[{idx}줄] {line.strip()}")
