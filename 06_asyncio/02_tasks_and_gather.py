"""
06_asyncio / 02_tasks_and_gather.py
- 백그라운드 Task 생성 및 gather를 통한 병렬 처리
"""

import asyncio
import time


async def fetch_api(service_name: str, delay: int) -> dict:
    """가상의 외부 API 서비스 호출 코루틴"""
    print(f"🚀 [{service_name}] API 요청 전송 (소요 예상: {delay}초)")
    await asyncio.sleep(delay)
    print(f"✅ [{service_name}] 응답 수신 완료!")
    return {"service": service_name, "status": 200}


# =====================================================================
# 1. asyncio.create_task(): 백그라운드에서 즉시 실행 시작
# =====================================================================
async def demo_create_task():
    print("--- 1. create_task 데모 (백그라운드 즉시 실행) ---")
    start = time.time()

    # create_task를 호출하는 순간 이벤트 루프에 등록되어 백그라운드 실행이 시작됨
    task1 = asyncio.create_task(fetch_api("유저 서비스", 2))
    task2 = asyncio.create_task(fetch_api("결제 서비스", 1))

    print("  -> 태스크 생성 완료! 다른 작업(로깅 등)을 여기서 진행할 수 있음...")
    await asyncio.sleep(0.5)
    print("  -> 메인 로직 작업 중...")

    # 결과가 필요한 시점에 await로 기다려 결과값을 가져옴
    res1 = await task1
    res2 = await task2

    print(f"결과: {res1}, {res2}")
    print(f"⏱️ create_task 총 소요 시간: {time.time() - start:.2f}초\n")


# =====================================================================
# 2. asyncio.gather(): N개의 작업을 깔끔하게 묶어서 한 번에 병렬 실행
# =====================================================================
async def demo_gather():
    print("--- 2. gather 데모 (N개 작업 일괄 동시 처리) ---")
    start = time.time()

    # 여러 코루틴을 한 번에 리스트처럼 묶어서 전달
    # 가장 오래 걸리는 작업(3초) 기준으로 전체 실행 시간이 결정됨
    results = await asyncio.gather(
        fetch_api("상품 목록", 1),
        fetch_api("배송 정보", 3),
        fetch_api("쿠폰 목록", 2),
    )

    print(f"모든 서비스 응답 결과: {results}")
    print(f"⏱️ gather 총 소요 시간: {time.time() - start:.2f}초")


# =====================================================================
# 실행 제어
# =====================================================================
async def main():
    await demo_create_task()
    await demo_gather()


if __name__ == "__main__":
    asyncio.run(main())
