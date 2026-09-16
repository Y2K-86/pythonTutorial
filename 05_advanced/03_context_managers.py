"""
05_advanced / 03_context_managers.py
- 컨텍스트 매니저(Context Manager)의 두 가지 구현 방식
"""

import time
from contextlib import contextmanager


# =====================================================================
# 방법 1. 클래스 기반 (OOP 방식: __enter__, __exit__ 매직 메서드)
# =====================================================================
class TimerContext:
    """코드 실행 시간을 자동으로 측정해주는 컨텍스트 매니저 클래스"""

    def __init__(self, task_name: str):
        self.task_name = task_name

    def __enter__(self):
        print(f"▶ [{self.task_name}] 작업 시작 - 타이머 작동!")
        self.start_time = time.time()
        return self  # as 변수로 전달될 객체 (여기선 자기 자신)

    def __exit__(self, exc_type, exc_val, exc_tb):
        # with 블록을 나갈 때 에러 여부와 관계없이 무조건 실행됨
        self.end_time = time.time()
        elapsed = self.end_time - self.start_time
        print(f"◀ [{self.task_name}] 작업 완료! (소요 시간: {elapsed:.4f}초)\n")
        # False를 반환하면 발생한 예외를 밖으로 던짐 (기본 동작)


# =====================================================================
# 방법 2. 함수 + yield 기반 (@contextmanager 데코레이터 활용)
# =====================================================================
@contextmanager
def file_manager(filename: str, mode: str):
    """yield와 try-finally를 이용해 with문 전용 함수로 변환"""
    print(f"📂 [Setup] '{filename}' 파일 연결 시도...")
    f = open(filename, mode, encoding="utf-8")
    try:
        yield f  # 💥 with 블록 내부(as f)로 파일 객체를 넘겨주고 일시 정지!
    finally:
        # with 블록이 끝나거나 에러가 나면 돌아와서 무조건 파일 정리
        print(f"🧹 [Teardown] '{filename}' 안전하게 닫기 완료!\n")
        f.close()


# =====================================================================
# 실행 테스트 (Main)
# =====================================================================
if __name__ == "__main__":
    print("--- 1. 클래스 기반 컨텍스트 매니저 실행 ---")
    with TimerContext("대용량 연산 테스트"):
        # 작업 진행 중...
        total = sum(i for i in range(5_000_000))
        time.sleep(0.5)

    print("--- 2. @contextmanager (yield) 기반 컨텍스트 매니저 실행 ---")
    # 자원을 만들고 닫는 과정을 with 문 하나로 깔끔하게 처리
    with file_manager("test_log.txt", "w") as f:
        f.write("컨텍스트 매니저로 기록한 로그입니다.\n")
        print("  -> 파일에 데이터 작성 중...")

    print("--- 3. 내장 open()과 비교 ---")
    # 파이썬 내장 open() 함수도 내부적으로 __enter__, __exit__가 구현되어 있음
    with open("test_log.txt", "r", encoding="utf-8") as f:
        content = f.read()
        print(f"  -> 파일 내용 읽기: {content.strip()}")
