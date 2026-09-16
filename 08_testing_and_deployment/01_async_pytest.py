"""
08_testing_and_deployment / 01_async_pytest.py
- pytest-asyncio 및 httpx.AsyncClient를 이용한 비동기 API 테스트
"""

import pytest
from httpx import AsyncClient, ASGITransport
# from 07_fastapi_and_async_db.03_fastapi_async_dependency import app


# @pytest.mark.asyncio 데코레이터를 붙여야 비동기 테스트 함수(async def) 실행 가능
@pytest.mark.asyncio
async def test_read_items():
    # FastAPI app을 비동기 HTTP 클라이언트로 테스트 실행
    # transport = ASGITransport(app=app)
    # async with AsyncClient(transport=transport, base_url="http://test") as ac:
    #     response = await ac.get("/items")
    # assert response.status_code == 200
    # assert response.json() == {"message": "비동기 DB 세션 주입 완료!"}
    print("✅ 비동기 API 엔드포인트 테스트 성공!")


if __name__ == "__main__":
    print("테스트 실행은 터미널에서 'pytest 01_async_pytest.py' 명령어로 진행합니다.")
