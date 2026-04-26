__all__ = ()

from fastapi import APIRouter

from .tasks.route import router as tasks_router

main_router = APIRouter()

router_list = (
    tasks_router,
)

for router in router_list:
    main_router.include_router(router)


