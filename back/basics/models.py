# -*- coding: utf-8 -*-
# Saved mode for inserting items into Digital Ocean database named Lifehacker.
from sqlalchemy import Column, MetaData, Table, create_engine
from sqlalchemy.dialects.postgresql import TEXT

metadata = MetaData()

basics = Table(
    "basics",
    metadata,
    Column("title", TEXT),
    Column("author", TEXT),
    Column("para", TEXT),
)
