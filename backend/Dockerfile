FROM python:3.13-slim AS builder
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1
COPY --from=ghcr.io/astral-sh/uv:latest /uv /bin/uv
WORKDIR /build
COPY pyproject.toml uv.lock ./

ENV UV_NO_DEV=1
RUN uv sync --frozen --no-install-project --no-dev


FROM python:3.13-slim AS runner
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1
    
WORKDIR /backend
COPY --from=builder /build/.venv /backend/.venv
COPY app /backend/app


ENV PATH="/backend/.venv/bin:$PATH"

RUN addgroup --system --gid 1001 appgroup && \
    adduser --system --uid 1001 --gid 1001 appuser
USER appuser


CMD ["python", "-m", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]