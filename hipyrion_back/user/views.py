import bcrypt
from fastapi.params import Depends
from fastapi_login.exceptions import InvalidCredentialsException
from sqlalchemy.orm.session import Session
from . import user_router
from .extension import load_user, login_manager
from .schemas import UserCreate, UserSchema, AuthData
from ..models import User
from ..database import get_db


@user_router.post('/register', response_model=UserSchema)
def create_account(new_user: UserCreate, db: Session = Depends(get_db)):
    user = User(
        username=new_user.username,
        email=new_user.email
    )
    passwd_salt = bcrypt.gensalt()
    user.password_hash = bcrypt.hashpw(new_user.password.encode('utf-8'), passwd_salt)
    db.add(user)
    db.commit()
    return dict(id=user.id, username=user.username, email=user.email)


@user_router.post('/auth/token')
def login_and_return_access_token(data: AuthData, db: Session = Depends(get_db)):
    username = data.username
    user = load_user(db, username)
    if user is None or (not user.verify_password(data.password)):
        raise InvalidCredentialsException
    access_token = user.gen_token(login_manager)
    return {'access_token': access_token, 'token_type': 'bearer'}
