from fastapi import FastAPI
from routers.movie_router import router

app = FastAPI()
app.include_router(router)

@app.get("/")
def home():
    return {"Message": "Movies API"}
