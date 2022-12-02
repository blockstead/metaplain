from abc import ABC, abstractmethod


class DataStore:
    def __init__(self, logger):
        self.logger = logger

    @abstractmethod
    def retrieve_metadata(self, item_id):
        self.logger.debug("Retrieve metadata from datastore")
        return "NA"
