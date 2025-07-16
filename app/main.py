from fastapi import HTTPException
from fastapi.routing import APIRouter
from pydantic import ValidationError

from app.llm_service import LLMService
from app.models import PersonInfo, Recommendation

llm = LLMService()
router = APIRouter()


@router.post("/recommend", response_model=Recommendation)
async def recommend_department(person_info: PersonInfo):
    try:
        recommendation = await llm.recommend_department(person_info)
        return recommendation
    except ValidationError as e:
        raise HTTPException(status_code=422, detail=e.errors())
    except Exception as e:
        raise HTTPException(status_code=500, detail=e)
