from app import app
from app.models import db, User
from datetime import datetime
from dotenv import load_dotenv
load_dotenv()

with app.app_context():

    ###########
    ## Users ##
    ###########

    user = User.query.filter(User.email == "email3@email.com").first()
    user.display_name = "Updated"
    db.session.commit()

    ##############
    ## Products ##
    ##############
