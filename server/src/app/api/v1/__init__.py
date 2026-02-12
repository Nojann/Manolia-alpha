from fastapi import APIRouter

from .knowledges import router as knowledge_router
from .metrics import router as metric_router

router = APIRouter(prefix="/v1")
router.include_router(knowledge_router)
router.include_router(metric_router)