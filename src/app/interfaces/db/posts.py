from __future__ import annotations
from uuid import UUID
from abc import (
    ABC,
    abstractmethod,
)

from app.infra.db.models.post import Post


class IPostReader(ABC):

    @abstractmethod
    async def get_posts(self,
                        limit: int = None,
                        offset: int = None,
                        theme: str = None
                        ) -> list[Post]:
        raise NotImplementedError

    @abstractmethod
    async def get_post(self, post_id: UUID) -> Post | None:
        raise NotImplementedError


class IPostWriter(ABC):
    @abstractmethod
    async def create_post(self, instance: Post):
        raise NotImplementedError
