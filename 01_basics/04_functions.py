# 1. 기본 함수 정의와 호출 (def 키워드)
def greet(name):
    """이름을 입력받아 인사말을 출력하는 기본 함수"""
    print(f"안녕하세요, {name}님! 파이썬 학습을 환영합니다.")


print("--- 1. 기본 함수 호출 ---")
greet("우분투")


# 2. 반환값(return)이 있는 함수
def add_numbers(a, b):
    """두 수를 더한 결과를 반환하는 함수"""
    return a + b


result = add_numbers(10, 20)
print(f"\n--- 2. 더하기 결과: {result} ---")


# 3. 기본값(Default Parameter)이 설정된 매개변수
def introduce(name, role="개발자"):
    """role 매개변수를 전달하지 않으면 기본값 '개발자' 적용"""
    print(f"이름: {name}, 직업: {role}")


print("\n--- 3. 기본 매개변수 활용 ---")
introduce("홍길동")  # role 생략 -> 기본값 사용
introduce("이순신", "장군")  # role 명시 -> 입력값 사용


# 4. 여러 값을 한 번에 반환하기 (튜플 형태 반환)
def get_min_max(numbers):
    """리스트에서 최솟값과 최댓값을 동시에 반환"""
    return min(numbers), max(numbers)


scores = [88, 92, 75, 100, 64]
minimum, maximum = get_min_max(scores)
print(f"\n--- 4. 점수 최저: {minimum}점, 최고: {maximum}점 ---")
