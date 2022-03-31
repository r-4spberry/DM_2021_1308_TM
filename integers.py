import copy

class Integer:
    """
    Целое число со знаком
    digits: массив цифр числа в обратном порядке
    sign: 0 - если положительное, 1 - если отрицательное
    """
    
    def __init__(self, x = 0):
        """
        Конструктор числа.
        Принимает на вход x: целое число в формате int,
        либо строку цифр, его представляую, преобразовывая в
        массив цифр digits и определяя знак sign
        
        Выполнил: 
        """
        
        dig = "0123456789"
        
        if type(x) != int and type(x) != str:
            raise TypeError("аргумент должен быть либо целым числом в формате int, либо строкой, его представляющей")
        
        if type(x) == int:
            x = str(x)
            
        #определение знака
        self.sign = "-" == x[0]
        if x[0] == "+" or x[0] == "-":
            x = x[1:]
        
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
                raise ValueError(f"invalid digit for an integer: '{i}'")
    
    def __str__(self) -> str:
        """
        Возвращает str(self)
        
        Выполнил: Томилов Даниил
        """
        s = ("-" if self.sign else "")+''.join(map(str, self.digits[::-1]))
        return s
    
    def __repr__(self) -> str:
        """
        Возвращает repr(self)
        s
        Выполнил: Томилов Даниил
        """
        
        return f"Integer('{str(self)}')"