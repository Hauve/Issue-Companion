from fastapi import FastAPI

from app.api.routes import router

app = FastAPI(
    title='Issue Companion',
    version='0.1.0',
    docs_url="/api/docs",
)

app.include_router(router=router)


@app.get("/api/health")
def get_health():
    return {"status": "ok"}
