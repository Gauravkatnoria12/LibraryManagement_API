from fastapi import FastAPI
from contextlib import asynccontextmanager

from .book.routes import route

version = "v1"

@asynccontextmanager
async def life_span(app: FastAPI):
  print("Server is Starting ...")
  yield
  print("Server is Stopping ...")

app = FastAPI(
  title="BookEra",
  description="A REST API for Web service.",
  version = version,
  lifespan= life_span
)
app.include_router(route)


@app.get("/")
def message():
  return {"Message": "Welcome"}