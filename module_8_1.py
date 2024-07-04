def add_everything_up(a, b):
    try:
        return round(a + b, 3)
    except TypeError:
        if type(a) == str and type(b) == int or type(b) == float:
            return a + str(b)
        elif type(a) == int or type(a) == float and type(b) == str:
            return str(a) + b


print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))
