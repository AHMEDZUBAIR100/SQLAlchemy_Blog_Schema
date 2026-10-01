# SQLAlchemy Blog Schema

A minimal database schema demonstration using **SQLAlchemy 2.0 (ORMs with `Mapped` and `mapped_column`)** modeling a standard blog structure with `User`, `Post`, and `Comment` models.

## Project Structure

```text
.
├── database.py    # Engine setup and session management
├── models.py      # SQLAlchemy declarative models (User, Post, Comment)
├── main.py        # Table creation and sample data population script
├── requirements.txt
└── README.md