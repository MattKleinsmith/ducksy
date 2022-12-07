from app import app
from app.models import db, User
from datetime import datetime
from dotenv import load_dotenv
load_dotenv()

with app.app_context():
    db.drop_all()
    db.create_all()

    ###########
    ## Users ##
    ###########

    user1 = User(display_name="Margot",
                 email="email@email.com",
                 password="password")
    user2 = User(display_name="Marshall",
                 email="email2@email.com",
                 password="password")
    db.session.add_all([user1, user2])
    db.session.commit()

    ##############
    ## Products ##
    ##############
