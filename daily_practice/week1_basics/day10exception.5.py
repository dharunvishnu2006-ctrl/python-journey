def check_marks(marks):
    assert 0 <= marks <= 100,"marks must be between 0 and 100!"
    print("valid marks:",marks)

try:
    check_marks(95)
    check_marks(50)
except AssertionError as e:
    print("error:",e)        