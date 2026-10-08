from sqlalchemy import Integer, String, Boolean, DateTime, func, ForeignKey
from sqlalchemy.orm import relationship, Mapped, mapped_column

from .database import Base

class TimestampMixin:
    created_at: Mapped[DateTime] = mapped_column(
        DateTime, nullable=False, default=func.now()
    )
    updated_at: Mapped[DateTime] = mapped_column(
        DateTime, nullable=False, default=func.now(), onupdate=func.now()
    )




class Category(Base, TimestampMixin):
    
    __tablename__ = "categories"
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String(255), nullable=False, unique=True)
    
    
    todos: Mapped[list["Todo"]] = relationship("Todo", back_populates="category")
    
    
    
class Todo(Base, TimestampMixin):
    
    __tablename__ = "todos"
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    title: Mapped[str] = mapped_column(String(255), nullable=False)
    description: Mapped[str] = mapped_column(String(255), nullable=True)
    completed: Mapped[bool] = mapped_column(Boolean, default=False)
    category_id: Mapped[int] = mapped_column(Integer, ForeignKey("categories.id"), nullable=True)
    
    
    category: Mapped["Category"] = relationship("Category", back_populates="todos")
    