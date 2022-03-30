from typing import List

class natural_number:
    ''' 
    Натуральное число.

    Атрибуты класса:
        digits -- список цифр числа в обратном порядке
    '''
    
    def __init__(self, x = 0):
        '''
        Конструктор числа.
        Принимает на вход x: целое положительное число в формате int,
        либо строку цифр, его представляющее, преобразовывая в массив цифр digits.
        Выполнил: Томилов Даниил
        '''
        
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
        '''
        NZER_N_B
        Проверяет, является ли число нулём.
        Выполнил: Томилов Даниил
        '''
        
        if self.digits == [0]:
            return True
        else:
            return False
    
    def add_1(self):
        '''
        ADD_1N
        Добавляет единицу к числу
        Выполнил: Томилов Даниил
        '''
        
        self.digits.append(0)
        self.digits[0] += 1
        for i in range(len(self.digits)-1):
            self.digits[i+1] += self.digits[i]//10
            self.digits[i] %= 10

        if self.digits[-1] == 0:
            self.digits.pop()

    def __str__(self) -> str:
        '''
        Возвращает str(self)
        Выполнил: Томилов Даниил
        '''
        s = ''.join(map(str, self.digits[::-1]))
        return s
    
    def __repr__(self) -> str:
        '''
        Возвращает repr(self)
        Выполнил: Томилов Даниил
        '''
        
        return f"natural_number('{str(self)}')"
    
    def __eq__(self, other):
        if type(self) == type(other):
            return self.digits == other.digits
        else:
            raise TypeError("Can't compare two natural number to not-natural'")

    def remove_leading_zeros(self):
        while self.digits[-1] == 0 and len(self.digits) > 1:
            self.digits.pop()

def nat_sum(n1, n2):
    '''
    ADD_NN_N
    Складывает два натуральных числа
    Выполнил: Томилов Даниил
    '''
    if nat_cmp(n1, n2):
        n1, n2 = n2, n1
    
    n2.digits.append(0)
    
    for i in range(len(n1.digits)):
        n2.digits[i] = n2.digits[i]+n1.digits[i]
        n2.digits[i+1] += n2.digits[i] // 10
        n2.digits[i] %= 10

    while i < len(n2.digits)-1:
        n2.digits[i+1] += n2.digits[i] // 10
        n2.digits[i] %= 10
        i += 1

    n2.remove_leading_zeros()
    
    return n2
    #тут дальше весь нужный код со всеми нужными комментариями

def nat_sub(n1, n2):
    '''
    SUB_NN_N
    Вычитание из большего натурального меньшее
    n1 > n2
    return n1 - n2
    '''
    
    if nat_cmp(n1, n2) == 1:
        raise ValueError("n1 должно быть больше n2")

    while len(n2.digits) < len(n1.digits):
        n2.digits.append(0)
    
    for i in range(len(n1.digits)):
        if n1.digits[i] < n2.digits[i]:
            n1.digits[i+1] -= 1
            n1.digits[i] += 10
        n1.digits[i] -= n2.digits[i]
    
    n1.remove_leading_zeros()
    
    return 0
    

def nat_cmp(n1,n2):
    '''
    COM_NN_D
    Сравнение двух чисел
    return 0: n1 == n2
    return 1: n1 < n2
    return 2: n1 > n2
    Выполнил: Томилов Даниил
    '''
    
    if len(n1.digits) > len(n2.digits):
        return 2
    elif len(n1.digits) < len(n2.digits):
        return 1
    else:
        i = len(n1.digits)-1
        
        if n1.digits == n2.digits:
            return 0
        
        #ищем первую несовпадающую цифру
        while n1.digits[i] == n2.digits[i]:
            i -= 1

        return 2 if n1.digits[i] > n2.digits[i] else 1