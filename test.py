import sympy as sp

# 1. 사용할 변수(미지수) 지정
x = sp.Symbol("x")

# 2. 방정식 정의 (좌변 - 우변 = 0 형태, 또는 Eq 함수 사용)
# 2x + 4 = 10 은 2x + 4 - 10 = 0 으로 표현 가능
eq = sp.Eq(2 * x**2 + 2 * x + 4, 10)

# 3. 방정식 풀기
solution = sp.solve(eq, x)

print(f"해: {solution}")  # 출력 결과: 해: [3]
