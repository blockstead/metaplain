from http import HTTPStatus
from fastapi import FastAPI,Request


class Workflow:
    def __init__(self, logger):
        self.logger = logger

    def process(self, metadata: str):
        self.logger.debug("Processing metadata")
        return HTTPStatus.OK, "NA"

    def validate(self, item_id: str, request: Request):
        self.logger.debug("Validating metadata request")
        return HTTPStatus.OK, True