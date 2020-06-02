from sqlalchemy import create_engine, Column, MetaData, Table
from sqlalchemy.dialects.postgresql import TEXT


metadata = MetaData()

basics = Table(
    'basics',
    metadata,
    Column('title', TEXT),
    Column('author', TEXT),
    Column('para', TEXT),
)
