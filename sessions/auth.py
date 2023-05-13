import hashlib


def encode_password(password: str) -> str:
    """Hash a password for storing."""
    hashed_password = hashlib.sha256(password.encode('utf-8')).hexdigest()
    return hashed_password


def verify_password(stored_password: str, provided_password: str) -> bool:
    """Check if a provided password matches the stored hashed password."""
    hashed_provided_password = encode_password(provided_password)
    return stored_password == hashed_provided_password
