from fastapi import APIRouter, HTTPException, Query, status
from schemas.schema import BookCreate, BookResponse    # Schemas & Validation
from db.data import books    # Database
from typing import Optional    # Optional import

route = APIRouter(prefix="/api", tags=["api"])

# Add new Book

@route.post("/books", response_model=BookResponse, status_code=status.HTTP_201_CREATED)
def add_book(book : BookCreate):
    new_id = max(b["id"] for b in books) + 1 if books else 1
    newbook = {
        "id" : new_id,
        "title" : book.title,
        "author" : book.author,
        "publication_year" : book.publication_year,
        "description" : book.description
    }
    books.append(newbook)
    return newbook


# Delete Book by ID

@route.delete("/books/{book_id}")
def delete_books(book_id : int):
    for book in books:
        if book["id"] == book_id:
            books.remove(book)
            return {"Message" : "Book removed Succesfully"}
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")



# Get all Books

@route.get("/books", response_model=list[BookResponse])
def get_all_books():
    return books



# Get Book by ID

@route.get("/books/{book_id}", response_model=BookResponse)
def get_book(book_id : int):
    for book in books:
        if book["id"] == book_id:
            return book
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book Not Found")



# Filter Books by name or year

@route.get("/filter", response_model=list[BookResponse])
def filter_books(name: Optional[str] = Query(default=None), year: int = Query(default=None)):
    filtered = books
    if name:
        filtered = [
            item for item in filtered 
            if name.strip().lower() in item["title"].lower()
        ]

    if year:
        filtered = [
            item for item in filtered 
            if year == item["publication_year"]
        ]

    if filtered == []:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Not found")
    
    return filtered