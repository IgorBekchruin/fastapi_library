from sqlalchemy import delete, desc, insert, select, update

from src.database import async_session


class BaseService:
    model = None

    @classmethod
    async def find_all_objects(cls, limit: int = 3, offset: int = 0):
        async with async_session() as session:
            query = (
                select(cls.model)
                .order_by(desc(cls.model.id))
                .limit(limit)
                .offset(offset)
            )
            res = await session.execute(query)
            return res.scalars().all()

    @classmethod
    async def find_one_object_by_id(cls, model_id: int):
        async with async_session() as session:
            query = select(cls.model).filter_by(id=model_id)
            res = await session.execute(query)
            return res.scalars().unique().one_or_none()

    @classmethod
    async def create_object(cls, object_data):
        async with async_session() as session:
            statement = insert(cls.model).values(**object_data.dict())
            await session.execute(statement)
            await session.commit()
            return {"status": "200", "object": object_data}

    @classmethod
    async def update_object(cls, model_id: int, object_data):
        async with async_session() as session:
            statement = (
                update(cls.model)
                .where(cls.model.id == model_id)
                .values(**object_data.dict())
            )
            await session.execute(statement)
            await session.commit()
            return {"status": "200", "object": object_data}

    @classmethod
    async def delete_object(cls, model_id: int):
        async with async_session() as session:
            statement = delete(cls.model).filter_by(id=model_id)
            await session.execute(statement)
            await session.commit()
            return {"status": "200", "msg": f"Object with id={model_id} was deleted"}
