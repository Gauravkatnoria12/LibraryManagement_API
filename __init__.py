from fastapi import FastAPI

from src.book.routes import route

version = "v1"

app = FastAPI(
  title="BookEra",
  description="A REST API for Web service.",
  version = version
)
app.include_router(route)


@app.get("/")
def message():
  return {"Message": "Welcome"}