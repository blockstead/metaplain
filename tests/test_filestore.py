import asyncio
from logging import Logger

import pytest
from src.filestore import FileStore
import logging.config
import yaml

# logger
with open('../src/loggingConfig.yaml', 'r') as configFile:
    config = yaml.safe_load(configFile.read())
    logging.config.dictConfig(config)

logger: Logger = logging.getLogger(__name__)


@pytest.mark.asyncio
async def test_filestore_with_test_metadata_file():
    filestore = FileStore(lambda file_name: file_name, logger)
    foundText = await asyncio.gather(filestore.retrieve_metadata("../tests/test_nft_metadata.json"))
    logger.debug(len(foundText))


@pytest.mark.asyncio
async def test_filestore_with_wrong_filepath():
    with pytest.raises(FileNotFoundError):
        filestore = FileStore(lambda file_name: "wrong_path/" + file_name, logger)
        foundText = await asyncio.gather(filestore.retrieve_metadata("test_nft_metadata.json"))
