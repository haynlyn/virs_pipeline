import pandas as pd
from os import listdir
from setup_db import engine, inspections
from sqlalchemy.dialects.postgresql import insert
from sqlalchemy.orm import Session

def process_file(filename):
    # Extract from csv
    df = pd.read_csv(filename, delimiter='|', quotechar='"')
    df = df.fillna(-1).replace([-1], [None])
    data = df.to_dict(orient='records')

    with Session(engine) as session:
        # Upsert with PostgreSQL
        with open('upsert.sql', 'r') as upsert:
            upsert_sql = upsert.read()

        for row in data:
            result = session.execute(upsert_sql, **row)

        session.commit()

if __name__ == '__main__':
    files = sorted(['to_load/' + f for f in listdir() if f.startswith('vir_') and f.endswith('.csv')])
    for file in files:
        print(file)
        process_file(file)
