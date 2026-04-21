try:
    try:
        num = int("abc")
    except ValueError as e:
        raise TypeError("type error occured!")from e
except TypeError as e:
    print("error:",e) 
    print("caused by:",e.__cause__)           