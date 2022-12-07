from src.datastore import DataStore
from logging import Logger

from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy import text


class SQLdbStore(DataStore):
    def __init__(self, db_engine, func, metadata_column_name: str, logger: Logger):
        super().__init__(logger)
        self.__db_engine = db_engine
        self.get_metadata_query = func
        self.metadata_column_name = metadata_column_name

    async def retrieve_metadata(self, item_id: str) -> str:
        try:
            query = self.get_metadata_query(item_id)
            self.logger.debug(f"DB query {query} found for {item_id}")
            result = "NA"
            with self.__db_engine.connect() as conn:
                row: object = conn.execute(text(query)).fetchall()
                result = row[0]
        except SQLAlchemyError as err:
            self.logger.debug(f"SQLAlchemy error while executing {query}")
            raise err
        else:
            return result
