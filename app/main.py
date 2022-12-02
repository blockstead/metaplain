from fastapi import FastAPI
import logging
import logging.config
import yaml

# logger
with open('./app/loggingConfig.yaml','r') as configFile:
    config=yaml.safe_load(configFile.read())
    logging.config.dictConfig(config)

logger = logging.getLogger(__name__)

app = FastAPI()


@app.get("/")
async def root():
    logger.debug('sample log message')
    return {"message": "Hello World"}


@app.get("/health", status_code=200)
async def health():
    return "OK"
