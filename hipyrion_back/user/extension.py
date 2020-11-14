from sqlalchemy.orm.session import Session
from hipyrion_back.database import get_db
from fastapi_login import LoginManager
import os
from ..models import User

SECRET_KEY = os.getenv('SECRET_KEY', 'hard-to-guess')
login_manager = LoginManager(SECRET_KEY, tokenUrl='/auth/token')
db = get_db()

@login_manager.user_loader
def load_user(db: Session, username: str):
    return db.query(User).filter(User.username==username).first()
