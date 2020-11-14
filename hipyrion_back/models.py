import sqlalchemy as db
import bcrypt
from .database import Base, engine


class User(Base):
    __tablename__ = "users"
    
    id = db.Column(db.Integer, primary_key=True, index=True)
    username = db.Column(db.String(64), unique=True, index=True)
    email = db.Column(db.String(256), unique=True, index=True)
    password_hash = db.Column(db.String(256))

    def verify_password(self, password):
        return bcrypt.checkpw(password.encode(), self.password_hash.encode())

    def gen_token(self, manager):
        return manager.create_access_token(
            data=dict(sub=self.email)
        )

Base.metadata.create_all(engine)
