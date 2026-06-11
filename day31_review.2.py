import secrets

def generate_otp():
    return secrets.token_hex(3)  

def generate_api_key():
    return secrets.token_hex(32)  
print("Generated OTPs:")
for i in range(3):
    print(f"OTP {i+1}: {generate_otp()}")

print("\nGenerated API Key:")
print(generate_api_key())