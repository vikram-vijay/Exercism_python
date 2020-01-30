from __future__ import division


class Rational(object):

    @staticmethod
    def gcd(x, y):
        while y:
            x, y = y, x % y
        return x

    def __init__(self, numer, denom):
        if denom == 0:
            raise ValueError("denom can not be 0")
        else:
            _gcd_num = Rational.gcd(numer, denom)
            self.numer = numer // _gcd_num
            self.denom = denom // _gcd_num

    def __eq__(self, other):
        return self.numer == other.numer and self.denom == other.denom

    def __repr__(self):
        return '{}/{}'.format(self.numer, self.denom)

    def __add__(self, other):
        return Rational(self.numer * other.denom + self.denom * other.numer, self.denom * other.denom)

    def __sub__(self, other):
        return Rational(self.numer * other.denom - self.denom * other.numer, self.denom * other.denom)

    def __mul__(self, other):
        return Rational(self.numer * other.numer, self.denom * other.denom)

    def __truediv__(self, other):
        return Rational(self.numer * other.denom, self.denom * other.numer)

    def __abs__(self):
        return Rational(self.numer * -1, self.denom) if self.numer * self.denom < 0 else Rational(self.numer,
                                                                                                  self.denom)

    def __pow__(self, power):
        if power > 0:
            return Rational(self.numer ** power, self.denom ** power)
        elif power == 0:
            return Rational(1, 1)
        else:
            return Rational(self.denom ** abs(power), self.numer ** abs(power))

    def __rpow__(self, base):
        return (base ** self.numer) ** (1 / self.denom)
