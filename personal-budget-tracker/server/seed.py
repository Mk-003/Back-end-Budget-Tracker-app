from random import choice as rc
from app import app
from models import db, Category, User, Transaction
from flask_bcrypt import bcrypt
from faker import Faker

with app.app_context():
 
 print('deleting.....')
 User.query.delete()
 Category.query.delete()
 Transaction.query.delete()

 fake = Faker()

 def seed_database():
    # Create a sample user
    user = User(
        username=fake.user_name(),
        email=fake.email(),
        password=bcrypt.generate_password_hash('password').decode('utf-8')
    )
    db.session.add(user)

    # Create some sample categories
    categories = [
        Category(name=fake.word()),
        Category(name=fake.word()),
        Category(name=fake.word())
    ]
    db.session.add_all(categories)

    # Create some sample transactions
    transactions = [
        Transaction(
            description=fake.sentence(),
            amount=fake.random.uniform(10, 100),
            date=fake.date_between(start_date='-1y', end_date='today'),
            category=fake.random_element(categories),
            user=user
        )
        for _ in range(10)
    ]
    db.session.add_all(transactions)

    db.session.commit()

print('seeded')