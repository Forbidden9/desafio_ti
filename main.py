import uvicorn
from fastapi import FastAPI

from config.config import settings
from db.session import Base, engine
from routers.uf.uf import uf

app = FastAPI()


def start_application():
    Base.metadata.create_all(bind=engine)
    app = FastAPI(title=settings.PROJECT_NAME, version=settings.PROJECT_VERSION)
    app.include_router(uf, tags=["uf"], prefix="/api/uf")

    @app.get("/")
    async def root():
        return "Welcome, Thanks for using SII API"

    return app


if __name__ == "__main__":
    uvicorn.run(start_application(), host="127.0.0.1", port=8000, workers=True)
