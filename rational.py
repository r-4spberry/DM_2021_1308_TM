from integer import *
from natnum import *

class RationalNumbers():
    def __init__(self, x=0, y=0):
        """
        Конструктор числа.
        Принимает на вход x: целое число в формате int,
        либо строку цифр, его представляую, преобразовывая в
        массив цифр digits и определяя знак sign

        Выполнил:   Пакулов Илья
        """

        dig = "0123456789"

        if type(x) != int and type(x) != str:
            raise TypeError("аргумент должен быть либо целым числом в формате int, либо строкой, его представляющей")
        if type(y) != int and type(y) != str:
            raise TypeError("аргумент должен быть либо целым числом в формате int, либо строкой, его представляющей")

        if type(x) == int:
            x = str(x)
        if type(y) == int:
            y = str(y)

        # определение знака
        if y[0] == '-':
            raise TypeError("знаменатель должен быть либо натуральным числом в формате int, либо строкой, его представляющей")

        self.sign = "-" == x[0]
        if x[0] == "+" or x[0] == "-":
            x = x[1:]

        # избавление от ведущих нулей
        x.lstrip("0")
        y.lstrip("0")

        # храним цифры в обратном порядке, так как добавлять их чаще всего надо
        # будет в начало, что затратно по времени
        x = x[::-1]
        y = y[::-1]

        self.numer_digits = []
        for i in x:
            if i in dig:
                self.numer_digits.append(int(i))
            else:
                raise ValueError(f"invalid digit for an integer: '{i}'")

        self.denom_digits = []
        for i in y:
            if i in dig:
                self.denom_digits.append(int(i))
            else:
                raise ValueError(f"invalid digit for an integer: '{i}'")

    def __str__(self) -> str:
        """
        Возвращает str(self)

        Выполнил: Пакулов Илья
        """
        s = '(' + ("-" if self.sign else "") + ''.join(map(str, self.numer_digits[::-1])) + ';' + ''.join(map(str, self.denom_digits[::-1])) + ')'
        return s

    def __repr__(self) -> str:
        """
        Возвращает repr(self)
        s
        Выполнил: Пакулов Илья
        """

        return f"RationalNumber({str(self)})"

def RED_Q_Q(q1):
    """
    Принимает рациональное число - дробь вида (z;n), где z - целое, n - натуральное
    Сокращает дробь
    Выполнил: Пакулов Илья
    """

    q1 = copy.deepcopy(q1)
    z = NaturalNumber(''.join(map(str, q1.numer_digits[::-1])))
    n = NaturalNumber(''.join(map(str, q1.denom_digits[::-1])))
    if not(z.is_zero()) and not(n.is_zero()):
        gcc = nat_gcd(z, n)
        answer = RationalNumbers(nat_div(z, gcc).__str__(), nat_div(n, gcc).__str__())
    elif z.is_zero() and not(n.is_zero()):
        answer = RationalNumbers(0, int(n.__str__()))
    else:
        raise TypeError("значение знаменателя должно быть натуральным числом")
    answer.sign = q1.sign
    return answer

def INT_Q_B(q1) -> bool:
    """
        Принимает рациональное число - дробь вида (z;n), где z - целое, n - натуральное
        Возвращает 1, если число является целым, иначе - 0
        Выполнил: Пакулов Илья
    """

    answer = False
    q1 = copy.deepcopy(q1)
    red = RED_Q_Q(q1)
    if red.denom_digits[0] == 1:
        answer = True
    return answer

def TRANS_Z_Q(z1):
    """
        Принимает целое число
        Преобразует его в рациональное (т.е. вида (z, n), где z - целое, n - натуральное) и возвращает его
        Выполнил: Пакулов Илья
    """

    if type(z1) != Integer:
        raise TypeError("Должно поступать целое число")
    q1 = RationalNumbers(int(z1.__str__()), 1)
    q1.sign = z1.sign
    return q1

def TRANS_Q_Z(q1):
    """
        Принимает рациональное число - дробь вида (z;n), где z - целое, n - натуральное
        Преобразует его в целое и возвращает
        Выполнил: Пакулов Илья
    """

    if type(q1) != RationalNumbers:
        raise TypeError("аргумент должен быть рациональным числом")
    if q1.numer_digits[0] == 0:
        z1 = Integer(0)
    else:
        q1 = copy.deepcopy(q1)
        q1 = RED_Q_Q(q1)
        if q1.denom_digits[0] == 1:
            z1 = Integer(''.join(map(str, q1.numer_digits)))
        else:
            raise TypeError("знаменатель дроби должен быть равен 1")
        if q1.sign:
            z1 = MUL_ZM_Z(z1)
    return z1

def ADD_QQ_Q(q1, q2):
    """
        Принимает 2 рациональных числа - дроби вида (z;n), где z - целое, n - натуральное
        Возвращает сокращенный результат сложения дробей
        Выполнил: Пакулов Илья
    """

    q1 = copy.deepcopy(q1)
    q2 = copy.deepcopy(q2)
    z1 = Integer(''.join(map(str, q1.numer_digits[::-1])))
    z1.sign = q1.sign
    z2 = Integer(''.join(map(str, q2.numer_digits[::-1])))
    z2.sign = q2.sign
    n1 = NaturalNumber(''.join(map(str, q1.denom_digits[::-1])))
    n2 = NaturalNumber(''.join(map(str, q2.denom_digits[::-1])))
    n = nat_lcm(n1, n2)
    mult1 = Integer(nat_div(n, n1).__str__())
    mult2 = Integer(nat_div(n, n2).__str__())
    z1 = MUL_ZZ_Z(mult1, z1)
    z2 = MUL_ZZ_Z(mult2, z2)
    answer = RationalNumbers(ADD_ZZ_Z(z1, z2).__str__(), n.__str__())
    answer = RED_Q_Q(answer)
    return answer

def SUB_QQ_Q(q1, q2):
    """
        Принимает 2 рациональных числа - дроби вида (z;n), где z - целое, n - натуральное
        Возвращает сокращенный результат вычитания дробей
        Выполнил: Пакулов Илья
    """

    q1 = copy.deepcopy(q1)
    q2 = copy.deepcopy(q2)
    z1 = Integer(''.join(map(str, q1.numer_digits[::-1])))
    z1.sign = q1.sign
    z2 = Integer(''.join(map(str, q2.numer_digits[::-1])))
    z2.sign = q2.sign
    n1 = NaturalNumber(''.join(map(str, q1.denom_digits[::-1])))
    n2 = NaturalNumber(''.join(map(str, q2.denom_digits[::-1])))
    n = nat_lcm(n1, n2)
    mult1 = Integer(nat_div(n, n1).__str__())
    mult2 = Integer(nat_div(n, n2).__str__())
    z1 = MUL_ZZ_Z(mult1, z1)
    z2 = MUL_ZZ_Z(mult2, z2)
    z = SUB_ZZ_Z(z1, z2)
    answer = RationalNumbers(z.__str__(), n.__str__())
    answer = RED_Q_Q(answer)
    return answer

def MUL_QQ_Q(q1, q2):
    """
            Принимает 2 рациональных числа - дроби вида (z;n), где z - целое, n - натуральное
            Возвращает сокращенный результат умножения дробей
            Выполнил: Пакулов Илья
    """

    q1 = copy.deepcopy(q1)
    q2 = copy.deepcopy(q2)
    z1 = Integer(''.join(map(str, q1.numer_digits[::-1])))
    z1.sign = q1.sign
    z2 = Integer(''.join(map(str, q2.numer_digits[::-1])))
    z2.sign = q2.sign
    n1 = NaturalNumber(''.join(map(str, q1.denom_digits[::-1])))
    n2 = NaturalNumber(''.join(map(str, q2.denom_digits[::-1])))
    z = MUL_ZZ_Z(z1, z2)
    n = nat_mul(n1, n2)
    answer = RationalNumbers(z.__str__(), n.__str__())
    answer = RED_Q_Q(answer)
    return answer

def DIV_QQ_Q(q1, q2):
    """
            Принимает 2 рациональных числа - дроби вида (z;n), где z - целое, n - натуральное
            Возвращает сокращенный результат деления дробей
            Выполнил: Пакулов Илья
    """

    q1 = copy.deepcopy(q1)
    q2 = copy.deepcopy(q2)
    z1 = Integer(''.join(map(str, q1.numer_digits[::-1])))
    z1.sign = q1.sign
    n2 = Integer(''.join(map(str, q2.numer_digits[::-1])))
    if n2.is_zero():
        raise TypeError("Знаменатель должен быть отличен от нуля")
    n1 = NaturalNumber(''.join(map(str, q1.denom_digits[::-1])))
    z2 = NaturalNumber(''.join(map(str, q2.denom_digits[::-1])))
    z2 = TRANS_N_Z(z2)
    n2 = TRANS_Z_N(n2)
    z2.sign = q2.sign
    q2 = RationalNumbers(int(z2.__str__()), int(n2.__str__()))
    answer = MUL_QQ_Q(q1, q2)
    answer = RED_Q_Q(answer)
    return answer

def main():
    a, b = map(int, input("Enter first drob: ").split())
    q1 = RationalNumbers(a, b)
    a, b = map(int, input("Enter second drob: ").split())
    q2 = RationalNumbers(a, b)
    print(SUB_QQ_Q(SUB_QQ_Q(q1, q2), ADD_QQ_Q(q1, q2)))

if __name__ == '__main__':
    main()
