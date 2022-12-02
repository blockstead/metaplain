from datastore import DataStore
import json


class FileStore(DataStore):
    def __init__(self, file_path: str, logger):
        super().__init__(logger)
        self.file_path = file_path

    def retrieve_metadata(self, item_id):
        try:
            self.logger.debug(f'Loading {self.file_path}')
            with open(self.file_path, "r") as read_file:
                content = json.dumps(read_file)
        except FileNotFoundError:
            self.logger.debug(f"File {self.file_path} not found")
            raise FileNotFoundError
        except OSError:
            self.logger.debug(f"OSError while opening file {self.file_path}")
            raise OSError
        except Exception as err:
            self.logger.debug(f"Unexpected error while opening file {self.file_path}")
            raise err
        else:
            return content

