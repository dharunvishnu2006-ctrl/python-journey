import secrets
import hashlib

def hash_password(password):
    salt = secrets.token_hex(16)  
    hashed = hashlib.sha256((salt + password).encode()).hexdigest()
    return salt, hashed

def verify_password(password, salt, hashed):
    check_hash = hashlib.sha256((salt + password).encode()).hexdigest()
    return check_hash == hashed

password = "AutoPilot@2025"
salt, hashed = hash_password(password)
print("Original Password :", password)
print("Salt              :", salt)
print("Hashed Password   :", hashed)
print("Verify Correct ->", verify_password(password, salt, hashed))
print("Verify Wrong   ->", verify_password("WrongPassword", salt, hashed))