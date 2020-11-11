from pydantic import BaseModel

class UserModel(BaseModel):
    username: str
    email: str
    password: str
    password_again: str