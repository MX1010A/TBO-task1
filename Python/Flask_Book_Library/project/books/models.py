from project import db, app
import re


def validate_text(value):
    if value is None:
        return value

    if not isinstance(value, str):
        raise ValueError("Value must be a string")

    # Check for HTML tags
    forbidden_patterns = [
        r"<[^>]*>",
        r"javascript\s*:",
        r"on\w+\s*="
    ]

    for pattern in forbidden_patterns:
        if re.search(pattern, value, re.IGNORECASE):
            raise ValueError("Invalid characters or HTML content detected")

    return value


# Book model
class Book(db.Model):
    __tablename__ = 'books'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True, index=True)
    author = db.Column(db.String(64))
    year_published = db.Column(db.Integer) 
    book_type = db.Column(db.String(20))
    status = db.Column(db.String(20), default='available')

    def __init__(self, name, author, year_published, book_type, status='available'):
        self.name = validate_text(name)
        self.author = validate_text(author)
        self.year_published = year_published
        self.book_type = book_type
        self.status = status

    def validate(self):
        self.name = validate_text(self.name)
        self.author = validate_text(self.author)

    def __repr__(self):
        return f"Book(ID: {self.id}, Name: {self.name}, Author: {self.author}, Year Published: {self.year_published}, Type: {self.book_type}, Status: {self.status})"


with app.app_context():
    db.create_all()