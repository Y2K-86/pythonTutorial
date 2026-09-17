"""
06_asyncio / 05_threads_and_processes.py
- 파이썬의 threading 모듈과 multiprocessing 모듈 기초 연습
"""

from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor
import os
import time


def cpu_bound_task(number: int) -> int:
    """CPU를 많이 쓰는 계산 작업 (GIL의 영향을 받음)"""
    print(f"  [PID {os.getpid()}] 계산 시작: {number}")
    count = 0
    for i in range(10_000_000):
        count += i
    return count


def main():
    numbers = [1, 2, 3, 4]

    # 1. ThreadPoolExecutor (멀티쓰레드 - 파이썬 GIL 때문에 CPU 작업은 속도 향상 적음)
    print("--- 1. Multi-Threading 실행 ---")
    start = time.time()
    with ThreadPoolExecutor(max_workers=4) as executor:
        results = list(executor.map(cpu_bound_task, numbers))
    print(f"⏱️ 쓰레드 소요 시간: {time.time() - start:.2f}초\n")

    # 2. ProcessPoolExecutor (멀티프로세싱 - 코어별로 프로세스를 새로 띄워 GIL 완전 회피)
    print("--- 2. Multi-Processing 실행 (진짜 CPU 병렬 처리) ---")
    start = time.time()
    with ProcessPoolExecutor(max_workers=4) as executor:
        results = list(executor.map(cpu_bound_task, numbers))
    print(f"⏱️ 멀티프로세스 소요 시간: {time.time() - start:.2f}초")


if __name__ == "__main__":
    main()
