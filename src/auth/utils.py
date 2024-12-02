from passlib.context import CryptContext
from datetime import datetime, timedelta
import jwt


passwd_contex = CryptContext(schemes=["bcrypt"])

def generate_passwd_hash(password: str) -> str:
    hash = passwd_contex.hash(password)
    
    return hash

def verify_password(password: str, hash: str) -> bool:
    return passwd_contex.verify(password, hash)

def create_access_token(user_data: dict, expiry=timedelta):
    payload = {}
    
    token = jwt.encode(
        payload=payload,
    )