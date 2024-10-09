import uvicorn

from fastapi import FastAPI

from src.web import explorer
from src.web import creature


app = FastAPI()


app.include_router(creature.router)
app.include_router(explorer.router)


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
