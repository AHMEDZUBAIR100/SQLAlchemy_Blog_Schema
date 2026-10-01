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

class Post(Base):
    __tablename__ = "posts"
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(
        String(200)
    )
    content: Mapped[str]

    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id")
    )
    author: Mapped["User"] = relationship(
        back_populates="posts"
    )
    comments: Mapped[list["Comment"]] = relationship(
        back_populates="post"
    )

class Comment(Base):
    __tablename__ = "comments"
    id: Mapped[int] = mapped_column(primary_key=True)
    content: Mapped[str]
    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id")
    )
    post_id: Mapped[int] = mapped_column(
        ForeignKey("posts.id")
    )
    author: Mapped["User"] = relationship(
        back_populates="comments"
    )
    post: Mapped["Post"] = relationship(
        back_populates="comments"
    )