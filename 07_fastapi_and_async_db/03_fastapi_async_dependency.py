"""
07_fastapi_and_async_db / 03_fastapi_async_dependency.py
- FastAPI와 AsyncSession 비동기 의존성 주입(Dependency Injection)
"""

from collections.abc import AsyncGenerator
from fastapi import Depends, FastAPI
from sqlalchemy.ext.asyncio import AsyncSession
from 01_async_db_engine import AsyncSessionLocal

app = FastAPI()


# 비동기 DB 세션 제너레이터 (핵심!)
async def get_db() -> AsyncGenerator[AsyncSession, None]:
    async with AsyncSessionLocal() as session:
        try:
            yield session  # 라우터로 세션 전달 후 일시 정지
        finally:
            await session.close()  # 응답 완료 후 세션 종료


@app.get("/items")
async def read_items(db: AsyncSession = Depends(get_db)):
    # 비동기 라우터 안에서 주입받은 async db 세션 사용
    return {"message": "비동기 DB 세션 주입 완료!"}

