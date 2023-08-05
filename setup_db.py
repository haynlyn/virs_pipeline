# this file was designed not to be run directly, but loaded into subsequent files, which then run this
# creates database and necessary table for assessment.
# this can be called multiple times as default behavior is to not attempt creation if table exists

from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, Date, Boolean

engine = create_engine("postgresql+psycopg2://postgres@localhost:5432/postgres", echo=False)

meta = MetaData()

inspections = Table(
    'inspections', meta,
    Column('vehicle_id', Integer, nullable=False, primary_key=True),
    Column('inspection_date', Date, nullable=False, primary_key=True),
    Column('vehicle_org_id', Integer, nullable=False),
    Column('org_name', String, nullable=False),
    Column('inspection_period_id', Integer, nullable=True),
    Column('inspection_passed', Boolean, nullable=True)
    )

meta.create_all(engine)
