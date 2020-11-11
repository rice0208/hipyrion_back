import bcrypt
from . import user_router
from .models import UserModel
from ..db_models import UserTable
from ..database import SessionLocal


@user_router.post('/register')
def create_account(user: UserModel):
    user = UserTable(
        username=UserModel.username,
        email=UserModel.email
    )
    passwd_salt = bcrypt.gensalt()
    user.password_hash = bcrypt.hashpw(UserModel.password, passwd_salt)