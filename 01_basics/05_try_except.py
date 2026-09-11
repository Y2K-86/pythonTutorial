# 1. 기본 예외 처리 (ZeroDivisionError & ValueError 방어)
print("--- 1. 나눗셈 프로그램 (에러 방어) ---")

try:
    num1 = int(input("첫 번째 정수를 입력하세요: "))
    num2 = int(input("두 번째 정수를 입력하세요: "))
    result = num1 / num2
    print(f"나눗셈 결과: {result}")

except ValueError:
    # 문자를 입력해서 int() 변환에 실패한 경우
    print("⚠️ 오류: 숫자가 아닌 문자열을 입력하셨습니다.")

except ZeroDivisionError:
    # 0으로 나누려고 한 경우
    print("⚠️ 오류: 0으로 숫자를 나눌 수 없습니다.")

except Exception as e:
    # 위에 예상하지 못한 기타 모든 에러 처리
    print(f"⚠️ 알 수 없는 오류 발생: {e}")


# 2. else 문과 finally 문
# - else: 에러가 전혀 발생하지 않았을 때 실행
# - finally: 에러 발생 여부와 상관없이 무조건 마지막에 실행 (파일 닫기, DB 연결 종료 등에 사용)
print("\n--- 2. else와 finally 동작 확인 ---")

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
