"""
05_advanced / 02_iterators_generators.py
- 이터레이터(Iterator)와 제너레이터(Generator)의 개념 및 활용
"""


# --- 1. 이터러블(Iterable)과 이터레이터(Iterator)의 기초 ---
# 리스트는 이터러블(반복 가능한 객체)이지만, 그 자체로 이터레이터는 아님
my_list = [10, 20, 30]
my_iter = iter(my_list)  # iter() 함수로 이터레이터 객체 생성

print("--- 1. Iterator 기초 (next 함수) ---")
print(next(my_iter))  # 10
print(next(my_iter))  # 20
print(next(my_iter))  # 30
# print(next(my_iter))  # ⚠️ 한번 더 부르면 StopIteration 예외 발생!


# --- 2. yield를 사용한 제너레이터(Generator) 함수 ---
def number_generator(max_num: int):
    """지정한 숫자까지 1씩 증가하며 뿜어내는 제너레이터"""
    print("▶ 제너레이터 시작")
    current = 1
    while current <= max_num:
        print(f"  [yield 직전] current = {current}")
        yield current  # 💥 여기서 값을 밖으로 던지고 일시 정지!
        print(f"  [yield 직후] 대기 해제 후 다음 루프 진행")
        current += 1
    print("▶ 제너레이터 종료")


print("\n--- 2. Generator 기본 동작 ---")
gen = number_generator(2)

# next()를 부를 때마다 yield 지점까지 실행되고 멈춤
print(f"외부 수신 1: {next(gen)}")
print(f"외부 수신 2: {next(gen)}")


# --- 3. 제너레이터 표현식 (Generator Expression) ---
print("\n--- 3. List Comprehension vs Generator Expression ---")
# 리스트 컴프리헨션: 대괄호 [], 메모리에 전체를 싹 다 올림
list_comp = [x * 2 for x in range(5)]

# 제너레이터 표현식: 소괄호 (), 메모리를 쓰지 않고 생성 준비만 함
gen_exp = (x * 2 for x in range(5))

print(f"List 결과: {list_comp}")
print(f"Generator 객체: {gen_exp}")
print(f"Generator에서 하나 추출: {next(gen_exp)}")


# --- 4. 실무 응용: 서버 자원 관리 패턴 (Setup & Teardown) ---
def fake_db_connection():
    """서버에서 흔히 쓰는 DB 커넥션 제너레이터 패턴"""
    print("\n[DB] 🟡 데이터베이스 연결 (Resource Setup)")
    db_session = {"status": "connected", "data": "Real Data"}

    try:
        yield db_session  # 호출자(API)에게 DB 세션을 주고 대기!
    finally:
        # 작업이 끝나거나 에러가 나도 무조건 실행되어 자원 반납
        print("[DB] 🔴 데이터베이스 연결 종료 및 자원 해제 (Teardown)")


print("\n--- 4. 실무 자원 관리 (yield) ---")
# 제너레이터 생성
db_gen = fake_db_connection()

# 1) DB 세션 받기
session = next(db_gen)
print(f"[API] 받아온 DB 정보로 비즈니스 로직 처리: {session['data']}")

# 2) 로직 처리 후 자원 정리 (일부러 한 번 더 불러서 yield 이후 실행)
try:
    next(db_gen)
except StopIteration:
    print("[API] DB 자원 정리 완료 확인")
