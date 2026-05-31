from pydantic import BaseModel ,Field ,ConfigDict

# Data Validation of Book

class BookBase(BaseModel):
    title : str = Field(min_length=1,max_length=100)
    author : str = Field(min_length=1,max_length=100)
    publication_year : int = Field(ge=1, le=9999)
    description : str = Field(min_length=1)

class BookCreate(BookBase):
    pass

class BookResponse(BookBase):
    model_config = ConfigDict(from_attributes=True)
    id : int