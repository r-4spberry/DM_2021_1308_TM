import natnum
import copy

class Integer:
    """
    Целое число со знаком
    digits: массив цифр числа в обратном порядке
    sign: 0 - если положительное, 1 - если отрицательное
    """

    def __init__(self, x=0):
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

        # определение знака
        self.sign = "-" == x[0]
        if x[0] == "+" or x[0] == "-":
            x = x[1:]

        # избавление от ведущих нулей
        x.lstrip("0")

        # храним цифры в обратном порядке, так как добавлять их чаще всего надо
        # будет в начало, что затратно по времени
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
        s = ("-" if self.sign else "") + ''.join(map(str, self.digits[::-1]))
        return s

    def __repr__(self) -> str:
        """
        Возвращает repr(self)
        s
        Выполнил: Томилов Даниил
        """

        return f"Integer('{str(self)}')"

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
    def __eq__(self, other):
        if type(self) == type(other):
            return self.digits == other.digits
        if type(other) == int:
            return self.digits == natnum.NaturalNumber(other).digits
        else:
            raise TypeError("Can't compare a natural number to this type'")


def ABS_Z_N(i1):
    """
    ABS_Z_N
    Возвращает модуль числа
    Выполнил: Мальцев Артем
    """
    ab=i1.__str__()
    #Если отрицательный вовращаем натуральное число как строчное представление целого со второго знака
    if i1.sign:
        ab=ab[1:]
        return natnum.NaturalNumber(ab)
    #если положительное возвращаем натуральное число индитеничное целому
    else:
        return natnum.NaturalNumber(ab)

def POZ_Z_D(i1):
    """
    POZ_Z_D
    Возвращает знак числа:
    2- положительное
    1- отрицательное
    0- равный нулю
    Выполнил: Мальцев Артем
    """
    if i1.is_zero():
        return 0
    elif i1.sign:
        return 1
    else:
        return 2

def MUL_ZM_Z(i1):
    """
    MUL_ZM_Z
    Умножение целого на (-1)
    Выполнил: Мальцев Артем
    """
    #если знак отрицательный, то меняет его на положительный
    if i1.sign:
         i1.sign=0
    #если знак положительный, то меняет его на отрицательный
    else:
         i1.sign=1
    return Integer(i1.__str__())

def TRANS_N_Z(n1):
    """
    TRANS_N_Z
    Преобразование натурального в целое
    Выполнил: Мальцев Артем
    """
    if type(n1) != natnum.NaturalNumber:
        raise TypeError("Должно поступать натуральное число")
    i1 = Integer(str(n1))
    return i1

def TRANS_Z_N(i1):
    """
    TRANS_Z_N
    Преобразование положительно целого в натруальное
    Выполнил: Мальцев Артем
    """
    if type(i1) != Integer and i1.sign:
        raise TypeError("Должно поступать положительное целое число")
    n1=natnum.NaturalNumber(str(i1))
    return n1

def ADD_ZZ_Z(i1, i2):
    """
    ADD_ZZ_Z
    Сложение целых чисел
    Выполнил: Мальцев Артем
    """

    i1 = copy.deepcopy(i1)
    i2 = copy.deepcopy(i2)
    znak1 = POZ_Z_D(i1)
    znak2 = POZ_Z_D(i2)
    mod1 = ABS_Z_N(i1)
    mod2 = ABS_Z_N(i2)
    #Если оба числа отрицательны, суммируя оставляя минус
    if i1.sign and i2.sign:
        i = Integer(natnum.nat_sum(mod1, mod2).__str__())
        i.sign = i1.sign
    #Только одно число отрицатеьно
    elif i1.sign:
        #Если число с минусом больше по модулю вычитаем меньшее из большего оставляя знак минуса
        if natnum.nat_cmp(mod1, mod2) == 2:
            i = Integer(natnum.nat_sub(mod1, mod2).__str__())
            i.sign = i1.sign
        #Если число с минусом меньше по модулю вычитаем меньшее из большего сохраняя знак плюса
        elif natnum.nat_cmp(mod1, mod2) == 1:
            i = Integer(natnum.nat_sub(mod2, mod1).__str__())
        else:
            i = Integer(0)
    elif i2.sign:
        #Если число с минусом больше по модулю вычитаем меньшее из большего оставляя знак минуса
        if natnum.nat_cmp(mod1, mod2) == 1:
            i = Integer(natnum.nat_sub(mod2, mod1).__str__())
            i.sign = i2.sign
        #Если число с минусом меньше по модулю вычитаем меньшее из большего сохраняя знак плюса
        elif natnum.nat_cmp(mod1, mod2) == 2:
            i = Integer(natnum.nat_sub(mod1, mod2).__str__())
        else:
            i = Integer(0)
    else:
        i = Integer(natnum.nat_sum(mod1, mod2).__str__())
    return i
    # i1 = copy.deepcopy(i1)
    # i2 = copy.deepcopy(i2)
    # otric1 = POZ_Z_D(i1)
    # otric2 = POZ_Z_D(i2)
    # mod1=ABS_Z_N(i1)
    # mod2 = ABS_Z_N(i2)
    # fl=0
    # if nat_cmp(mod1, mod2) == 1:
    #     mod1, mod2 = mod2, mod1
    #     if otric2==1:
    #         fl=1
    # elif otric1:
    #     fl=1
    # if otric2==otric1:
    #     if otric1==1:
    #         return MUL_ZM_Z(TRANS_N_Z(nat_sum(mod1,mod2))) #если оба числа отрицательны
    #     else:
    #         return nat_sum(mod1,mod2) #если оба числа положительны
    # else:
    #     if fl==1 and mod1!=mod2:
    #         return MUL_ZM_Z(TRANS_N_Z(nat_sub(mod1, mod2))) #если числа разных знаков и отрицательное больше по модолю
    #     else:
    #         return nat_sub(mod1, mod2) #если числа разных знаков и положительное больше по модолю

def SUB_ZZ_Z(i1,i2):
    """
    SUB_ZZ_Z
    Вычетание целых чисел
    Выполнил: Мальцев Артем
    """

    i1 = copy.deepcopy(i1)
    i2 = copy.deepcopy(i2)
    znak1 = POZ_Z_D(i1)
    znak2 = POZ_Z_D(i2)
    mod1 = ABS_Z_N(i1)
    mod2 = ABS_Z_N(i2)

    if i1.sign and i2.sign: #оба отрицательные
        # Если вычетаемое число меньше, оставляем знак минуса
        if natnum.nat_cmp(mod1, mod2) == 2:
            i = Integer(natnum.nat_sub(mod1, mod2).__str__())
            i.sign = i1.sign
        # Если вычетаемое число меньше, меняем на знак плюса
        elif natnum.nat_cmp(mod1, mod2) == 1:
            i = Integer(natnum.nat_sub(mod2, mod1).__str__())
        # Если числа равны
        else:
            i = Integer(0)
    elif i1.sign: #Если  только число из которого вычетают отрицательно
        #Суммируем числа оставляя знак минуса
        i = Integer(natnum.nat_sum(mod1, mod2).__str__())
        i.sign = i1.sign
    elif i2.sign: #Если только вычетаемое число отрицательно
        #Суммируем числа оставляя знак плюс
        i = Integer(natnum.nat_sum(mod1, mod2).__str__())
    else:                               #оба положительные
        # Если вычитаемое число меньше, производим разность оставлляя знак плюса
        if natnum.nat_cmp(mod1, mod2) == 2:
            i = Integer(natnum.nat_sub(mod1, mod2).__str__())
        # Если вычитаемое число больше, производим разность оставлляя знак минуса
        elif natnum.nat_cmp(mod1, mod2) == 1:
            i = Integer(natnum.nat_sub(mod2, mod1).__str__())
            i.sign = True
        #Если числа равны
        else:
            i = Integer(0)
    return i

    # i1 = copy.deepcopy(i1)
    # i2 = copy.deepcopy(i2)
    # otric1 = POZ_Z_D(i1)
    # otric2 = POZ_Z_D(i2)
    # mod1 = ABS_Z_N(i1)
    # mod2 = ABS_Z_N(i2)
    # fl1 = 0
    # fl2=0
    # if nat_cmp(mod1, mod2) == 1:
    #     mod1, mod2 = mod2, mod1
    #     if otric1 == 1:
    #         fl1 = 1 #отрицательое меньшее
    #     if otric2 == 1:
    #         fl2 = 1 #отрицательое большее
    # elif otric2==1:
    #     fl2= 1 #отрицательое меньшее
    #     if otric1==1:
    #         fl1=1 #отрицательое большее
    # elif otric1==1:
    #         fl1=1 #отрицательое большее
    # if fl1==1:
    #     if fl2==1 and mod1!=mod2:
    #         return MUL_ZM_Z(TRANS_N_Z(nat_sub(mod1,mod2))) # из отрицательного вычитается отрицательное
    #     if fl2==0 :
    #         return MUL_ZM_Z(TRANS_N_Z(nat_sum(mod1,mod2))) # Из отрицательного вычитается положительное
    #     if mod1==mod2:
    #         return (TRANS_N_Z(nat_sub(mod1,mod2))) # два числа с одинаковым знаком и одинаковым значением
    # else:
    #     if fl2==1:
    #         return (TRANS_N_Z(nat_sum(mod1,mod2))) # Из положительного вычитают отрицательное
    #     if fl2==0 :
    #         return (TRANS_N_Z(nat_sub(mod1,mod2))) # Из положительного вычитается положительное

def MUL_ZZ_Z(i1,i2):
    """
    MUL_ZZ_Z
    Умножение целых чисел
    Выполнил: Мальцев Артем
    """
    i1 = copy.deepcopy(i1)
    i2 = copy.deepcopy(i2)
    otric1 = POZ_Z_D(i1)
    otric2 = POZ_Z_D(i2)
    mod1 = ABS_Z_N(i1)
    mod2 = ABS_Z_N(i2)
    #Если числа с одинаковыми знаками возвращаем положительное произведение
    if (otric1==1 and otric2==1) or (otric1==2 and otric2==2):
        return TRANS_N_Z(natnum.nat_mul(mod1, mod2))
    #Если числа с разными знаками возвращаем отрицательное произведение
    if (otric1 == 2 and otric2 == 1) or (otric1 == 1 and otric2 == 2):
        return MUL_ZM_Z(TRANS_N_Z((natnum.nat_mul(mod1, mod2))))
    #Если одно из чисел равно нулю возвращаем нуль
    if otric1==0 or otric2==0:
        return Integer(0)

def DIV_ZZ_Z(i1,i2):
    """
    DIV_ZZ_Z
    Частное от деления целого на целое (делитель отличен от нуля)
    Выполнил: Мальцев Артем
    """
    i1 = copy.deepcopy(i1)
    i2 = copy.deepcopy(i2)
    otric1 = POZ_Z_D(i1)
    otric2 = POZ_Z_D(i2)
    mod1 = ABS_Z_N(i1)
    mod2 = ABS_Z_N(i2)
    #Если  числитель меншье знаменателя  и знак одинаковый возвращаем нуль
    if natnum.nat_cmp(mod1, mod2) == 1 and( (otric1==1 and otric2==1) or (otric1==2 and otric2==2)):
        return Integer(0)
    # Если  числитель меншье знаменателя  и знак разный возвращаем минусс один
    elif(natnum.nat_cmp(mod1, mod2) == 1 and ((otric1 == 2 and otric2 == 1) or (otric1 == 1 and otric2 == 2))):
        return Integer(-1)
    #Если числитель нуль возвращаем нуль
    elif otric1 == 0:
        return Integer(0)
    else: #Если числитель больше знаменателя
        #Делим числа как натуральеы
        x=natnum.nat_div(mod1, mod2)
        #Если знак одинаковый возвращаем частное как целое
        if (otric1==2 and otric2==2):
            return TRANS_N_Z(x)
        if (otric1==1 and otric2==1):
            #Если делится без остатка - возвращаем результат деления модулей, иначе - на единицу больше
            if SUB_ZZ_Z(MUL_ZZ_Z(TRANS_N_Z(x),TRANS_N_Z(mod2)),TRANS_N_Z(mod1)).is_zero():
                return TRANS_N_Z(x)
            else:
                x.add_1()
                return TRANS_N_Z(x)
        if (otric1 == 1 and otric2 == 2):
            #Если разность между модуля числителя  и модулем произведения частного и знаменателя равна
            #нулю возвращаем частное с знаком минус
            #ИЛИ
            #если числа делятся без остатка возвращаем отрицательное частное
            if SUB_ZZ_Z(MUL_ZZ_Z(TRANS_N_Z(x),TRANS_N_Z(mod2)),TRANS_N_Z(mod1)).is_zero():
                return MUL_ZM_Z(TRANS_N_Z(x))
            # если числа делятся с остатком возвращаем отрицательное (частное+1)
            else:
                x.add_1()
                return MUL_ZM_Z(TRANS_N_Z(x))
        if (otric1 == 2 and otric2 == 1):
            if SUB_ZZ_Z(MUL_ZZ_Z(TRANS_N_Z(x),TRANS_N_Z(mod2)),TRANS_N_Z(mod1)).is_zero():
                return MUL_ZM_Z(TRANS_N_Z(x))
            # если числа делятся с остатком возвращаем отрицательное (частное)
            else:
                return MUL_ZM_Z(TRANS_N_Z(x))


def MOD_ZZ_Z(i1,i2):
    """
    MOD_ZZ_Z
    Остаток от деления целого на целое(делитель отличен от нуля)
    Выполнил: Мальцев Артем
    """

    i1 = copy.deepcopy(i1)
    i2 = copy.deepcopy(i2)
    
    return SUB_ZZ_Z(i1, MUL_ZZ_Z(i2, DIV_ZZ_Z(i1, i2)))






def main():
    a, b = input().split()
    i1 = Integer(a)
    i2 = Integer(b)
    print(f"{DIV_ZZ_Z(i1,i2)}")


if __name__ == '__main__':
    main()
