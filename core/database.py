from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine

from sqlmodel.ext.asyncio.session import AsyncSession as AS
from config import settings


as_engine = create_async_engine(settings.SQLALCHEMY_DATABASE_URI_ASYNC.unicode_string())
session_maker = async_sessionmaker(bind=as_engine, autoflush=False, expire_on_commit=False, class_=AS)
