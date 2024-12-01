from passlib.context import CryptContext

passwd_contex = CryptContext(schemes=["bcrypt"])

def generate_passwd_hash(password: str) -> str:
    hash = passwd_contex.hash(password)
    
    return hash

def verify_password(password: str, hash: str) -> bool:
    return passwd_contex.verify(password, hash)