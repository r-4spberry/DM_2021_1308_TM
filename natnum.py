from typing import List

class natural_number:
    ''' Натуральное число.

    Атрибуты класса:
        digits -- список цифр числа в обратном порядке
    '''
    
    def __init__(self, x = 0):
        '''
        Конструктор числа.
        Принимает на вход x: целое положительное число в формате int,
        либо строку цифр, его представляющее, преобразовывая в массив цифр digits.
        Выполнил:Ф.И.
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
        Выполнил: Ф.И.
        '''
        
        if self.digits == [0]:
            return True
        else:
            return False

    def __str__(self) -> str:
        '''
        Возвращает str(self)
        Выполнил: Ф.И.
        '''
        s = ''.join(map(str, self.digits[::-1]))
        return s
    
    def __repr__(self) -> str:
        '''
        Возвращает repr(self)
        Выполнил: Ф.И.
        '''
        
        return f"natural_number('{str(self)}')"
    
def nat_sum(n1, n2):
    '''
    ADD_NN_N
    Складывает два натуральных числа
    Выполнил: Ф.И.
    '''
    
    #тут дальше весь нужный код со всеми нужными комментариями
