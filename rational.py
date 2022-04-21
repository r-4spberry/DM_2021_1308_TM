# =============================================================================================================
#		 Программный модуль для выполнения вычислений над рациональными числами
# =============================================================================================================
#		 @version   2.0
#		 @author    Пакулов Илья, гр. 1308
# =============================================================================================================


from integer import *
from natnum import *


class RationalNumber():
    """
        Рациональное число.

        Атрибуты класса:
            numer -- натуральный числитель рационального числа.
            denom -- натуральный знаменатель рационального числа.
            sign  -- знак рационального числа. 1 - отрицательное, 0 - положительное
    """

    def __init__(self, x=0, y=1):
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


        self.numer = ABS_Z_N(Integer(x))    # числитель
        self.denom = NaturalNumber(y)   # знаменатель
        
        if self.denom == NaturalNumber(0):
            raise ZeroDivisionError("Знаменатель не может равняться нулю")
        
        self.sign = '-' == x.__str__()[0]   # знак

    def __str__(self) -> str:
        """
        Возвращает str(self)

        Выполнил: Пакулов Илья
        """
        if self.numer != NaturalNumber(0):
            s = ("-" if self.sign else "") + str(self.numer) + '/' + str(self.denom)
        else:
            s = "0"
        return s

    def __repr__(self) -> str:
        """
        Возвращает repr(self)
        
        Выполнил: Пакулов Илья
        """

        return "RationalNumber("+("-" if self.sign else "")+f"{self.numer},{self.denom})"


def RED_Q_Q(q1):
    """
    Принимает рациональное число - дробь вида (z;n), где z - целое, n - натуральное
    Сокращает дробь
    
    Выполнил: Пакулов Илья
    """

    if type(q1) != RationalNumber:
        raise TypeError("аргумент должен быть рациональным числом (дробью вида (z, n), где z - целое число, n - натуральное")

    z = NaturalNumber(q1.numer.__str__())
    n = NaturalNumber(q1.denom.__str__())
    # если и числитель, и знаменатель не равны 0
    if not(z.is_zero()) and not(n.is_zero()):
        gcc = nat_gcd(z, n)     # НОД числителя и знаменателя
        answer = RationalNumber(nat_div(z, gcc).__str__(), nat_div(n, gcc).__str__())
    # если числитель равен 0
    elif z.is_zero() and not(n.is_zero()):
        answer = RationalNumber(0, int(n.__str__()))
    # если знаменатель равен 0
    else:
        raise ZeroDivisionError("Знаменатель не может равняться нулю")
    answer.sign = q1.sign   # запоминаем знак
    return answer


def INT_Q_B(q1):
    """
        Принимает рациональное число - дробь вида (z;n), где z - целое, n - натуральное
        Возвращает 1, если число является целым, иначе - 0
        
        Выполнил: Пакулов Илья
    """

    if type(q1) != RationalNumber:
        raise TypeError("аргумент должен быть рациональным числом (дробью вида (z, n), где z - целое число, n - натуральное")
    answer = False
    # если числитель равен нулю
    if q1.numer == 0:
        answer = True
    else:
        q1 = RationalNumber(str(q1.numer), str(q1.denom))
        red = RED_Q_Q(q1)   # сокращаем
        # проверяем на целое
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
        raise TypeError("аргумент должен быть целым числом")
    q1 = RationalNumber(int(z1.__str__()), 1)   # преобразуем в дробь
    q1.sign = z1.sign   # запоминаем знак
    return q1


def TRANS_Q_Z(q1):
    """
        Принимает рациональное число - дробь вида (z;n), где z - целое, n - натуральное
        Преобразует его в целое и возвращает
        
        Выполнил: Пакулов Илья
    """

    if type(q1) != RationalNumber:
        raise TypeError("аргумент должен быть рациональным числом (дробью вида (z, n), где z - целое число, n - натуральное")
    # если числитель равен 0, сразу присваиваем 0
    if q1.numer == 0:
        z1 = Integer(0)
    # иначе
    else:
        q1 = copy.deepcopy(q1)
        q1 = RED_Q_Q(q1)    # сокращаем
        if q1.denom == 1:
            z1 = Integer(q1.numer.__str__())
        else:
            raise ValueError("знаменатель дроби должен быть равен 1")
        # разбираемся со знаком
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
   
    z1 = Integer(q1.numer.__str__())
    z2 = Integer(q2.numer.__str__())
    z1.sign = q1.sign   # запоминаем знак
    z2.sign = q2.sign   # запоминаем знак
    
    n1 = NaturalNumber(q1.denom.__str__())
    n2 = NaturalNumber(q2.denom.__str__())
    
    n = nat_lcm(n1, n2)     # НОК знаменателей
    
    mult1 = Integer(nat_div(n, n1).__str__())   # делим НОК на знаменатель
    mult2 = Integer(nat_div(n, n2).__str__())   # делим НОК на знаменатель
    
    z1 = MUL_ZZ_Z(mult1, z1)    # находим числитель новой дроби
    z2 = MUL_ZZ_Z(mult2, z2)    # находим числитель новой дроби
    
    sm = ADD_ZZ_Z(z1, z2)   # сумма числителей
    
    answer = RationalNumber(ABS_Z_N(sm).__str__(), n.__str__())
    answer.sign = sm.sign   # запоминаем знак
    answer = RED_Q_Q(answer)    # сокращаем
    
    return answer


def SUB_QQ_Q(q1, q2):
    """
        Принимает 2 рациональных числа - дроби вида (z;n), где z - целое, n - натуральное
        Возвращает сокращенный результат вычитания дробей
        
        Выполнил: Пакулов Илья
    """

    if type(q1) != RationalNumber or type(q2) != RationalNumber:
        raise TypeError("аргумент должен быть рациональным числом (дробью вида (z, n), где z - целое число, n - натуральное")
    
    q2 = copy.deepcopy(q2)
    
    #меняем знак второй дроби на противоположный
    q2.sign = 1-q2.sign
    
    answer = ADD_QQ_Q(q1, q2)
    return answer


def MUL_QQ_Q(q1, q2):
    """
            Принимает 2 рациональных числа - дроби вида (z;n), где z - целое, n - натуральное
            Возвращает сокращенный результат умножения дробей
            
            Выполнил: Пакулов Илья
    """

    if type(q1) != RationalNumber or type(q2) != RationalNumber:
        raise TypeError("аргумент должен быть рациональным числом (дробью вида (z, n), где z - целое число, n - натуральное")
    
    z1 = Integer(q1.numer.__str__())
    z2 = Integer(q2.numer.__str__())
    z1.sign = q1.sign   # запоминаем знак
    z2.sign = q2.sign   # запоминаем знак
    
    n1 = NaturalNumber(q1.denom.__str__())
    n2 = NaturalNumber(q2.denom.__str__())
    
    z = MUL_ZZ_Z(z1, z2)    # произведение числителей
    n = nat_mul(n1, n2)     # произведение знаменателей
    
    answer = RationalNumber(z.__str__(), n.__str__())
    answer = RED_Q_Q(answer)    # сокращаем
    return answer


def DIV_QQ_Q(q1, q2):
    """
            Принимает 2 рациональных числа - дроби вида (z;n), где z - целое, n - натуральное
            Возвращает сокращенный результат деления дробей
            
            Выполнил: Пакулов Илья
    """

    if type(q1) != RationalNumber or type(q2) != RationalNumber:
        raise TypeError("аргумент должен быть рациональным числом (дробью вида (z, n), где z - целое число, n - натуральное")
    z1 = Integer(q1.numer.__str__())
    z1.sign = q1.sign   # запоминаем знак
    n2 = Integer(q2.numer.__str__())
    z2 = NaturalNumber(q2.denom.__str__())
    # симуляция переворота дроби
    z2 = TRANS_N_Z(z2)
    n2 = TRANS_Z_N(n2)
    z2.sign = q2.sign
    q2 = RationalNumber(int(z2.__str__()), int(n2.__str__()))
    answer = MUL_QQ_Q(q1, q2)   # умножаем дроби
    answer = RED_Q_Q(answer)    # сокращаем
    return answer


def main():
    a, b = map(int, input("Enter first drob: ").split())
    q1 = RationalNumber(a, b)
    a, b = map(int, input("Enter second drob: ").split())
    q2 = RationalNumber(a, b)
    DIV_QQ_Q(q1, q2)
    print(q1.__str__())
    print(q2.__repr__())
    SUB_QQ_Q(q1, q2)
    print(q1.__str__())
    print(q2.__repr__())
    ADD_QQ_Q(q1, q2)
    print(q1.__str__())
    print(q2.__repr__())
    MUL_QQ_Q(q1, q2)
    print(q1.__str__())
    print(q2.__repr__())


if __name__ == '__main__':
    main()