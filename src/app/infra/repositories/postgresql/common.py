from datetime import datetime
from typing import (
    Any,
    TypeVar,
)

from sqlalchemy import (
    Case,
    case,
    delete,
    select,
    update,
)
from sqlalchemy.ext.asyncio import AsyncSession

T = TypeVar('T')


class CommonRepo:

    def __init__(self, session: AsyncSession):
        self.session = session

    def latest_date(self, entity: T) -> Case[Any]:  # noqa
        return case(
            (entity.updated_at != None, entity.updated_at),  # noqa When condition and value
            else_=entity.created_at  # Default value if no when conditions are true
        )

    async def get(self, entity: T, where):
        query = (
            select(entity)
            .where(where)
        )
        result = await self.session.execute(query)
        return result.scalars().one_or_none()

    async def update(self, entity: T, where, **kwargs):
        query = (
            update(entity)
            .where(where)
            .values(
                updated_at=datetime.now(),
                **kwargs
            )
            .returning(entity)
        )
        result = await self.session.execute(query)
        return result.scalar()

    async def insert(self, instance: object):
        return self.session.add(instance)

    async def delete(self, entity: T, where, soft: bool = False):
        if soft:
            return await self.update(entity, where, deleted_at=datetime.now())

        query = (
            delete(entity)
            .where(where)
        )
        result = await self.session.execute(query)
        return result.rowcount
