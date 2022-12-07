from fastapi import FastAPI
import logging.config
import yaml

# logger
with open('./src/loggingConfig.yaml', 'r') as configFile:
    config = yaml.safe_load(configFile.read())
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


@app.get("/get", status_code=200)
async def get():
    return "OK"


@app.get("/put", status_code=501)
async def put():
    return "ERROR"


@app.get("/patch", status_code=501)
async def patch():
    return "ERROR"


@app.get("/delete", status_code=501)
async def delete():
    return "ERROR"
