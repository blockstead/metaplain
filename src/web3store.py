from src.datastore import DataStore
from logging import Logger


class FileStore(DataStore):
    def __init__(self, func, logger: Logger):
        super().__init__(logger)
        self.get_metadata_location = func

    async def retrieve_metadata(self, item_id, func) -> str:
        pass