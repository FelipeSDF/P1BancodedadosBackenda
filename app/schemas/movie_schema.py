from pydantic import BaseModel

class Movie(BaseModel):
    title: str
    director: str
    genre: str
    release_year: int
