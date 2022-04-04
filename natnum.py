from logging import raiseExceptions
from typing import List
import copy
import cProfile
class NaturalNumber:
    """ 
    Натуральное число.

    Атрибуты класса:
        digits -- список цифр числа в обратном порядке
    """
    
    def __init__(self, x = 0):
        """
        Конструктор числа.
        Принимает на вход x: целое положительное число в формате int,
        либо строку цифр, его представляющее, преобразовывая в массив цифр digits.
        
        Выполнил: Томилов Даниил
        """
        
        dig = "0123456789"
        
        if type(x) != int and type(x) != str:
            raise TypeError("аргумент должен быть либо целым положительным числом в формате int, либо строкой его цифр")
        
        if type(x) == int:
            x = str(x)
            
        #избавление от ведущих нулей
        x.lstrip("0")

        #храним цифры в обратном порядке, так как добавлять их чаще всего надо
        #будет в начало, что затратно по времени
        x = x[::-1]
        
        self.digits = []
        for i in x:
            if i in dig:
                self.digits.append(int(i))
            else:
                raise ValueError(f"invalid digit for natural number: '{i}'")

    def is_zero(self) -> bool:
        """
        NZER_N_B
        Проверяет, является ли число нулём.
        
        Выполнил: Томилов Даниил
        """
        
        if self.digits == [0]:
            return True
        else:
            return False
    
    def add_1(self):
        """
        ADD_1N
        Добавляет единицу к числу
        
        Выполнил: Томилов Даниил
        """

        #Добавление разряда
        self.digits.append(0)
        
        self.digits[0] += 1

        #Перенос единицы в старшие разряды, при надобности.
        for i in range(len(self.digits)-1):
            self.digits[i+1] += self.digits[i]//10
            self.digits[i] %= 10

        #Удаление лишнего разряда, если он ен понадобился
        if self.digits[-1] == 0:
            self.digits.pop()

    def __str__(self) -> str:
        """
        Возвращает str(self)
        
        Выполнил: Томилов Даниил
        """
        s = ''.join(map(str, self.digits[::-1]))
        return s
    
    def __repr__(self) -> str:
        """
        Возвращает repr(self)
        
        Выполнил: Томилов Даниил
        """
        
        return f"NaturalNumber('{str(self)}')"
    
    def __eq__(self, other):
        if type(self) == type(other):
            return self.digits == other.digits
        if type(other) == int:
            return self.digits == NaturalNumber(other).digits
        else:
            raise TypeError("Can't compare a natural number to this type'")

    def remove_leading_zeros(self):
        while self.digits[-1] == 0 and len(self.digits) > 1:
            self.digits.pop()
    
def nat_sum(n1, n2):
    """
    ADD_NN_N
    Складывает два натуральных числа
    
    Выполнил: Томилов Даниил
    """
    
    n2 = NaturalNumber(str(n2))

    #Ставим числа в убывающем порядке
    if nat_cmp(n1, n2) == 2:
        n1, n2 = n2, n1
    
    n2.digits.append(0)

    #Складывание чисел поциферно
    for i in range(len(n1.digits)):
        n2.digits[i] = n2.digits[i]+n1.digits[i]
        #Перенос в старший разряд
        n2.digits[i+1] += n2.digits[i] // 10
        n2.digits[i] %= 10

    #Перенос в старший разряд у следующих цифр
    while i < len(n2.digits)-1:
        n2.digits[i+1] += n2.digits[i] // 10
        n2.digits[i] %= 10
        i += 1

    n2.remove_leading_zeros()
    
    return n2
    #тут дальше весь нужный код со всеми нужными комментариями

def nat_sub(n1, n2):
    """
    SUB_NN_N
    Вычитание из большего натурального меньшее
    n1 > n2
    return n1 - n2
    
    Выполнил: Томилов Даниил
    """
    
    n1 = NaturalNumber(str(n1))
    n2 = NaturalNumber(str(n2))
    
    if nat_cmp(n1, n2) == 1:
        raise ValueError("n1 должно быть больше n2")

    #Добавление к n2 ведущих нулей
    while len(n2.digits) < len(n1.digits):
        n2.digits.append(0)
    
    for i in range(len(n1.digits)):
        if n1.digits[i] < n2.digits[i]: #Если цифра первого числа меньше цифры второго - занимаем из старшего разряда
            n1.digits[i+1] -= 1
            n1.digits[i] += 10

        n1.digits[i] -= n2.digits[i]
    
    n1.remove_leading_zeros()
    
    return n1
    

def nat_cmp(n1,n2):
    """
    COM_NN_D
    Сравнение двух чисел
    
    return 0: n1 == n2
    return 1: n1 < n2
    return 2: n1 > n2
    
    Выполнил: Томилов Даниил
    """
    
    if len(n1.digits) > len(n2.digits): #Если в первом числе больше цифр - оно больше
        return 2
    elif len(n1.digits) < len(n2.digits): #Аналогично для второго
        return 1
    else: #Если количество цифр равно
        
        i = len(n1.digits)-1
    
        if n1.digits == n2.digits: #Если числа равны, то возвращаем 0
            return 0
        
        #Ищем первую несовпадающую цифру
        while n1.digits[i] == n2.digits[i]:
            i -= 1

        return 2 if n1.digits[i] > n2.digits[i] else 1

def nat_mul_by_digit(n, d):
    """
    MUL_ND_N
    Умножение натурального числа на однозначное (цифру)
    
    n: natural_number
    d: int, 0 <= d < 10
    
    Выполнил: Томилов Даниил
    """
    
    if type(n) is not NaturalNumber:
        raise TypeError('n must be a natural number')
    if type(d) is not int:
        raise TypeError('d must be an integer')
    if d < 0 or d > 10:
        raise ValueError('d must be a digit')

    n = NaturalNumber(str(n))
    
    #Добавление разряда
    n.digits.append(0)

    #Изначально остаток равен нулю
    rem = 0
    
    #Каждое число умножается на цифру и к нему добавляется остаток с прошлого разряда,
    #после чего остаток переносится в старший разряд.
    for i in range(len(n.digits)-1): 
        n.digits[i] = n.digits[i]*d+rem
        rem = n.digits[i]//10
        n.digits[i] %= 10
    n.digits[-1] += rem

    n.remove_leading_zeros()
    
    return n

def nat_mul_by_10_pow(n, k):
    """
    MUL_Nk_N
    Умножение натурального числа на 10^k
    
    n: natural_number
    k: integer or natual_number
    
    Выполнил: Томилов Даниил
    """

    if type(n) is not NaturalNumber:
        raise TypeError('n must be a natural number')
    if type(k) is not NaturalNumber and type(k) is not int:
        raise TypeError('k must be a natural number or an integer')

    if type(k) is int:
        k = NaturalNumber(k) 
    
    n = NaturalNumber(str(n))
    k = NaturalNumber(str(k))
    
    while k != 0: #k раз приписываем к числу справа ноль. 
        n.digits.insert(0, 0)
        k = nat_sub(k, NaturalNumber(1))
    
    n.remove_leading_zeros()
    
    return n

def nat_mul(n1, n2):
    """
    Умножение натурального n1 на n2

    Выполнил: Томилов Даниил
    """
    
    if type(n1) is not NaturalNumber:
        raise TypeError('n1 must be a natural number')
    if type(n2) is not NaturalNumber:
        raise TypeError('n2 must be a natural number')
    
    
    ans = NaturalNumber()
    #Произведение чисел - это сумма произведений первого числа на каждый из разрядов второго
    #123 * 456 = 123 * (400 + 50 + 6) = 123*400 + 123*50 + 123*6
    for i in range(len(n2.digits)): 
        t = nat_mul_by_digit(n1, n2.digits[i])
        t = nat_mul_by_10_pow(t, i)
        ans = nat_sum(ans, t)
        
    return ans

def SUB_NDN_N(n1, n2, d):
    """
    Возвращает результат выражения n1-n2*d > 0
    n1: natural number
    n2: natural number
    d: integer, 0 <= d < 10
    
    Выполнил: Томилов Даниил
    """
    
    if type(n1) is not NaturalNumber:
        raise TypeError("n1 must be a natural number")
    if type(n2) is not NaturalNumber:
        raise TypeError('n2 must be a natural number')
    if type(d) is not int:
        raise TypeError('d must be an integer')
    
    if d < 0 or d >= 10:
        raise ValueError("d must be a digit")
    
    n1 = NaturalNumber(str(n1))
    n2 = NaturalNumber(str(n2))
    
    n2 = nat_mul_by_digit(n2, d)
    
    if nat_cmp(n1, n2) == 1:
        raise ValueError("result must be not-negative")
    
    n1 = nat_sub(n1, n2)
    
    return n1

def DIV_NN_Dk(n1,n2):
    """
    Вычисление первой цифры деления n1 на n2,
    домноженное на 10^k,где k - номер позиции этой цифры
    n1 >= n2
    
    Выполнил: Томилов Даниил
    """
    
    if type(n1) is not NaturalNumber:
        raise TypeError("n1 must be a natural number")
    if type(n2) is not NaturalNumber:
        raise TypeError("n2 must be a natural number")
    
    n1 = NaturalNumber(str(n1))
    
    if nat_cmp(n1, n2) == 1:
        raise ValueError("n1 must be greater than or equal to n2")
    
    if nat_cmp(n1, NaturalNumber(0)) == 0:
        raise ZeroDivisionError
    
    t = NaturalNumber(n1.digits.pop())
    while nat_cmp(t, n2) == 1:
        t.digits.insert(0, (n1.digits.pop()))
    
    ans = NaturalNumber()
    
    while True:
        try:
            t = nat_sub(t, n2)
            ans.add_1()
            
        except ValueError:
            break
    ans = nat_mul_by_10_pow(ans, len(n1.digits))
    
    return ans

def nat_div(n1, n2):
    """
    DIV_NN_N
    Частное от деления n1 на n2 с остатком
    n1 >= n2
    
    Выполнил: Томилов Даниил
    """
    
    if type(n1) is not NaturalNumber:
        raise TypeError("n1 must be a natural number")
    if type(n2) is not NaturalNumber:
        raise TypeError("n2 must be a natural number")
    
    n1 = NaturalNumber(str(n1))
    
    if nat_cmp(n1, n2) == 1:
        raise ValueError("n1 must be greater than or equal to n2")
    
    ans = NaturalNumber()
    while nat_cmp(n1, n2) != 1:
        t = DIV_NN_Dk(n1, n2)
        ans = nat_sum(ans, t)
        n1 = nat_sub(n1, nat_mul(n2, t))
    return ans

def nat_mod(n1, n2):
    """
    DIV_NN_N
    Остаток от деления n1 на n2 с остатком
    n1 >= n2
    
    Выполнил: Томилов Даниил
    """

    if type(n1) is not NaturalNumber:
        raise TypeError("n1 must be a natural number")
    if type(n2) is not NaturalNumber:
        raise TypeError("n2 must be a natural number")
    

    ans = nat_div(n1, n2)
    ans = nat_sub(n1, nat_mul(ans, n2))
    
    return ans

def nat_gcd(n1, n2):
    """
    GCF_NN_N
    НОД натуральных чисел n1 и n2
    Как минимум n1 или n2 должно не равняться нулю
    
    Выполнил: Томилов Даниил
    """
    
    if type(n1) is not NaturalNumber:
        raise TypeError("n1 must be a natural number")
    if type(n2) is not NaturalNumber:
        raise TypeError("n2 must be a natural number")
    
    n1 = NaturalNumber(str(n1))
    n2 = NaturalNumber(str(n2))
    
    if nat_cmp(n1, n2) == 1:
        t = NaturalNumber(str(n1))
        n1 = NaturalNumber(str(n2))
        n2 = t
        
    if nat_cmp(n1, NaturalNumber(0)) == 0:
        raise ValueError("at least one of n1 and n2 must be non-zero")
    
    if nat_cmp(n2, NaturalNumber(0)) == 0:
        return NaturalNumber(0)
    
    while True:
        c = nat_mod(n1, n2)
        if nat_cmp(c, NaturalNumber(0)) == 0:
            return n2
        n1 = NaturalNumber(str(n2))
        n2 = copy.deepcopy(c)
    
def nat_lcm(n1, n2):
    """
    LCM_NN_N
    НОК натуральных чисел n1 и n2
    n1 и n2 должны быть больше нуля
    
    Выполнил: Томилов Даниил
    """
    
    n1 = NaturalNumber(str(n1))
    n2 = NaturalNumber(str(n2))

    m = nat_mul(n1, n2)
    gcc = nat_gcd(n1, n2)
    if nat_cmp(gcc, NaturalNumber(0)) == 0:
        raise ValueError("n1 and n2 must be positive")
    return nat_div(m, gcc)

# def main():
#     from math import gcd, lcm
#     from random import randrange as rr
    
#     for i in range(2, 100):
#         print(i)
#         a = rr(1, i)
#         b = rr(1, i)
#         n1 = natural_number(a)
#         n2 = natural_number(b)
#         ngcc = nat_gcd(n1, n2)
#         nlcm = nat_lcm(n1, n2)
#         if ngcc != gcd(a,b) or nlcm != lcm(a,b):
#             print(a, b, ngcc, gcd(a,b), nlcm, lcm(a,b))

def main():
    print(nat_div(NaturalNumber(12345613433543521452145214535214521452145321453214532145123456134335435214521452145321453214532145321451234561343354352145214521453521452145214532145321453214512345613433543521452145214532145321453214532145),  NaturalNumber(3)))
    print(12345613433543521452145214535214521452145321453214532145123456134335435214521452145321453214532145321451234561343354352145214521453521452145214532145321453214512345613433543521452145214532145321453214532145//3)

if __name__ == '__main__':
    main()
    
