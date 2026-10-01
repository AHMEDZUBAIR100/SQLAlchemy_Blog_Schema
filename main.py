from database import engine, SessionLocal
from models import Base, User, Post, Comment


Base.metadata.create_all(engine)


with SessionLocal() as session:

    ahmed = User(
        name="Ahmed",
        email="ahmed@gmail.com"
    )
    ali = User(
        name="Ali",
        email="ali@gmail.com"
    )

    post1 = Post(
        title="Learning SQLAlchemy",
        content="SQLAlchemy is a powerful Python ORM."
    )
    post2 = Post(
        title="Learning FastAPI",
        content="FastAPI is a modern Python web framework."
    )

    ahmed.posts.append(post1)
    ali.posts.append(post2)


    comment1 = Comment(
        content="Great article!"
    )
    comment2 = Comment(
        content="Very useful explanation."
    )

    ali.comments.append(comment1)
    ahmed.comments.append(comment2)

    post1.comments.append(comment1)
    post2.comments.append(comment2)

    session.add(ahmed)
    session.add(ali)

    session.commit()

    print("Data inserted successfully!")