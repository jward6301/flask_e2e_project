from sqlalchemy import create_engine, inspect, Column, BigInteger, Integer, String, Text, Float
from sqlalchemy.ext.declarative import declarative_base
import os
from dotenv import load_dotenv

# Load environment variables from a .env file
load_dotenv()

# Database connection settings from environment variables
DB_HOST = os.getenv("DB_HOST")
DB_DATABASE = os.getenv("DB_DATABASE")
DB_USERNAME = os.getenv("DB_USERNAME")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_PORT = int(os.getenv("DB_PORT", 3306))
DB_CHARSET = os.getenv("DB_CHARSET", "utf8mb4")

# Define the base class for declarative models
Base = declarative_base()

class data1(Base):
    __tablename__ = 'data1'

    my_row_id = Column(BigInteger, primary_key=True, autoincrement=True, nullable=False)
    Year = Column(Integer, default=None)
    Related = Column(Text)
    Underlying_cause = Column(Text)
    Race_ethnicity = Column(Text)
    Borough = Column(Text)
    Deaths = Column(Integer, default=None)

class data3(Base):
    __tablename__ = 'data3'
    my_row_id = Column(BigInteger, primary_key=True, autoincrement=True, nullable=False)
    Year = Column(Integer, default=None)
    Race_ethnicity = Column(Text)
    Education = Column(Text)
    Borough = Column(Text)
    Nativity = Column(Text)
    Age = Column(Text)
    Insurance = Column(Text)
    Trimester = Column(Text)
    Diabetes = Column(Text)
    Hypertension = Column(Text)
    Heart_Disease = Column(Text)
    Employed = Column(Text)
    Miscarriage = Column(Text)
    Parity = Column(Text)
    SMM = Column(Integer, default=None)
    SMM_Rate = Column(Float, default=None)

connect_args = {'ssl': {'fake_flag_to_enable_tls': True}}
connection_string = f'mysql+pymysql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_DATABASE}?charset={DB_CHARSET}'

# Create the SQLAlchemy engine
engine = create_engine(
    connection_string,
    connect_args=connect_args
)

inspector = inspect(engine)
table_names = inspector.get_table_names()
print("Tables in the database:", table_names)

# Part 3 - Create the tables using the defined models
Base.metadata.create_all(engine)

# Close the database connection explicitly
engine.dispose()

print("Tables created successfully.")