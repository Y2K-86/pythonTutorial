# 08_testing_and_deployment / Dockerfile

# 1. 경량화된 파이썬 3.11/3.12 이미지 사용
FROM python:3.11-slim

# 2. 작업 디렉토리 설정
WORKDIR /app

# 3. 의존성 파일 복사 및 설치 (uvicorn, fastapi, sqlalchemy, aiosqlite 등)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 4. 애플리케이션 코드 전체 복사
COPY . .

# 5. Uvicorn 비동기 ASGI 웹 서버 실행 명령 (포트 8000)
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
