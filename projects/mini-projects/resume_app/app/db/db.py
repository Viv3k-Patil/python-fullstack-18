"""
In-memory database for the Resume Portal.
Simulates a database using a plain dict — students replace this with a real DB.
"""

import logging
from typing import Optional
from uuid import UUID

from app.models.resume import ResumeRecord

logger = logging.getLogger(__name__)


class InMemoryDatabase:
    """Thread-unsafe, in-process store (fine for dev / learning purposes)."""

    def __init__(self) -> None:
        self._store: dict[UUID, ResumeRecord] = {}
        logger.info("InMemoryDatabase initialised.")

    # ------------------------------------------------------------------
    # CRUD helpers
    # ------------------------------------------------------------------

    def insert(self, record: ResumeRecord) -> ResumeRecord:
        self._store[record.id] = record
        logger.info("DB insert | id=%s | filename=%s", record.id, record.original_filename)
        return record

    def get(self, record_id: UUID) -> Optional[ResumeRecord]:
        record = self._store.get(record_id)
        if record:
            logger.debug("DB get hit | id=%s", record_id)
        else:
            logger.debug("DB get miss | id=%s", record_id)
        return record

    def get_all(self) -> list[ResumeRecord]:
        records = list(self._store.values())
        logger.debug("DB get_all | count=%d", len(records))
        return records

    def delete(self, record_id: UUID) -> bool:
        if record_id in self._store:
            del self._store[record_id]
            logger.info("DB delete | id=%s", record_id)
            return True
        logger.warning("DB delete miss | id=%s", record_id)
        return False

    def count(self) -> int:
        return len(self._store)


# Singleton instance — import this anywhere in the app
db = InMemoryDatabase()