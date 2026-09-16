"""
07_fastapi_and_async_db / 04_background_tasks.py
- FastAPI BackgroundTasks를 활용한 비동기 백그라운드 작업
"""

import asyncio
from fastapi import BackgroundTasks, FastAPI

app = FastAPI()


async def write_audit_log(message: str):
    """응답이 나간 후 백그라운드에서 실행될 비동기 작업"""
    await asyncio.sleep(2)  # 파일 저장/로깅 대기
    print(f"📝 [Background Log]: {message}")


@app.post("/send-notification")
async def send_notification(email: str, background_tasks: BackgroundTasks):
    # 클라이언트에게는 즉시 응답을 주고, 로깅은 백그라운드 태스크에 등록
    background_tasks.add_task(write_audit_log, f"{email}에게 알림 전송됨")
    return {"status": "accepted", "message": "요청이 접수되었습니다."}
