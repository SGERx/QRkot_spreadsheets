from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from typing import Optional

from app.crud.base import CRUDBase
from app.models.charity_project import CharityProject


class CRUDCharityProject(CRUDBase):

    async def get_project_id_by_name(
            self,
            project_name: str,
            session: AsyncSession,
    ) -> Optional[int]:
        db_project_id = await session.execute(
            select(CharityProject.id).where(
                CharityProject.name == project_name
            )
        )
        db_project_id = db_project_id.scalar() if db_project_id is not None else None
        return db_project_id

    async def get_not_used(
            self,
            session: AsyncSession,
    ):
        db_objects = await session.execute(select(self.model))
        return db_objects.scalars().first()

    @staticmethod
    async def get_projects_by_completion_rate(session: AsyncSession):
        closed_projects = await session.execute(
            select(
                CharityProject.name,
                CharityProject.description,
                CharityProject.create_date,
                CharityProject.close_date
            ).where(
                CharityProject.fully_invested.is_(True)
            ).order_by(
                CharityProject.close_date - CharityProject.create_date
            )
        )
        return closed_projects.all()


charity_project_crud = CRUDCharityProject(CharityProject)
