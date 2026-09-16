"""
06_asyncio / 01_async_await.py
- async / await 키워드 기초 및 비동기 루틴 실행
"""

import asyncio
import time


# --- 1. 동기(Sync) 방식 함수 ---
def sync_fetch_data(user_id: int):
    print(f"  [Sync {user_id}] 데이터 요청 시작...")
    time.sleep(1)  # 1초 동안 전체 프로그램이 멈춤 (Blocking)
    print(f"  [Sync {user_id}] 데이터 수신 완료!")
    return f"User-{user_id} Data"


# --- 2. 비동기(Async) 코루틴 함수 ---
async def async_fetch_data(user_id: int):
    print(f"  [Async {user_id}] 데이터 요청 시작...")
    # time.sleep 대신 asyncio.sleep을 사용해야 CPU 제어권을 다른 작업에 양보함 (Non-blocking)
    await asyncio.sleep(1)
    print(f"  [Async {user_id}] 데이터 수신 완료!")
    return f"User-{user_id} Data"


# --- 3. 비동기 메인 실행 함수 ---
async def main():
    print("=== 1. 동기(Sync) 방식 실행 (순차 처리) ===")
    start = time.time()
    sync_fetch_data(1)
    sync_fetch_data(2)
    sync_fetch_data(3)
    print(f"⏱️ 동기 방식 총 소요 시간: {time.time() - start:.2f}초\n")

    print("=== 2. 비동기(Async) 방식 실행 (동시 처리) ===")
    start = time.time()
    # asyncio.gather: 여러 비동기 작업을 동시에 묶어서 실행
    results = await asyncio.gather(
        async_fetch_data(1),
        async_fetch_data(2),
        async_fetch_data(3)
    )
    print(f"결과 데이터: {results}")
    print(f"⏱️ 비동기 방식 총 소요 시간: {time.time() - start:.2f}초")


# --- 4. 파이썬 비동기 이벤트 루프 시작점 ---
if __name__ == "__main__":
    # async 함수는 그냥 main()으로 호출하면 안 되고, asyncio.run()으로 이벤트 루프를 열어줘야 함
    asyncio.run(main())

