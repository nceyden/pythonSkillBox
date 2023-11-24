import re

def is_valid_password(password):
    """
    >>> is_valid_password("rtG&3FG#Tr^e")
    True
    >>> is_valid_password("a^A1@*@1Aa")
    True
    >>> is_valid_password("oF^a1D@y5%e6")
    True
    >>> is_valid_password("enroi#$*rkdeR#$*092uwedchf34tguv394h")
    True

    >>> is_valid_password("password")
    False
    >>> is_valid_password("password")
    False
    >>> is_valid_password("qwerty")
    False
    >>> is_valid_password("lOngPa$$W0Rd")
    False
    """
    #только разрешенные символы, не менне 8 символов
    if not re.match(r'^[a-zA-Z\d^$%@#&*]{8,}$', password):
        return False

    # минимум две латинские буквы в нижнем регистре
    if len(re.findall(r'[a-z]', password)) < 2:
        return False

    # минимум одна цифра
    if len(re.findall(r'\d', password)) < 1:
        return False

    # минимум три спецсимвола 
    if len(set(re.findall(r'[\^$%@#&*]', password))) < 3:
        return False

    return True

if __name__ == "__main__":
    import doctest
    doctest.testmod()
