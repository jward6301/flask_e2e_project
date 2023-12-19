from flask import Flask, render_template
from sqlalchemy import create_engine, text
import os
from dotenv import load_dotenv
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

# Creating a connection string with ssl=false
ssl_params = {'ssl': {'fake_flag_to_enable_tls': True}}
connection_string = f'mysql+pymysql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}/{DB_DATABASE}'

engine = create_engine(
    connection_string,
    connect_args=ssl_params
)

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
    with create_engine(connection_string).connect() as connection:
        query1 = text('SELECT * FROM data3')
        result1 = connection.execute(query1)
        db_data1 = result1.fetchall()
    return render_template('morbidity.html', data3=db_data1)

@app.route('/mortality')
def mortality():
    with create_engine(connection_string).connect() as connection:
        query2 = text('SELECT * FROM data1')
        result2 = connection.execute(query2)
        db_data2 = result2.fetchall()
    return render_template('morbidity.html', data1=db_data2)

@app.route('/additionalinfo')
def additionalinfo():
    return render_template('additionalinfo.html')

@app.route('/error')
def error():
    raise Exception('This is a test error for Sentry Testing')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)
