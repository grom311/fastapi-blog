import uvicorn
from fastapi import FastAPI

from blog import models
from db.db import engine
from routers.auth import router as auth_router
from routers.blogs import router
from routers.user import router as user_router

app = FastAPI()
app.include_router(auth_router)
app.include_router(router)
app.include_router(user_router)

models.Base.metadata.create_all(engine)


if __name__ == '__main__':
    uvicorn.run("main:app",host='0.0.0.0', port=8000, reload=True)