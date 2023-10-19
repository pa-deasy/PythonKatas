from dataclasses import dataclass
from typing import Dict, List, Optional, Set


# 7.5 - Online Book Reader: Design the data structures for an online book reader system.
@dataclass
class Page:
    number: int
    content: str
    comments: List[str]


@dataclass
class Book:
    id: int
    title: str
    author: str
    page_count: int
    current_page: int
    pages: Dict[int, Page]
    bookmarks: Set[int]
    

class Library:
    books: Dict[int, Book]
    

@dataclass
class User:
    id: int
    active_book_id: Optional[int]
    
    
class UserManager:
    users: Dict[int, User]
    

class OnlineReader:
    library: Library
    active_user: User
    
    def get_active_book(self) -> Book:
        return self.library.books[self.active_user.active_book_id]
    
    def get_active_page(self) -> Page:
        book = self.get_active_book()
        return book.pages[book.current_page]
    
    def bookmark_page(self) -> None:
        book = self.get_active_book()
        book.bookmarks.add(book.current_page)
        
    def turn_page_forward(self) -> None:
        book = self.get_active_book()
        book.current_page += 1
        
    def turn_page_backward(self) -> None:
        book = self.get_active_book()
        book.current_page -= 1