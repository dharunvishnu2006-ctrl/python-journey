import secrets
import hashlib
from dotenv import load_dotenv
import os

load_dotenv()

class UserAuth:
    def __init__(self):
        self.users = {}

    def register(self, username, password):
        salt = secrets.token_hex(16)
        hashed = hashlib.sha256((salt + password).encode()).hexdigest()
        self.users[username] = {'salt': salt, 'hash': hashed}

    def login(self, username, password):
        if username not in self.users:
            return False
        salt = self.users[username]['salt']
        hashed =  self.users[username]['hash']
        check = hashlib.sha256((salt + password).encode()).hexdigest()
        return check == hashed
    def generate_session_token(self):
        return secrets.token_hex(32)

auth = UserAuth()
auth.register("dharun", "CloudShield@2025")

print(auth.login("dharun", "CloudShield@2025")) 
print(auth.login("dharun", "wrongpass"))         
print(auth.generate_session_token())             