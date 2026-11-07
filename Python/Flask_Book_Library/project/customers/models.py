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


# Customer model
class Customer(db.Model):
    __tablename__ = 'customers'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True, index=True)
    city = db.Column(db.String(64))
    age = db.Column(db.Integer)

    def __init__(self, name, city, age):
        self.name = validate_text(name)
        self.city = validate_text(city)
        self.age = age

    def validate(self):
        self.name = validate_text(self.name)
        self.city = validate_text(self.city)

    def __repr__(self):
        return f"Customer(ID: {self.id}, Name: {self.name}, City: {self.city}, Age: {self.age})"


with app.app_context():
    db.create_all()
