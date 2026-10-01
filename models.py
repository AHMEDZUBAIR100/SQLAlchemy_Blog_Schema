from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(
        String(100)
    )
    email: Mapped[str] = mapped_column(
        String(255),
        unique=True
    )
    posts: Mapped[list["Post"]] = relationship(
        back_populates="author"
    )
    comments: Mapped[list["Comment"]] = relationship(
        back_populates="author"
    )