"""
06_asyncio / 04_async_generator.py
- 비동기 제너레이터(async yield) 및 async for 구문 활용
"""

import asyncio


# 비동기로 스트리밍 데이터를 받아오는 제너레이터 (FastAPI의 Depends(get_db) 원리)
async def async_data_streamer():
    for i in range(1, 4):
        await asyncio.sleep(0.5)  # 비동기 데이터 조회 대기
        yield f"스트리밍 데이터조각 #{i}"  # async와 yield의 결합!


async def main():
    print("--- 비동기 제너레이터 데이터 수신 시작 ---")

    # 비동기 제너레이터의 데이터를 하나씩 꺼내올 때는 'async for'를 사용!
    async for data in async_data_streamer():
        print(f"  -> 수신 완료: {data}")

    print("--- 데이터 스트리밍 종료 ---")


if __name__ == "__main__":
    asyncio.run(main())
