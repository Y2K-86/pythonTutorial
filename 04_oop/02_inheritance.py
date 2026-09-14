from pathlib import Path


# 1. 부모 클래스 (Parent / Super Class)
class User:
    def __init__(self, name: str, email: str):
        self.name = name
        self.email = email

    def get_info(self) -> str:
        """기본 사용자 정보 반환"""
        return f"이름: {self.name} | 이메일: {self.email}"

    def get_role(self) -> str:
        """사용자 권한 반환 (자식 클래스에서 오버라이딩할 예정)"""
        return "일반 사용자"


# 2. 자식 클래스 1: Student (User 상속)
class Student(User):
    def __init__(self, name: str, email: str, student_id: int):
        # super().__init__()을 통해 부모(User)의 생성자를 호출하여 name, email 초기화
        super().__init__(name, email)
        self.student_id = student_id  # Student만의 고유 변수 추가

    # [메서드 오버라이딩] 부모의 get_role() 재정의
    def get_role(self) -> str:
        return f"학생 (학번: {self.student_id})"


# 3. 자식 클래스 2: Teacher (User 상속)
class Teacher(User):
    def __init__(self, name: str, email: str, subject: str):
        super().__init__(name, email)
        self.subject = subject  # Teacher만의 고유 변수 추가

    # [메서드 오버라이딩] 부모의 get_role() 재정의
    def get_role(self) -> str:
        return f"교사 (담당 과목: {self.subject})"


# 4. 객체 생성 및 활용
print("--- 1. 객체 생성 및 다형성(Polymorphism) 확인 ---")

# 부모 클래스와 자식 클래스 객체들 생성
users = [
    User("홍길동", "hong@example.com"),
    Student("김철수", "chulsoo@example.com", 2026001),
    Teacher("이영희", "younghee@example.com", "파이썬 프로그래밍"),
]

# 하나의 리스트 안에서 서로 다른 클래스 객체들이 각자의 오버라이딩된 메서드를 실행
for user in users:
    print(f"[{user.get_role()}] {user.get_info()}")


# 5. pathlib을 활용한 사용자 권한 목록 파일 저장
print("\n--- 2. 사용자 정보 파일 저장 ---")
BASE_DIR = Path(__file__).resolve().parent
log_file = BASE_DIR / "user_list.txt"

with open(log_file, "w", encoding="utf-8") as f:
    f.write("=== 시스템 등록 사용자 목록 ===\n")
    for user in users:
        f.write(f"[{user.get_role()}] {user.get_info()}\n")

print(f"사용자 목록 저장 완료: {log_file}")
