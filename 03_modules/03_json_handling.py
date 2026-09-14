import json
from pathlib import Path

# 1. 파이썬 딕셔너리 객체 준비
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

# 2. 직렬화 (Serialization): 파이썬 Dict -> JSON 파일로 저장 (.dump)
print("--- 1. 파이썬 딕셔너리를 JSON 파일로 저장 ---")
with open(json_file_path, "w", encoding="utf-8") as f:
    # indent=4: 보기 좋게 들여쓰기 4칸 적용
    # ensure_ascii=False: 한글이 \u... 형태로 깨지지 않고 그대로 저장되도록 설정
    json.dump(user_data, f, indent=4, ensure_ascii=False)

print(f"'{json_file_path}' 파일로 저장되었습니다.")


# 3. 역직렬화 (Deserialization): JSON 파일 -> 파이썬 Dict로 불러오기 (.load)
print("\n--- 2. JSON 파일을 읽어서 파이썬 딕셔너리로 변환 ---")
with open(json_file_path, "r", encoding="utf-8") as f:
    loaded_data = json.load(f)

print(f"불러온 데이터 타입: {type(loaded_data)}")
print(f"사용자 이름: {loaded_data['name']}")
print(f"주요 기술: {loaded_data['skills'][0]}")


# 4. 문자열(String) 형태의 JSON 변환 (.dumps / .loads)
# 파일이 아니라 네트워크 통신이나 API에서 문자열로 데이터를 받을 때 다루는 방법입니다.
print("\n--- 3. JSON 문자열 직접 파싱 ---")

# (1) Dict -> JSON 문자열 (dumps)
json_string = json.dumps(user_data, ensure_ascii=False)
print(f"JSON 문자열: {json_string}")

# (2) JSON 문자열 -> Dict (loads)
parsed_dict = json.loads(json_string)
print(f"파싱된 Dict 이름: {parsed_dict['name']}")
