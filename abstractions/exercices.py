
import math


# BEGIN (write your solution here)
def make_rational(numer, denom):
    division = math.gcd(numer, denom)
    return {'numer': numer // division, 'denom': denom // division,}


def get_numer(rational):
    return rational['numer']


def get_denom(rational):
    return rational['denom']


def get_nok(d1, d2):
    return d1 * d2 // math.gcd(d1, d2)


def get_numer_for_nok(r, nok):
    return get_numer(r) * (nok // get_denom(r))


def sub(r1, r2):
    nok = get_nok(get_denom(r1), get_denom(r2))
    temp_numer1 = get_numer_for_nok(r1, nok)
    temp_numer2 = get_numer_for_nok(r2, nok)
    return make_rational(temp_numer1 - temp_numer2, nok)


def add(r1, r2):
    nok = get_nok(get_denom(r1), get_denom(r2))
    temp_numer1 = get_numer_for_nok(r1, nok)
    temp_numer2 = get_numer_for_nok(r2, nok)
    return make_rational(temp_numer1 + temp_numer2, nok)
# END


def rat_to_string(rat):
    return "{}/{}".format(get_numer(rat), get_denom(rat))

