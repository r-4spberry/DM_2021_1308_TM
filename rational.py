from integer import *
from natnum import *

class RationalNumber():
    """
        Рациональное число.

        Атрибуты класса:
            numer -- числитель рационального числа
            denom -- знаменатель рационального числа
    """

    def __init__(self, x=0, y=0):
        """
        Конструктор числа.
        Принимает на вход пару чисел (x, y): x - целое число в формате int, либо строка цифр(числитель дроби);
        приводится к целому типу и записывается в атрибут numer;
        y - натуральное число в формате int, либо строка цифр(знаменатель дроби);
        приводится к натуральному типу и записывается в атрибут denom;

        Выполнил:   Пакулов Илья
        """

        if type(x) != int and type(x) != str:
            raise TypeError("аргумент должен быть либо целым числом в формате int, либо строкой, его представляющей")
        if type(y) != int and type(y) != str:
            raise TypeError("аргумент должен быть либо целым числом в формате int, либо строкой, его представляющей")


        self.numer = ABS_Z_N(Integer(x))
        self.denom = NaturalNumber(y)
        self.sign = '-' == x.__str__()[0]


    def __str__(self) -> str:
        """
        Возвращает str(self)

        Выполнил: Пакулов Илья
        """

        s = '(' + ("-" if self.sign else "") + str(self.numer) + ';' + str(self.denom) + ')'
        return s

    def __repr__(self) -> str:
        """
        Возвращает repr(self)
        s
        Выполнил: Пакулов Илья
        """

        return f"RationalNumber{str(self)}"

def RED_Q_Q(q1):
    """
    Принимает рациональное число - дробь вида (z;n), где z - целое, n - натуральное
    Сокращает дробь
    Выполнил: Пакулов Илья
    """

    if type(q1) != RationalNumber:
        raise TypeError("аргумент должен быть рациональным числом (дробью вида (z, n), где z - целое число, n - натуральное")
    q1 = copy.deepcopy(q1)

    z = NaturalNumber(q1.numer.__str__())
    n = NaturalNumber(q1.denom.__str__())
    if not(z.is_zero()) and not(n.is_zero()):
        gcc = nat_gcd(z, n)
        answer = RationalNumber(nat_div(z, gcc).__str__(), nat_div(n, gcc).__str__())
    elif z.is_zero() and not(n.is_zero()):
        answer = RationalNumber(0, int(n.__str__()))
    else:
        raise ValueError("значение знаменателя должно быть натуральным числом")
    answer.sign = q1.sign
    return answer

def INT_Q_B(q1) -> bool:
    """
        Принимает рациональное число - дробь вида (z;n), где z - целое, n - натуральное
        Возвращает 1, если число является целым, иначе - 0
        Выполнил: Пакулов Илья
    """

    if type(q1) != RationalNumber:
        raise TypeError("аргумент должен быть рациональным числом (дробью вида (z, n), где z - целое число, n - натуральное")
    answer = False
    if q1.numer == 0:
        answer = True
    else:
        q1 = copy.deepcopy(q1)
        red = RED_Q_Q(q1)
        if red.denom == 1:
            answer = True
    return answer

def TRANS_Z_Q(z1):
    """
        Принимает целое число
        Преобразует его в рациональное (т.е. вида (z, n), где z - целое, n - натуральное) и возвращает его
        Выполнил: Пакулов Илья
    """

    if type(z1) != Integer:
        raise TypeError("аргумент должено быть целым числом")
    q1 = RationalNumber(int(z1.__str__()), 1)
    q1.sign = z1.sign
    return q1

def TRANS_Q_Z(q1):
    """
        Принимает рациональное число - дробь вида (z;n), где z - целое, n - натуральное
        Преобразует его в целое и возвращает
        Выполнил: Пакулов Илья
    """

    if type(q1) != RationalNumber:
        raise TypeError("аргумент должен быть рациональным числом (дробью вида (z, n), где z - целое число, n - натуральное")
    if q1.numer == 0:
        z1 = Integer(0)
    else:
        q1 = copy.deepcopy(q1)
        q1 = RED_Q_Q(q1)
        if q1.denom == 1:
            z1 = Integer(q1.numer.__str__())
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

    if type(q1) != RationalNumber or type(q2) != RationalNumber:
        raise TypeError("аргумент должен быть рациональным числом (дробью вида (z, n), где z - целое число, n - натуральное")
    q1 = copy.deepcopy(q1)
    q2 = copy.deepcopy(q2)
    z1 = Integer(q1.numer.__str__())
    z1.sign = q1.sign
    z2 = Integer(q2.numer.__str__())
    z2.sign = q2.sign
    n1 = NaturalNumber(q1.denom.__str__())
    n2 = NaturalNumber(q2.denom.__str__())
    n = nat_lcm(n1, n2)
    mult1 = Integer(nat_div(n, n1).__str__())
    mult2 = Integer(nat_div(n, n2).__str__())
    z1 = MUL_ZZ_Z(mult1, z1)
    z2 = MUL_ZZ_Z(mult2, z2)
    sm = ADD_ZZ_Z(z1, z2)
    answer = RationalNumber(ABS_Z_N(sm).__str__(), n.__str__())
    answer.sign = sm.sign
    answer = RED_Q_Q(answer)
    return answer

def SUB_QQ_Q(q1, q2):
    """
        Принимает 2 рациональных числа - дроби вида (z;n), где z - целое, n - натуральное
        Возвращает сокращенный результат вычитания дробей
        Выполнил: Пакулов Илья
    """

    if type(q1) != RationalNumber or type(q2) != RationalNumber:
        raise TypeError("аргумент должен быть рациональным числом (дробью вида (z, n), где z - целое число, n - натуральное")
    q1 = copy.deepcopy(q1)
    q2 = copy.deepcopy(q2)
    z1 = Integer(q1.numer.__str__())
    z1.sign = q1.sign
    z2 = Integer(q2.numer.__str__())
    z2.sign = q2.sign
    n1 = NaturalNumber(q1.denom.__str__())
    n2 = NaturalNumber(q2.denom.__str__())
    n = nat_lcm(n1, n2)
    mult1 = Integer(nat_div(n, n1).__str__())
    mult2 = Integer(nat_div(n, n2).__str__())
    z1 = MUL_ZZ_Z(mult1, z1)
    z2 = MUL_ZZ_Z(mult2, z2)
    z = SUB_ZZ_Z(z1, z2)
    answer = RationalNumber(z.__str__(), n.__str__())
    answer.sign = z.sign
    answer = RED_Q_Q(answer)
    return answer

def MUL_QQ_Q(q1, q2):
    """
            Принимает 2 рациональных числа - дроби вида (z;n), где z - целое, n - натуральное
            Возвращает сокращенный результат умножения дробей
            Выполнил: Пакулов Илья
    """

    if type(q1) != RationalNumber or type(q2) != RationalNumber:
        raise TypeError("аргумент должен быть рациональным числом (дробью вида (z, n), где z - целое число, n - натуральное")
    q1 = copy.deepcopy(q1)
    q2 = copy.deepcopy(q2)
    z1 = Integer(q1.numer.__str__())
    z1.sign = q1.sign
    z2 = Integer(q2.numer.__str__())
    z2.sign = q2.sign
    n1 = NaturalNumber(q1.denom.__str__())
    n2 = NaturalNumber(q2.denom.__str__())
    z = MUL_ZZ_Z(z1, z2)
    n = nat_mul(n1, n2)
    answer = RationalNumber(z.__str__(), n.__str__())
    answer = RED_Q_Q(answer)
    return answer

def DIV_QQ_Q(q1, q2):
    """
            Принимает 2 рациональных числа - дроби вида (z;n), где z - целое, n - натуральное
            Возвращает сокращенный результат деления дробей
            Выполнил: Пакулов Илья
    """

    if type(q1) != RationalNumber or type(q2) != RationalNumber:
        raise TypeError("аргумент должен быть рациональным числом (дробью вида (z, n), где z - целое число, n - натуральное")
    q1 = copy.deepcopy(q1)
    q2 = copy.deepcopy(q2)
    z1 = Integer(q1.numer.__str__())
    z1.sign = q1.sign
    n2 = Integer(q2.numer.__str__())
    if n2.is_zero():
        raise TypeError("Знаменатель должен быть отличен от нуля")
    z2 = NaturalNumber(q2.denom.__str__())
    z2 = TRANS_N_Z(z2)
    n2 = TRANS_Z_N(n2)
    z2.sign = q2.sign
    q2 = RationalNumber(int(z2.__str__()), int(n2.__str__()))
    answer = MUL_QQ_Q(q1, q2)
    answer = RED_Q_Q(answer)
    return answer

def main():
    a, b = map(int, input("Enter first drob: ").split())
    q1 = RationalNumber(a, b)
    a, b = map(int, input("Enter second drob: ").split())
    q2 = RationalNumber(a, b)
    print(q2.__repr__())
    print(DIV_QQ_Q(q1, q2))

if __name__ == '__main__':
    main()