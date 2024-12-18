from fastapi import APIRouter, status, HTTPException, Depends
from typing import List
from sqlmodel.ext.asyncio.session import AsyncSession
from src.db.main import get_session
from .schemas import Book, BookUpdateModel
from .models import Book
from .service import BookService


book_router = APIRouter()
book_service = BookService()

@book_router.get("/", response_class=List[Book])
async def get_all_books(session: AsyncSession = Depends(get_session)):
    books = book_service.get_all_books(session)
    return books

@book_router.post("/", status_code=status.HTTP_201_CREATED)
async def create_a_book(book_data: Book, session: AsyncSession = Depends(get_session)) -> dict:
    new_book = book_service.create_book(book_data, session)
    return new_book

