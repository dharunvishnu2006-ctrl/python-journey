import secrets
import hashlib
import os

api_key = secrets.token_hex(32)
print(f"API Key: {api_key}")

otp = secrets.token_hex(3) 
print(f"OTP: {otp}")

def hash_password(password):
    salt = secrets.token_hex(16) 
    hashed = hashlib.sha256(f"{salt}{password}".encode()).hexdigest()
    return salt, hashed

def verify_password(password, salt, hashed):
    check = hashlib.sha256(f"{salt}{password}".encode()).hexdigest()
    return check == hashed

password = "CloudShield@2025"
salt, hashed = hash_password(password)
print(f"\nOriginal: {password}")
print(f"Salt: {salt}")
print(f"Hashed: {hashed}")
print(f"Verify correct: {verify_password(password, salt, hashed)}")
print(f"Verify wrong: {verify_password('wrongpass', salt, hashed)}")

from dotenv import load_dotenv

load_dotenv()

api_key = os.environ.get('API_KEY', 'not_found')
db_pass = os.environ.get('DB_PASSWORD', 'not_found')

print(f"\nAPI Key from env: {api_key}")
print(f"DB Password from env: {db_pass}")