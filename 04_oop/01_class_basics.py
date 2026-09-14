from pathlib import Path


# 1. 클래스(Class) 정의: 객체를 찍어내는 틀/설계도
class Student:
    # 클래스 변수: 모든 객체가 공유하는 데이터
    school_name = "파이썬 IT 아카데미"

    # 생성자 메서드(__init__): 객체가 생성될 때 자동으로 호출됨
    def __init__(self, name: str, student_id: int):
        # 인스턴스 변수: 각 객체마다 독립적으로 갖는 데이터
        self.name = name
        self.student_id = student_id
        self.scores = []

    # 인스턴스 메서드: 객체의 행동을 정의 (첫 번째 인자는 무조건 self)
    def add_score(self, score: int):
        self.scores.append(score)
        print(f"[{self.name}] 점수 {score}점이 추가되었습니다.")

    def get_average(self) -> float:
        if not self.scores:
            return 0.0
        return sum(self.scores) / len(self.scores)

    def print_info(self):
        avg = self.get_average()
        print(
            f"학교: {Student.school_name} | 학번: {self.student_id} | 이름: {self.name} | 평균점수: {avg:.1f}점"
        )


# 2. 객체(Instance) 생성 및 활용
print("--- 1. 객체 생성 및 메서드 호출 ---")
# Student 클래스로부터 독립된 객체 2개 생성
student1 = Student("김철수", 2026001)
student2 = Student("이영희", 2026002)

# 메서드 실행
student1.add_score(85)
student1.add_score(92)

student2.add_score(100)
student2.add_score(95)

print("\n--- 2. 학생 정보 출력 ---")
student1.print_info()
student2.print_info()


# 3. pathlib을 활용한 안전한 파일 저장 응용
print("\n--- 3. 학습 기록 저장 ---")
BASE_DIR = Path(__file__).resolve().parent
log_file = BASE_DIR / "student_log.txt"

with open(log_file, "w", encoding="utf-8") as f:
    f.write(f"등록 학생 수: 2명\n")
    f.write(f"{student1.name}: 평균 {student1.get_average():.1f}점\n")
    f.write(f"{student2.name}: 평균 {student2.get_average():.1f}점\n")

print(f"기록이 완료되었습니다: {log_file}")
