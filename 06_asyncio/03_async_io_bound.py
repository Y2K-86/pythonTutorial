"""
06_asyncio / 03_async_io_bound.py
- 동기 HTTP 요청(Blocking) vs 비동기 HTTP 요청(Non-blocking) 비교
"""

import asyncio
import time


# 가상의 동기 I/O 요청 (예: requests.get)
def sync_network_request(site_id: int):
    print(f"  [Sync] 사이트 {site_id} 접속 중...")
    time.sleep(1)  # 전체 프로세스가 멈춤
    return f"Site {site_id} Data"


# 가상의 비동기 I/O 요청 (예: httpx.AsyncClient().get)
async def async_network_request(site_id: int):
    print(f"  [Async] 사이트 {site_id} 비동기 접속 중...")
    await asyncio.sleep(1)  # 제어권을 이벤트 루프에 양보
    return f"Site {site_id} Data"


async def main():
    print("--- 1. 동기 방식 (순차 처리: 3초 소요 예상) ---")
    start = time.time()
    for i in range(1, 4):
        sync_network_request(i)
    print(f"⏱️ 동기 소요 시간: {time.time() - start:.2f}초\n")

    print("--- 2. 비동기 방식 (동시 처리: 1초 소요 예상) ---")
    start = time.time()
    tasks = [async_network_request(i) for i in range(1, 4)]
    results = await asyncio.gather(*tasks)
    print(f"결과: {results}")
    print(f"⏱️ 비동기 소요 시간: {time.time() - start:.2f}초")


if __name__ == "__main__":
    asyncio.run(main())
