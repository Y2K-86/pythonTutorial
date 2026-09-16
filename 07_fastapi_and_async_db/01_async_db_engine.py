"""
07_fastapi_and_async_db / 01_async_db_engine.py
- SQLAlchemy AsyncEngine 및 AsyncSession 설정
"""

import asyncio
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase

# 1. 비동기 DB 드라이버 지정 (sqlite+aiosqlite)
DATABASE_URL = "sqlite+aiosqlite:///./test_async.db"

# 2. 비동기 엔진 및 세션 팩토리 생성
engine = create_async_engine(DATABASE_URL, echo=True)
AsyncSessionLocal = async_sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)

class Base(DeclarativeBase):
    pass

async def main():
    # 비동기로 테이블 생성
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    print("✅ 비동기 DB 엔진 설정 및 테이블 생성 완료!")

if __name__ == "__main__":
    asyncio.run(main())
