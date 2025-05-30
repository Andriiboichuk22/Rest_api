from fastapi import APIRouter, HTTPException, Query

from .book_repository import BookRepository
from .schema import BookSchema

books_router = APIRouter()

book_repo = BookRepository()


@books_router.get("/books")
async def get_all_books(
        limit: int = Query(10, ge=1, le=100),
        cursor: int = Query(0, ge=0)
):
    return await book_repo.get_books(limit=limit, cursor=cursor)


@books_router.get("/book/{book_id}")
async def get_book_by_id(book_id: str):
    book = await book_repo.get_book(book_id)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    return book


@books_router.delete("/book/{book_id}", status_code=204)
async def delete_book_by_id(book_id: str):
    if await book_repo.delete_book(book_id):
        return
    raise HTTPException(status_code=404, detail="Book not found")


@books_router.post("/books", response_model=BookSchema, status_code=201)
async def create_book(book_data: BookSchema):
    try:
        new_book = await book_repo.add_book(book_data.model_dump())
        return new_book
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))