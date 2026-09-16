import time

# 1. 데코레이터 함수 정의 (다른 함수를 인자로 받음)
def timer_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)  # 원본 함수 실행
        end_time = time.time()
        print(f"⏱️ [{func.__name__}] 실행 시간: {end_time - start_time:.4f}초")
        return result
    return wrapper

# 2. @ 기호를 사용해 함수에 데코레이터 적용
@timer_decorator
def heavy_processing():
    """시간이 좀 걸리는 작업"""
    total = sum(i for i in range(10_000_000))
    return total

# 3. 실행
heavy_processing()
