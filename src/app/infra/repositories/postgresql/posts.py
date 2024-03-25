from uuid import UUID

from sqlalchemy import (
    func,
    select,
)

from app.infra.db.models.post import Post
from app.infra.repositories.postgresql.common import CommonRepo
from app.interfaces.db.posts import IPostReader, IPostWriter


class PostReader(CommonRepo, IPostReader):
    async def get_post(self, post_id: UUID):
        query = (
            select(Post)
            .where(
                Post.id.is_(post_id)
            )
        )
        result = await self.session.execute(query)
        return result.scalars().one_or_none()

    async def get_posts(self,
                        limit: int = None,
                        offset: int = None,
                        theme: str = None):
        query = (
            select(Post).where(Post.theme_id.is_(theme))
            .order_by(self.latest_date(entity=Post).desc()
                      .limit(limit)
                      .offset(offset))
        )
        result = await self.session.execute(query)
        total_qty = await self.session.execute(
            select(func.count()),
        )
        result = await self.session.execute(query)
        return result.scalars().all(), total_qty.scalar_one()


class PostWriter(CommonRepo, IPostWriter):
    async def create_post(self, instance: Post):
        await self.insert(instance=instance)
