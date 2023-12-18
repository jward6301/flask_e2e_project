from flask import Flask, render_template, request
from sqlalchemy import create_engine, inspect
import os
from dotenv import load_dotenv
from pandas import read_sql
import pandas as pd

import sentry_sdk

sentry_sdk.init(
    dsn="https://10c94c263b7bd5ff9a2b8d0754624c78@o4506300835692544.ingest.sentry.io/4506418502172672",
    traces_sample_rate=1.0,
    profiles_sample_rate=1.0,
)

load_dotenv()

# Database connection settings from environment variables
DB_HOST = os.getenv("DB_HOST")
DB_DATABASE = os.getenv("DB_DATABASE")
DB_USERNAME = os.getenv("DB_USERNAME")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_PORT = int(os.getenv("DB_PORT", 3306))
DB_CHARSET = os.getenv("DB_CHARSET", "utf8mb4")

# Creating a connection string
ssl_args = {'ssl': {'fake_flag_to_enable_tls': True}}
connection_string = f'mysql+pymysql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}/{DB_DATABASE}?charset={DB_CHARSET}'
connection_string += '&'.join([f'{key}={value}' for key, value in ssl_args.items()])

# Create a database engine
db_engine = create_engine(connection_string, echo=False)

def execute_query_to_dataframe(query: str):
    return read_sql(query, db_engine)

def get_table_data(table_name, limit=50):
    query = f"SELECT * FROM {table_name} LIMIT {limit}"
    return pd.read_sql(query, db_engine)

def get_table_column_names(table_name):
    query = f"SHOW COLUMNS FROM {table_name}"
    result = db_engine.execute(query)
    return [row[0] for row in result]

# Create a flask application

app = Flask(__name__)

@app.route('/')
def mainpage():
    return render_template('base.html')

@app.route('/about')
def aboutpage():
    return render_template('about.html')

@app.route('/morbidity')
def morbidity():
    table_name = "data3"
    limit = 45
    data = get_table_data(table_name, limit=limit)
    column_names = get_table_column_names(table_name)
    return render_template('morbidity.html', column_names=column_names, data3=data.to_html())

@app.route('/mortality')
def mortality():
    table_name = "data1"
    limit = 45
    data = get_table_data(table_name, limit=limit)
    column_names = get_table_column_names(table_name)
    return render_template('mortality.html', column_names=column_names, data1=data.to_html())


@app.route('/error')
def error():
    raise Exception('This is a test error for Sentry Testing')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)