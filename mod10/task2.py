import re

def check_date_format(date_string):
    """
    >>> check_date_format("20 января 1806")
    True
    >>> check_date_format("1924, July 25")
    True
    >>> check_date_format("26/09/1635")
    True
    >>> check_date_format("3.1.1506")
    True

    >>> check_date_format("25.08-1002")
    False
    >>> check_date_format("декабря 19, 1838")
    False
    >>> check_date_format("8.20.1973")
    False
    >>> check_date_format("Jun 7, -1563")
    False
    >>> check_date_format("31 февраля 2023")
    False
    >>> check_date_format("31 июня 2015")
    False
    """

    date_pattern = r"^(?:(?:0?\d|[12]\d|3[01])([\.\/-])(?:(?<!3[01][\.\/-])0?2|(?<!31[\.\/-])0?[469]|0?[^2469]|12)\1\d{4}|\d{4}([\.\/-])(?:0?2(?![\.\/-]3[01])|0?[469](?!31[\.\/-])|0?[^2469]|12)\2(?:0?\d|[12]\d|3[01])|(?:[0-2]\d|3[01]) (?:января|(?<!3[01] )февраля|марта|(?<!31 )(?:апреля|июня|сентября|ноября)|мая|июля|августа|октября|декабря) \d{4}|(?:Jan(?:uary)?|Feb(?:ruary)?(?! 3[01])|Mar(?:ch)?|(?:Apr(?:il)?|June?|Sep(?:tember)?|Nov(?:ember)?)(?! 31)|May|July?|Aug(?:ust)?|Oct(?:ober)?|Dec(?:ember)?) (?:[0-2]\d|3[01]), \d{4}|\d{4}, (?:Jan(?:uary)?|Feb(?:ruary)?(?! 3[01])|Mar(?:ch)?|(?:Apr(?:il)?|June?|Sep(?:tember)?|Nov(?:ember)?)(?! 31)|May|July?|Aug(?:ust)?|Oct(?:ober)?|Dec(?:ember)?) (?:[0-2]\d|3[01]))$"

    return bool(re.match(date_pattern, date_string))


if __name__ == "__main__":
    import doctest
    doctest.testmod()
