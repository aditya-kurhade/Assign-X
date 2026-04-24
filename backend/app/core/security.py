from passlib.context import CryptContext
import jwt

SECRET_KEY = "secret"
ALGORITHM = "HS256"

pwd = CryptContext(schemas=["bcrypt"])

def hash_password(password):
    return pwd.hash(password)

def verify_password(password, hash):
    return pwd.verify(password, hash)

def create_token(data: dict):
    return jwt.encode(data, SECRET_KEY, algorithm=ALGORITHM)