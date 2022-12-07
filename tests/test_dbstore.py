import asyncio
from logging import Logger
from sqlalchemy import create_engine
from sqlalchemy import text
import pytest
from src.sql_dbstore import SQLdbStore
import logging.config
import yaml

# logger
with open('../src/loggingConfig.yaml', 'r') as configFile:
    config = yaml.safe_load(configFile.read())
    logging.config.dictConfig(config)

logger: Logger = logging.getLogger(__name__)

# Initialize sqlite3 DB
sample_metadata: str = "{ item_name: Pixelmon }"

engine = create_engine("sqlite+pysqlite:///memory:", echo=True, future=True)
with engine.connect() as conn:
    conn.execute(text("CREATE TABLE IF NOT EXISTS metadata (item_id INTEGER, metadata_content TEXT)"))
    conn.execute(text("INSERT INTO metadata (item_id, metadata_content) VALUES (:x, :y)"), [{"x": 1375, "y": sample_metadata}])
    conn.commit()


@pytest.mark.asyncio
async def test_dbstore_with_test_metadata():
    db_store = SQLdbStore(engine,
                          lambda item_id: "SELECT metadata_content FROM metadata WHERE item_id = '" + item_id + "'",
                       "metadata_content",
                          logger)
    foundText = await asyncio.gather(db_store.retrieve_metadata("1375"))
    assert foundText[0][0] == sample_metadata