from fastapi import FastAPI

app = FastAPI()


@app.get('/')
async def index():
    return {'qwer': {"a": 1, "b": 2}}
    