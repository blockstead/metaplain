import aiofiles
from src.datastore import DataStore
from logging import Logger


class FileStore(DataStore):
    def __init__(self, func, logger: Logger):
        super().__init__(logger)
        self.get_metadata_location = func

    async def retrieve_metadata(self, item_id) -> str:
        try:
            file_path = self.get_metadata_location(item_id)
            self.logger.debug(f"Filepath {file_path} found for {item_id}")
            async with aiofiles.open(file_path, "r") as read_file:
                content = read_file.readlines()
        except FileNotFoundError:
            self.logger.debug(f"File at {file_path} not found")
            raise FileNotFoundError
        except OSError:
            self.logger.debug(f"OSError while opening file at {file_path}")
            raise OSError
        except Exception as err:
            self.logger.debug(f"Unexpected error while opening file at {file_path}")
            raise err
        else:
            return content

