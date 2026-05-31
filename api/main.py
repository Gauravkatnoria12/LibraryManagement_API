from fastapi import FastAPI

from routes.book import route

app = FastAPI()
app.include_router(route)


@app.get("/")
def message():
  return {"Message": "Welcome"}