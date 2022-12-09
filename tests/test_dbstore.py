import asyncio
from logging import Logger
import pytest
from src.sql_dbstore import SQLdbStore
import sqlite3
from sqlite3 import Error as Err
import logging.config
import yaml

# logger
with open('../src/loggingConfig.yaml', 'r') as configFile:
    config = yaml.safe_load(configFile.read())
    logging.config.dictConfig(config)

logger: Logger = logging.getLogger(__name__)


# Constants
sample_metadata: str = "{ item_name: Pixelmon }"
sample_metadata_id: str = "1375"


# Create connection to sqlite3 DB
def create_db_connection():
    try:
        # Connecting to sqlite
        connection_obj = sqlite3.connect(':memory:')

        # cursor object
        cursor_obj = connection_obj.cursor()

        # Drop/create the metadata table
        cursor_obj.execute("DROP TABLE IF EXISTS GEEK")
        table = """ CREATE TABLE METADATA (
                    item_id INT,
                    metadata_content VARCHAR(255) NOT NULL
                ); """
        cursor_obj.execute(table)
        cursor_obj.execute("INSERT INTO METADATA VALUES ('" + sample_metadata_id + "', '" + sample_metadata + "')")
        connection_obj.commit()
    except Err:
        print(Err)
    finally:
        pass
    return connection_obj


@pytest.mark.asyncio
async def test_dbstore_with_test_metadata():
    dbconn = create_db_connection()
    db_store = SQLdbStore(dbconn, logger)
    foundText = await asyncio.gather(db_store.retrieve_metadata(sample_metadata_id))
    dbconn.close()
    assert foundText[0] == sample_metadata
