from src.datastore import DataStore
from logging import Logger

import sqlite3
from sqlite3 import Error as Err


class SQLdbStore(DataStore):
    def __init__(self, dbconn, logger: Logger):
        super().__init__(logger)
        self.__dbconn = dbconn

    async def retrieve_metadata(self, item_id: str) -> str:
        try:
            query = self.generate_metadata_query(item_id)
            cursor = self.__dbconn.cursor()
            cursor.execute(query)
            return cursor.fetchone()[0]
        except Err as er:
            self.logger.error(f"SQLite3 error while executing {query}")
            self.logger.error('SQLite error: %s' % (' '.join(er.args)))
            self.logger.error("Exception class is: ", er.__class__)
        finally:
            pass

    def generate_metadata_query(self, item_id: str) -> str:
        query = "SELECT metadata_content FROM metadata WHERE item_id = '" + item_id + "'"
        self.logger.debug(f"{query}")
        return query
