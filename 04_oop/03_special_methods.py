from pathlib import Path


class BankAccount:
    """은행 계좌 클래스 (캡슐화 및 매직 메서드 실습)"""

    def __init__(self, owner: str, initial_balance: int = 0):
        self.owner = owner
        # __ (Double Underscore)를 붙여 Private 변수로 선언 (캡슐화)
        # 클래스 외부에서 account.__balance 로 직접 접근 불가
        self.__balance = initial_balance
        self.__history = []  # 거래 내역 리스트

    # --- 1. 캡슐화를 위한 Getter / Setter (메서드를 통한 비즈니스 로직 검증) ---

    def get_balance(self) -> int:
        """잔액 조회 (Getter)"""
        return self.__balance

    def deposit(self, amount: int):
        """입금 처리"""
        if amount <= 0:
            print("❌ 입금 금액은 0원보다 커야 합니다.")
            return
        self.__balance += amount
        self.__history.append(f"입금: +{amount:,}원")
        print(f"💰 [{self.owner}] {amount:,}원 입금 완료 (잔액: {self.__balance:,}원)")

    def withdraw(self, amount: int):
        """출금 처리"""
        if amount > self.__balance:
            print(f"❌ 잔액이 부족합니다. (현재 잔액: {self.__balance:,}원)")
            return
        self.__balance -= amount
        self.__history.append(f"출금: -{amount:,}원")
        print(f"💸 [{self.owner}] {amount:,}원 출금 완료 (잔액: {self.__balance:,}원)")

    # --- 2. 주요 매직 메서드 (Special Methods) 구현 ---

    def __str__(self) -> str:
        """print(acc) 시 호출되는 가독성 높은 문자열"""
        return f"[계좌] 소유주: {self.owner} | 잔액: {self.__balance:,}원"

    def __repr__(self) -> str:
        """개발자 디버깅용 객체 표현"""
        return f"BankAccount(owner='{self.owner}', initial_balance={self.__balance})"

    def __len__(self) -> int:
        """len(acc) 호출 시 거래 내역 건수 반환"""
        return len(self.__history)

    def __eq__(self, other) -> bool:
        """acc1 == acc2 비교 시 잔액이 같은지 판별"""
        if isinstance(other, BankAccount):
            return self.__balance == other.__balance
        return False


# --- 실행 및 검증 ---
print("--- 1. 캡슐화 및 입출력 테스트 ---")
acc1 = BankAccount("홍길동", 10000)
acc2 = BankAccount("김철수", 10000)

acc1.deposit(5000)
acc1.withdraw(3000)
acc1.withdraw(20000)  # 잔액 부족 실패 테스트

# Private 변수 직접 접근 시도 (AttributeError 발생 확인)
try:
    print(acc1.__balance)
except AttributeError:
    print("🔒 Private 변수(__balance)는 외부에서 직접 접근할 수 없습니다!")

print("\n--- 2. 매직 메서드 동작 확인 ---")
# __str__ 테스트
print(f"str() 결과: {acc1}")

# __repr__ 테스트
print(f"repr() 결과: {repr(acc1)}")

# __len__ 테스트 (거래 내역 개수)
print(f"len() 결과 (총 거래 건수): {len(acc1)}건")

# __eq__ 테스트 (잔액 비교)
print(f"acc1 == acc2 (잔액 동일 여부): {acc1 == acc2}")


print("\n--- 3. pathlib 활용 계좌 거래 내역 저장 ---")
BASE_DIR = Path(__file__).resolve().parent
log_file = BASE_DIR / "account_log.txt"

with open(log_file, "w", encoding="utf-8") as f:
    f.write(f"=== {acc1.owner} 계좌 정보 ===\n")
    f.write(f"{acc1}\n")
    f.write(f"총 거래 건수: {len(acc1)}건\n")

print(f"기록 완료: {log_file.name}")
