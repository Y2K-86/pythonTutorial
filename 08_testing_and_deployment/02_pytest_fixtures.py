"""
08_testing_and_deployment / 02_pytest_fixtures.py
- pytest fixture를 이용한 비동기 DB 세션 라이프사이클 관리
"""

import pytest_asyncio
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_sessionmaker


TEST_DATABASE_URL = "sqlite+aiosqlite:///:memory:"  # 인메모리 테스트 DB


@pytest_asyncio.fixture
async def db_session():
    """각 테스트마다 독립적으로 생성되고 파기되는 비동기 DB 세션 Fixture"""
    engine = create_async_engine(TEST_DATABASE_URL)
    session_factory = async_sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)

    async with session_factory() as session:
        yield session  # 테스트 함수로 비동기 세션 전달
        # 테스트가 끝나면 아래가 실행되어 안전하게 정리됨
        await session.rollback()
        await session.close()
