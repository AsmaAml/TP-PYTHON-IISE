def convert_to_int(value):
    try :   
        return int(value)
    except ValueError :
        raise ValueError("error")
   
convert_to_int("123")
convert_to_int("abc")
   
