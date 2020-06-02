from settings import DATABASE
from sqlalchemy import create_engine, Column, MetaData, Table
from sqlalchemy.dialects.postgresql import TEXT
from sqlalchemy.engine.url import URL


metadata = MetaData()

def db_connect():
    """Database connection string."""
    return create_engine(URL(**DATABASE))

def create_table(engine):
    """Table creation"""
    return metadata.create_all(engine)

basics = Table(
    'basics',
    metadata,
    Column('title', TEXT),
    Column('author', TEXT),
    Column('para', TEXT),
)
