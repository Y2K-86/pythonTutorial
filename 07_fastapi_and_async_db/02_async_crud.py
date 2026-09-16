"""
07_fastapi_and_async_db / 02_async_crud.py
- AsyncSession 기반 비동기 데이터 추가 및 조회
"""

import asyncio
from sqlalchemy import String, select
from sqlalchemy.orm import Mapped, mapped_column
from 01_async_db_engine import AsyncSessionLocal, Base, engine


class Item(Base):
    __tablename__ = "items"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(50))


async def create_and_read():
    # 비동기 트랜잭션 관리 (async with)
    async with AsyncSessionLocal() as session:
        # 1. 비동기 데이터 추가
        new_item = Item(name="Async Keyboard")
        session.add(new_item)
        await session.commit()  # DB 저장 대기 (await)

        # 2. 비동기 데이터 조회 (select)
        stmt = select(Item).where(Item.name == "Async Keyboard")
        result = await session.execute(stmt)  # DB 조회 대기 (await)
        item = result.scalar_one_or_none()
        print(f"✅ 조회된 아이템: {item.id} - {item.name}")


async def main():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    await create_and_read()


if __name__ == "__main__":
    asyncio.run(main())
