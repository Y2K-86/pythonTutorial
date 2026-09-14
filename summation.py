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
with open("file_path", "r", encoding="utf-8") as f:
    lines = f.readlines()  # 각 줄을 요소로 가지는 리스트 반환
    for idx, line in enumerate(lines, 1):
        pass

# 6. Json Handling
import json
from pathlib import Path

# 6.1. 파이썬 딕셔너리 객체 준비
user_data = {
    "user_id": 1001,
    "name": "홍길동",
    "skills": ["Python", "Linux", "Git"],
    "is_member": True,
}

# 경로문제 발생 코드
# json_file_path = "03_modules/user_data.json"

# os.path.dirname(os.path.abspath(__file__))와 완전히 동일한 역할
BASE_DIR = Path(__file__).resolve().parent

# 경로 결합도 / 기호로 깔끔하게 가능!
json_file_path = BASE_DIR / "user_data.json"

# 6.2. 직렬화 (Serialization): 파이썬 Dict -> JSON 파일로 저장 (.dump)
print("--- 1. 파이썬 딕셔너리를 JSON 파일로 저장 ---")
with open(json_file_path, "w", encoding="utf-8") as f:
    # indent=4: 보기 좋게 들여쓰기 4칸 적용
    # ensure_ascii=False: 한글이 \u... 형태로 깨지지 않고 그대로 저장되도록 설정
    json.dump(user_data, f, indent=4, ensure_ascii=False)

print(f"'{json_file_path}' 파일로 저장되었습니다.")


# 6.3. 역직렬화 (Deserialization): JSON 파일 -> 파이썬 Dict로 불러오기 (.load)
print("\n--- 2. JSON 파일을 읽어서 파이썬 딕셔너리로 변환 ---")
with open(json_file_path, "r", encoding="utf-8") as f:
    loaded_data = json.load(f)

# (1) Dict -> JSON 문자열 (dumps)
json_string = json.dumps(user_data, ensure_ascii=False)
print(f"JSON 문자열: {json_string}")

# (2) JSON 문자열 -> Dict (loads)
parsed_dict = json.loads(json_string)
print(f"파싱된 Dict 이름: {parsed_dict['name']}")

# 7. 파일 경로 설정
from pathlib import Path

# os.path.dirname(os.path.abspath(__file__))와 완전히 동일한 역할
BASE_DIR = Path(__file__).resolve().parent

# 경로 결합도 / 기호로 깔끔하게 가능!
json_file_path = BASE_DIR / "user_data.json"
