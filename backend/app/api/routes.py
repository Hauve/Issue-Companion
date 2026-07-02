from fastapi import APIRouter

router = APIRouter()


@router.post("/api/context")
def get_context_data():
    return {"a": "b"}
