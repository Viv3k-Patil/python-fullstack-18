# """
# services/campus_service.py

# All business logic lives here. NEVER in the router.

# The router calls this. This calls the repository (Phase 2).
# When we switch to Postgres in Phase 2 — only this file
# changes. The router stays exactly the same.
# That is the entire point of this layer.
# """

# from uuid import UUID, uuid4
# from datetime import datetime, timezone

# from app.schemas.campus import CampusCreate, CampusUpdate, CampusResponse
# from app.core.exceptions import NotFoundException, ConflictException

# # ── Temporary in-memory store ─────────────────────────────
# # Replaced 100% by CampusRepository in Phase 2.
# # Do not add any logic that depends on this being a dict.
# _campuses: dict[UUID, dict] = {}


# class CampusService:

#     def create(self, data: CampusCreate) -> CampusResponse:
#         # business rule: no duplicate campus names
#         for c in _campuses.values():
#             if c["name"].lower() == data.name.lower():
#                 raise ConflictException(f"Campus '{data.name}' already exists")

#         campus = {
#             "id": uuid4(),
#             "name": data.name,
#             "city": data.city,
#             "address": data.address,
#             "cabin_count": data.cabin_count,
#             "is_active": True,
#             "created_at": datetime.now(timezone.utc),
#         }
#         _campuses[campus["id"]] = campus
#         return CampusResponse(**campus)

#     def get_all(self, page: int, size: int) -> tuple[list[CampusResponse], int]:
#         active = [c for c in _campuses.values() if c["is_active"]]
#         total = len(active)
#         start = (page - 1) * size
#         chunk = active[start: start + size]
#         return [CampusResponse(**c) for c in chunk], total

#     def get_by_id(self, campus_id: UUID) -> CampusResponse:
#         campus = _campuses.get(campus_id)
#         if not campus or not campus["is_active"]:
#             raise NotFoundException(f"Campus {campus_id} not found")
#         return CampusResponse(**campus)

#     def update(self, campus_id: UUID, data: CampusUpdate) -> CampusResponse:
#         campus = _campuses.get(campus_id)
#         if not campus or not campus["is_active"]:
#             raise NotFoundException(f"Campus {campus_id} not found")

#         # only update fields the client actually sent
#         updates = data.model_dump(exclude_none=True)
#         campus.update(updates)
#         _campuses[campus_id] = campus
#         return CampusResponse(**campus)

#     def delete(self, campus_id: UUID) -> CampusResponse:
#         campus = _campuses.get(campus_id)
#         if not campus or not campus["is_active"]:
#             raise NotFoundException(f"Campus {campus_id} not found")

#         # always soft delete — never remove from DB
#         campus["is_active"] = False
#         return CampusResponse(**campus)


# campus_service = CampusService()
from app.schemas.campus import CampusResponse, CampusCreate
from app.repositories.CampusRepository import CampusRepository
from sqlalchemy.ext.asyncio import AsyncSession

class CampusService:

    def __init__(self, db: AsyncSession):
        self.campus_repo = CampusRepository(db)
    
    async def create(self, data: CampusCreate) -> CampusResponse:
        campus = await self.campus_repo.create(data)
        return CampusResponse.model_validate(campus)
    
    async def get_by_id(self, campus_id: int)-> CampusResponse:
        campus = await self.campus_repo.get_by_id(campus_id)
        return CampusResponse.model_validate(campus)
    
    async def get_all(self, page: int, size: int) -> tuple[list[CampusResponse], int]:
        campuses, total = await self.campus_repo.get_all(page, size)
        return [CampusResponse.model_validate(c) for c in campuses], total
    
    async def delete(self, campus_id: int):
        return await self.campus_repo.soft_delete(campus_id)
    
