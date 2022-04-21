# =============================================================================================================
#		 Программный модуль для выполнения вычислений над многочленами
# =============================================================================================================
#		 @version   2.0
#		 @author    Мельник Даниил, гр. 1308
# =============================================================================================================


from typing import List
import rational
import natnum
import copy
from rational import RationalNumber


class Polynom:
    def __init__(self, coef: List[rational.RationalNumber]):
        """
        Возвращает многочлен в стандартном виде (ax^n+...+yx^1+z)
        Принимает массив чисел типа RationalNumber

        Выполнил: Мельник Даниил
        """
        if coef is None:
            coef = []
        self.coef = coef
    def __str__(self):
        """
        Возвращает repr(self)
        
        Выполнил: Томилов Даниил
        """
        s = ""
        for i in range(len(self.coef)-1, -1, -1):
            if self.coef[i].numer != 0 or len(self.coef) == 1:
                if self.coef[i].denom == 1 and self.coef[i].sign == 0:
                    s += f"{self.coef[i].numer}"
                else:
                    s += ("(" + ("-" if self.coef[i].sign == 1 else "") + f"{self.coef[i].numer}"+
                          (f"/{self.coef[i].denom}" if self.coef[i].denom != 1 else "") + ")")
                if i != 0:
                    if i != 1:
                        s += f"x^{i}+"
                    else:
                        s += f"x+"
        s = s.rstrip("+")
        return s

    def __repr__(self):
        """
        Возвращает repr(self)
        
        Выполнил: Мельник Даниил
        """
        return f"Polynom([{repr(self.coef)}])"
    
    def normalise(self):
        """
        Убирает нулевые старшие коэффициенты
        
        Выполнил: Мельник Даниил
        """
        while len(self.coef) > 1 and self.coef[-1].numer == 0:
            self.coef.pop()
        if len(self.coef) == 0:
            self.coef = [RationalNumber(0)]
 
            
def ADD_PP_P(p1, p2):
    """
    Складывает два многочлена типа Polynom
    Возвращает многочлен типа Polinom

    Выполнил: Мельник Даниил
    """
    
    p3 = Polynom([]) # создание чистого многочлена
    p2r= Polynom(p2.coef[::]) # копирование исхлдных данных для обработки
    p1r= Polynom(p1.coef[::])
    
    # дополнение меньшего многочлена до длины большего созданием нулевых коэффициентов при больших степенях
    if (len(p2r.coef)<len(p1r.coef)):
        for i in range(len(p1r.coef)-len(p2r.coef)):
            p2r.coef.append(rational.RationalNumber('0','1'))
    else:
        for i in range(len(p2r.coef)-len(p1r.coef)):
            p1r.coef.append(rational.RationalNumber('0','1'))
            
        #сложение коэффициентов многочленов с формированием нового многочлена
    for i in range (len(p1r.coef)):
        k=rational.ADD_QQ_Q(p1r.coef[i],p2r.coef[i])
        p3.coef.append(k)
        
    return p3


def SUB_PP_P(p1, p2):
    """
    Принимает многочлены р1 и р2 типа полином
    Вычитает один многочлен из другогого
    Возвращает многочлен типа Polynom

    Выполнил: Мельник Даниил
    """
    # создание чистого многочлена, копирование исходных данных
    p3=Polynom([])
    p1r=Polynom(p1.coef[::])
    p2r=Polynom(p2.coef[::])
    
    # дополнение меньшего многочлена до длины большего созданием нулевых коэффициентов при больших степенях
    if (len(p2r.coef)<len(p1r.coef)):
        for i in range(len(p1r.coef)-len(p2r.coef)):
            p2r.coef.append(rational.RationalNumber('0','1'))
    else:
        for i in range(len(p2r.coef)-len(p1r.coef)):
            p1r.coef.append(rational.RationalNumber('0','1'))

    # вычитание коэффициентов многочленов с формированием нового многочлена
    for i in range (0,len(p1r.coef)):
        if (i<len(p2r.coef)):
            k=rational.SUB_QQ_Q(p1r.coef[i],p2r.coef[i])
            p3.coef.append(k)
    return p3


def MUL_PQ_P (p1,x):
    """
    Принимает многочлен р1 типа Polynom, число х типа Rational
    Умножает многочлен на рациональное число
    Возвращает многочлен типа Polynom

    Выполнил: Мельник Даниил
    """
    #создание чистого многочлена
    p3=Polynom(p1.coef[::])
    
    #умножение каждого коэффициента многочлена на рациональное число
    for i in range(0,len(p1.coef)):
        p3.coef[i] = rational.MUL_QQ_Q(p1.coef[i], x)
    return p3


def MUL_Pxk_P (p1,k):
    """
    Принимает многочлен типа Polynom, показатель степени х - k
    Умножает многочлен p1 в на переменную в степени k
    Возвращает многочлен типа Polynom

    Выполнил: Мельник Даниил
    """
    #проверка типа поступивших данных, преобразование int в NaturalNumber
    if type(p1) is not Polynom:
        assert ValueError
    if type(k) is not int or type(k) and not natnum.NaturalNumber:
        assert ValueError
        
    if type(k) is int:
        k = natnum.NaturalNumber(k)
        
    #дополнение длины массива коэффициентов многочлена на количество элементов, равное степени х
    p3=Polynom(p1.coef[::])
    p3.coef.reverse()
    i = natnum.NaturalNumber(0)
    while natnum.nat_cmp(k, i) != 0:
        p3.coef.append(rational.RationalNumber(0,1))
        i.add_1()
    p3.coef.reverse()
    return p3


def LED_P_Q(p1):
    """
    Возвращает старший коэффициент в формате RationalNumber многочлена р1 типа Polynom

    Выполнил: Мельник Даниил
    """
    # вывод элемента массива коэффициентов многочлена
    return p1.coef[len(p1.coef)-1]


def DEG_P_N (p1):
    """
    Возвращает степень многочлена p1 типа Polynom

    Выполнил: Мельник Даниил
    """
    
    # вывод длины массива коэффициентов многочлена
    return len(p1.coef)-1


def FAC_P_Q(p1):
    """
    Принимает на вход многочлен р1 типа Polynom
    Выносит из многочлена НОК знаменателей и НОД числителей коэффициентов
    Возвращает многочлен типа Polynom

    Выполнил: Мельник Даниил
    """
    # создание переменных-копий
    p1=Polynom(p1.coef[::])
    p2=Polynom([])
    p3=Polynom([])
    p4=Polynom([])
    p3.coef=p1.coef
    p2.coef=p1.coef
    znam=[]
    chisl=[]
    # формирование массивов числителей и знаменателей коэффициентов
    for i in range(len(p3.coef)):
        if p3.coef[i].numer != 0:
            chisl.append(p3.coef[i].numer)
            znam.append(p3.coef[i].denom)

    # поиск массива НОК знаменателей (сравниваются соседние элементы)
    while (len(znam)!=1):
        k=natnum.nat_lcm(znam[0],znam[1])
        for i in range(2):
            znam.pop(0)
        znam.insert(0,k)
    
    # поиск массива НОД числителей (сравниваются соседние элементы)
    while (len(chisl)!=1):
        k=natnum.nat_gcd(chisl[0],chisl[1])
        for i in range(2):
            chisl.pop(0)
        chisl.insert(0,k)

    # нулевые элементы полученных массивов - НОК занменателей и НОД числителей
    nzn=znam[0]
    nch=chisl[0]
    
    # формирование дроби из НОК и НОД
    P=rational.RationalNumber(str(nch),str(nzn))
    # деление каждокго коэффициента на дробь из НОК и НОД
    for i in range (len(p1.coef)):
        d=rational.DIV_QQ_Q(p1.coef[i],P)
        p4.coef.append(d)
    return P, p4


def MUL_PP_P(pP,pA): 
    """
    Принимает на вход многочлены типа Polynom
    Умножает многочлены
    Возвращает многочлен типа Polynom

    Выполнил: Мельник Даниил
    """
    pP=Polynom(pP.coef[::])
    pA=Polynom(pA.coef[::])
    res=Polynom([])
    
    # дополнение меньшего по длине (в количестве коэффициентов) до длины большего
    if (len(pP.coef)<len(pA.coef)):
        for i in range(len(pA.coef)-len(pP.coef)):
            pP.coef.append(RationalNumber('0','1'))

    if (len(pA.coef)<len(pP.coef)):
        for i in range(len(pP.coef)-len(pA.coef)):
            pA.coef.append(RationalNumber('0','1'))


    # дополнение результирующего многочлена с учётом разности степеней умножаемых
    deg=2*(len(pP.coef)-1)
    for i in range (deg+1):
        res.coef.append(RationalNumber('0','1'))

    # умножение одного многочлена на коэффициент другого с учётом степени
    # полученный после умножения многочлен добавляется к результирующему.
    for i in range(0, len(pP.coef)):
        P1 = MUL_Pxk_P(pP, i)
        P2 = MUL_PQ_P(P1, pA.coef[i])
        
        res= ADD_PP_P(P2,res)
    res.normalise()
    return res


def divmod(p1, p2):
    """
    Принимает на вход два многочлена типа Polynom
    Находит остаток от деления двух многочленов p1 на p2
    Возвращает многочлен типа Polynom

    Выполнил: Мельник Даниил
    """
    p1 = Polynom(p1.coef[::])
    p2 = Polynom(p2.coef[::])
    
    #Если степень первого многочлена меньше степени второго -
    #целая часть равна нулю, а остаток - первому многочлену
    if DEG_P_N(p1) < DEG_P_N(p2):
        return Polynom([RationalNumber()]), p1

    
    ans = Polynom([])
    diff = DEG_P_N(p1) - DEG_P_N(p2)
    
    #Алгоритм аналогичен делению в столбик
    while (diff >= 0 and (DEG_P_N(p1) != 0 or LED_P_Q(p1).numer != 0)):
        #T = k*x^n, где n - разница между старшеми степенями p1 и p2,
        #k - частное между коэффициентами при старших коэффициентах
        T = MUL_Pxk_P(Polynom([rational.DIV_QQ_Q(LED_P_Q(p1),LED_P_Q(p2))]), diff)

        p1 = SUB_PP_P(p1, MUL_PP_P(T, p2))
        p1.normalise()
        
        ans = ADD_PP_P(ans, T)
        diff = DEG_P_N(p1) - DEG_P_N(p2)
        
    ans.normalise()
    p1.normalise()
    
    return ans, p1


def DIV_PP_P (p1,p2):
    """
    Принимает на вход два многочлена типа Polynom
    Возвращает целое от деления р1 и р2

    Выполнил: Мельник Даниил
    """
    return divmod(p1, p2)[0]


def MOD_PP_P (p1,p2):
    """
    Возвращает остаток от деления двух многочленов

    Выполнил: Мельник Даниил
    """
    return divmod(p1, p2)[1]


def GCF_PP_P(p1, p2):
    """
    Приниает два многочлена типа Polynom
    Находит НОД двух многочленов
    Возвращает многочлен типа Polynom

    Выполнил: Мельник Даниил
    """
    P1= Polynom(p1.coef[::])
    P2= Polynom(p2.coef[::])
    m=1
    #Для вычисления используется алгоритм Евклида
    while True:
        #Приводим коэффициенты многочленов к рациональным.
        P2 = FAC_P_Q(P2)[1]
        P1 = FAC_P_Q(P1)[1]
        
        if (DEG_P_N(P1)>DEG_P_N(P2)):
            P1=MOD_PP_P(P1, P2)
            if DEG_P_N(P1) == 0 and P1.coef[0].numer == 0:
                return P2
        else:
            P2=MOD_PP_P(P2, P1)
            if DEG_P_N(P2) == 0 and P2.coef[0].numer == 0:
                return P1


def DER_P_P (p1):
    """
    Принимает на вход многочлен типа Polynom
    Находит производную многочлена
    Возвращает многочлен типа Polynom

    Выполнил: Мельник Даниил
    """
    P1= Polynom(p1.coef[::])

    # производная константы равна нулю
    if DEG_P_N(p1) == 0:
        return Polynom([rational.RationalNumber(0)])

    for deg in range (DEG_P_N(p1), 0, -1): #домножаем a*x^deg на deg
        P1.coef[deg] = rational.MUL_QQ_Q(P1.coef[deg], rational.RationalNumber(str(deg),'1'))
    
    P1.coef.pop(0) #Делим многочлен на x и убираем свободный член.

    return P1


def NMR_P_P(p):
    """
    Возвращает многочлен с сокращенными кратными корнями

    Выполнил: Мельник Даниил
    """
    #q - производная многочлена p => в ней содержатся все
    #его корни, но их кратность уменьшена на 1
    q = DER_P_P(p)
    #Чтобы убрать появившиеся при дифференцировании p корни,
    #находим НОД между p и q
    d = GCF_PP_P(p, q   )
    #Сокращаем p, после чего степень всех корней понижается до 1.
    ans = DIV_PP_P(p, d)
    return ans


def main():
    p1 = Polynom([rational.RationalNumber(1, 1), rational.RationalNumber(0, 1), rational.RationalNumber(0, 1), rational.RationalNumber(0, 1), rational.RationalNumber(0, 1), rational.RationalNumber(0, 1), rational.RationalNumber(0, 1), rational.RationalNumber(0, 1), rational.RationalNumber(0, 1), rational.RationalNumber(0, 1), rational.RationalNumber(0, 1), rational.RationalNumber(1, 1),])
    p2= Polynom([rational.RationalNumber(10, 1), rational.RationalNumber(1, 1)])
    print(DIV_PP_P(p1, p2))
    
    
if __name__ == "__main__":
    main()