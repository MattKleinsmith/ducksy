from app import app
from app.models import db, User
from dotenv import load_dotenv
from datetime import datetime
load_dotenv()

with app.app_context():
    db.drop_all()
    db.create_all()
    user1 = User(display_name="Margot",
                 email="test1@user.io", password="password", created_at=datetime(), updated_at=datetime())
    user2 = User(display_name="Marshall",
                 email="test2@user.io", password="password", created_at=datetime(), updated_at=datetime())
    db.session.add_all([user1, user2])
    db.session.commit()
