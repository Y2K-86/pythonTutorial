"""
05_advanced / 04_type_hinting.py
- 파이썬 타입 힌팅의 기초 및 실무 고급 활용
"""

from typing import Callable, TypeVar

# --- 1. 기본 타입 및 컬렉션 타입 힌트 ---
def process_user_data(
    names: list[str],
    meta: dict[str, int]
) -> list[str]:
    """사용자 이름 목록을 대문자로 변환해 반환"""
    return [name.upper() for name in names]


# --- 2. None 허용 (Optional / Pipe 연산자) ---
def get_user_email(user_id: int) -> str | None:
    """유저 ID 조회 실패 시 None을 안전하게 반환 가능함을 명시"""
    db = {1: "admin@test.com", 2: "user@test.com"}
    return db.get(user_id)  # 키가 없으면 None 반환


# --- 3. 콜백 함수 타입 힌트 (Callable) ---
def run_calculator(
    calc_fn: Callable[[int, int], int],
    a: int,
    b: int
) -> int:
    """함수를 인자로 받아 실행해주는 고차 함수"""
    return calc_fn(a, b)


# --- 4. 제네릭(Generic) - 입력 타입과 출력 타입을 동적으로 매핑 ---
T = TypeVar("T")  # 임의의 타입을 의미하는 템플릿 변수

def get_first_item(items: list[T]) -> T | None:
    """리스트의 첫 번째 요소를 원본 타입 그대로 반환"""
    if not items:
        return None
    return items[0]


# --- 실행 및 테스트 ---
if __name__ == "__main__":
    print("--- 1. 컬렉션 타입 테스트 ---")
    users = ["kim", "lee", "park"]
    print(process_user_data(users, {"count": 3}))

    print("\n--- 2. None 처리 테스트 ---")
    email = get_user_email(999)
    if email is None:
        print("사용자를 찾을 수 없습니다.")

    print("\n--- 3. Callable(함수 인자) 테스트 ---")
    multiply = lambda x, y: x * y
    print(f"연산 결과: {run_calculator(multiply, 4, 5)}")

    print("\n--- 4. Generic 테스트 ---")
    int_first = get_first_item([10, 20, 30])    # T가 int로 추론됨
    str_first = get_first_item(["A", "B", "C"])  # T가 str로 추론됨
    print(f"숫자 첫 번째: {int_first}, 문자 첫 번째: {str_first}")
