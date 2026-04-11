class AppError(Exception):
    pass

class ValidationError(AppError):
    pass

class AgeError(ValidationError):
    pass

class MarksError(ValidationError):
    pass

try:
    raise AgeError("Age must be 18+!")
except ValidationError as e:
    print("Validation Error:",e)

try:
    raise MarksError("Marks must be 0-100!")
except AppError as e:
    print("App Error:",e)    