from fastapi import FastAPI, HTTPException
# from books_service.app.book import Book # for IDE Pycharm
from app.book import Book # for Docker
books: list[Book] = [
    Book("100", "Fred Pearce", "The Coming Population Crash: and Our Planet's Surprising Future", "20$"),
    Book("101", "Thomas Robert Malthus", "An Essay on the Principle of Population (Paperback)", "30$")
]


app = FastAPI()


@app.get("/v1/book")
async def get_book():
    return books


@app.get("/v1/book/{id_}")
async def get_book_by_id(id_: str):
    result = [item for item in books if item.id == id_]
    if len(result) > 0:
        return result[0]
    raise HTTPException(status_code=404, detail="Book not found")

