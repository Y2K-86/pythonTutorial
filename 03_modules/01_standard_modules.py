# 1. math 모듈: 수학 관련 유용한 기능 제공
import math

print("--- 1. math 모듈 활용 ---")
print(f"원주율 (pi): {math.pi}")
print(f"4의 제곱근: {math.sqrt(4)}")
print(f"3.14 올림: {math.ceil(3.14)}")
print(f"3.14 내림: {math.floor(3.14)}")


# 2. random 모듈: 난수 생성 및 무작위 추출
import random

print("\n--- 2. random 모듈 활용 ---")
print(f"1~10 사이 무작위 정수: {random.randint(1, 10)}")

fruits = ["사과", "바나나", "체리", "오렌지"]
print(f"무작위 하나 뽑기: {random.choice(fruits)}")

numbers = [1, 2, 3, 4, 5]
random.shuffle(numbers)
print(f"무작위 섞기: {numbers}")


# 3. datetime 모듈: 날짜 및 시간 다루기
from datetime import datetime, timedelta

print("\n--- 3. datetime 모듈 활용 ---")
now = datetime.now()
print(f"현재 날짜와 시간: {now}")
print(f"날짜 포맷팅 (YYYY-MM-DD): {now.strftime('%Y-%m-%d %H:%M:%S')}")

# 날짜 연산 (오늘로부터 7일 뒤)
future = now + timedelta(days=7)
print(f"일주일 뒤 날짜: {future.strftime('%Y-%m-%d')}")


# 4. os / sys 모듈: 운영체제 및 시스템 제어 (Ubuntu 환경 제어)
import os

print("\n--- 4. os 모듈 활용 (Ubuntu 관련) ---")
print(f"현재 작업 디렉터리: {os.getcwd()}")
print(f"현재 폴더 내 파일 목록: {os.listdir('.')}")
