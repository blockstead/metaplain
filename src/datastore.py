from abc import ABC, abstractmethod
from logging import Logger


class DataStore:
    def __init__(self, logger: Logger):
        self.logger = logger

    @abstractmethod
    async def retrieve_metadata(self, item_id) -> str:
        self.logger.debug("Retrieve metadata from datastore")
        return "NA"