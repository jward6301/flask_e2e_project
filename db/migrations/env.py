from logging.config import fileConfig
from sqlalchemy import engine_from_config, pool
from alembic import context

from db_schema import Base
from dotenv import load_dotenv
import os

# Load environment variables from a .env file
load_dotenv()

# Database connection settings from environment variables
DB_HOST = os.getenv("DB_HOST")
DB_DATABASE = os.getenv("DB_DATABASE")
DB_USERNAME = os.getenv("DB_USERNAME")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_PORT = int(os.getenv("DB_PORT", 3306))
DB_CHARSET = os.getenv("DB_CHARSET", "utf8mb4")

# Define the database URL
url = f"mysql+pymysql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_DATABASE}?charset={DB_CHARSET}"

# Configure the SQLAlchemy engine
connect_args = {'ssl': {'fake_flag_to_enable_tls': True}}  # Adjust SSL parameters as needed
engine = engine_from_config(
    context.config.get_section(context.config.config_ini_section),
    prefix='sqlalchemy.',
    connect_args=connect_args,
    url=url,
    poolclass=pool.NullPool  # Use NullPool to prevent connection pooling during migrations
)

# Update the context configuration
context.configure(
    connection=engine.connect(),
    target_metadata=Base.metadata,
    # ... (other configurations)
)

# this is the Alembic Config object, which provides
# access to the values within the .ini file in use.
config = context.config

# Interpret the config file for Python logging.
# This line sets up loggers basically.
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# add your model's MetaData object here
# for 'autogenerate' support
# target_metadata = Base.metadata
# target_metadata = None

# other values from the config, defined by the needs of env.py,
# can be acquired:
# my_important_option = config.get_main_option("my_important_option")
# ... etc.

def run_migrations_offline() -> None:
    """Run migrations in 'offline' mode."""
    with context.begin_transaction():
        context.run_migrations()

def run_migrations_online() -> None:
    """Run migrations in 'online' mode."""
    with engine.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=Base.metadata
        )

        with context.begin_transaction():
            context.run_migrations()

if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
