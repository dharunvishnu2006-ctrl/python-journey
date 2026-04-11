class AgeError(Exception):
    pass
def check_age(age):
    if age < 18:
        raise AgeError("age must be 18 or above!")
    print("age is valid!")

try:
    check_age(19)
except AgeError as e:
    print("Error:",e)        