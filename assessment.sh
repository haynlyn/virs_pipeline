#!/bin/bash

# creates and activates virtual env, into which the necessary packages are installed
python3 -m venv virs && source ./virs/bin/activate
pip install pandas sqlalchemy psycopg2-binary

# run the assessment
python3 setup_db.py
python3 load_files.py
python3 run_reports.py
