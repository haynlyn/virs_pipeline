import pandas as pd
from os import listdir
from setup_db import engine, inspections
from sqlalchemy.orm import Session

def generate_report(engine, report_query):
    with Session(engine) as session:
        report_df = pd.read_sql(report_query, engine)
        report_df.to_csv('virs_report.tsv', sep='\t', index=False)


if __name__ == '__main__':
    ''' unlike with loading files, since we're likely to have later reports,
        making it so that the reports can be written in pure SQL would be easiest
    '''
    reports = listdir('reports')
    for report in reports:
        with open('reports/' + report, 'r') as query_text:
            query = query_text.read()

        generate_report(engine, query)
