def to_rna(dna):
    d = {
        'G': 'C',
        'C': 'G',
        'T': 'A',
        'A': 'U',
    }

    res = []
    for i in dna:
        res.append(d.get(i))
    return ''.join(res)


def build_query_string(query_string):
    res = []
    for param, val in sorted(query_string.items()):
        res.append(f'{param}={val}')
    return '&'.join(res)


NUMERALS = {  # noqa: WPS407
    'M': 1000,
    'CM': 900,
    'D': 500,
    'CD': 400,
    'C': 100,
    'XC': 90,
    'L': 50,
    'XL': 40,
    'X': 10,
    'IX': 9,
    'V': 5,
    'IV': 4,
    'I': 1,
}


def to_roman(number):
    roman = ''
    for symbol, value in NUMERALS.items():
        while number >= value:
            roman += symbol
            number -= value
        if number <= 0:
            break
    return roman


def to_arabic(roman):
    arabic = 0
    temp = roman
    while len(roman):
        if NUMERALS.get(roman):
            arabic += NUMERALS[roman]
            break

        while not NUMERALS.get(temp):
            temp = temp[:-1]

        arabic += NUMERALS[temp]
        temp = roman = roman[len(temp):]
    return arabic
