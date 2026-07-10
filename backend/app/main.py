from fastapi import FastAPI

from .api import routes

app = FastAPI(
    title='Issue Companion',
    version='0.1.0',
    docs_url="/api/docs",
)

app.include_router(router=routes.router)


@app.get("/api/health")
def get_health():
    return {"status": "healthy"}