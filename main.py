# =============================================================================================================
#		 Программный модуль для построения графического пользовательского интерфейса
# =============================================================================================================
#		 @version   1.0
#		 @author    Лепов Алексей, гр. 1308
# =============================================================================================================


import sys
import tkinter
import tkinter.messagebox
import customtkinter
from natnum import *
from integer import *
from rational import *
from polynual import *


customtkinter.set_appearance_mode("system")
customtkinter.set_default_color_theme("blue")


class App(customtkinter.CTk):
    # Задание размеров окна приложения
    WIDTH = 1200
    HEIGHT = 667


    def __init__(self):
        super().__init__()  # Определение родительского класса

        self.title("Система компьютерной алгебры")
        self.geometry(f"{App.WIDTH}x{App.HEIGHT}")
        # self.minsize(App.WIDTH, App.HEIGHT)

        self.protocol("WM_DELETE_WINDOW", self.on_closing)
        if sys.platform == "darwin":
            self.bind("<Command-q>", self.on_closing)
            self.bind("<Command-w>", self.on_closing)
            self.createcommand('tk::mac::Quit', self.on_closing)


        # =============================================================================================================
        # =============================================== Создание окон ===============================================
        # =============================================================================================================


        # Настройка макета сетки (1x2)
        self.grid_columnconfigure(1, weight=1)
        self.rowconfigure(0, weight=1)

        # Создание окон (1x2)
        self.frame_left_menu = customtkinter.CTkFrame(master=self, width=180, corner_radius=0)
        self.frame_left_menu.grid(row=0, column=0, sticky="nswe")
        self.frame_right_info = customtkinter.CTkFrame(master=self)
        self.frame_right_info.grid(row=0, column=1, sticky="nswe", padx=20, pady=20)
        self.frame_right_natnum = customtkinter.CTkFrame(master=self)
        self.frame_right_natnum.grid(row=0, column=1, sticky="nswe", padx=20, pady=20)
        self.frame_right_integer = customtkinter.CTkFrame(master=self)
        self.frame_right_integer.grid(row=0, column=1, sticky="nswe", padx=20, pady=20)
        self.frame_right_rational = customtkinter.CTkFrame(master=self)
        self.frame_right_rational.grid(row=0, column=1, sticky="nswe", padx=20, pady=20)
        self.frame_right_polynual = customtkinter.CTkFrame(master=self)
        self.frame_right_polynual.grid(row=0, column=1, sticky="nswe", padx=20, pady=20)


        # =============================================================================================================
        # ============================================= Левое окно - МЕНЮ =============================================
        # =============================================================================================================


        # Настройка макета сетки
        self.frame_left_menu.grid_rowconfigure(6, weight=1)
        self.frame_left_menu.grid_rowconfigure(11, minsize=10)

        self.label_menu = customtkinter.CTkLabel(master=self.frame_left_menu, text="МЕНЮ",
                                                 text_font=("Roboto Medium", -16))
        self.label_menu.grid(row=0, column=0, pady=10, padx=10)

        # Кнопки выбора алгебраических структур
        self.button_info = customtkinter.CTkButton(master=self.frame_left_menu, text="О программе",
                                                   fg_color=("gray75", "#64897e"), width=180, height=40,
                                                   command=self.button_info_event)
        self.button_info.grid(row=1, column=0, pady=10, padx=20)

        self.button_natnum = customtkinter.CTkButton(master=self.frame_left_menu, text="Натуральные числа",
                                                     fg_color=("gray75", "#64897e"), width=180, height=40,
                                                     command=self.button_natnum_event)
        self.button_natnum.grid(row=2, column=0, pady=10, padx=20)

        self.button_integer = customtkinter.CTkButton(master=self.frame_left_menu, text="Целые числа",
                                                      fg_color=("gray75", "gray30"), width=180, height=40,
                                                      command=self.button_integer_event)
        self.button_integer.grid(row=3, column=0, pady=10, padx=20)

        self.button_rational = customtkinter.CTkButton(master=self.frame_left_menu, text="Рациональные числа",
                                                       fg_color=("gray75", "gray30"), width=180, height=40,
                                                       command=self.button_rational_event)
        self.button_rational.grid(row=4, column=0, pady=10, padx=20)

        self.button_polynual = customtkinter.CTkButton(master=self.frame_left_menu, text="Многочлены",
                                                       fg_color=("gray75", "gray30"), width=180, height=40,
                                                       command=self.button_polynual_event)
        self.button_polynual.grid(row=5, column=0, pady=10, padx=20)

        # Переключатель темной темы
        self.switch_dark_theme = customtkinter.CTkSwitch(master=self.frame_left_menu, text="Темная тема",
                                                         command=self.change_mode)
        self.switch_dark_theme.grid(row=10, column=0, pady=10, padx=20, sticky="w")


        # =============================================================================================================
        # =================================== Правое окно - информация о программе ====================================
        # =============================================================================================================


        # Настройка макета сетки
        self.frame_right_info.rowconfigure(14, weight=10)
        self.frame_right_info.columnconfigure(0, weight=1)

        self.label_info = customtkinter.CTkLabel(master=self.frame_right_info, text="Информация о программе",
                                                 text_font=("Roboto Medium", -16))
        self.label_info.grid(row=0, column=0, pady=10, padx=10)

        self.label_info_info = customtkinter.CTkLabel(master=self.frame_right_info, height=100,
                                                      text_font=("Roboto Medium", -16), fg_color=("white", "gray38"),
                                                      justify=tkinter.LEFT,
                                                      text=" \nДанная программа представляет собой систему компьютерной алгебры \n" +
                                                           "для выполнения различных вычислений над натуральными, целыми, \n" +
                                                           "рациональными числами и многочленами. \n")
        self.label_info_info.grid(row=1, column=0, sticky="we", padx=15, pady=15)

        self.label_info_authors = customtkinter.CTkLabel(master=self.frame_right_info, height=200,
                                                         text_font=("Roboto Medium", -16), fg_color=("white", "gray38"),
                                                         justify=tkinter.LEFT,
                                                         text="\nРазработкой занимались:\n\n" +
                                                              "Томилов Даниил (архитектор) \n" + " - разработка программного модуля <natnum.py> выполнения вычислений над натуральными числами; \n\n" +
                                                              "Мальцев Артём \n" + " - разработка программного модуля <integer.py> выполнения вычислений над целыми числами; \n\n" +
                                                              "Пакулов Илья \n" + " - разработка программного модуля <rational.py> выполнения вычислений над рациональными числами; \n\n" +
                                                              "Мельник Даниил (ответственный за управление качеством) \n" + " - разработка программного модуля <polynual.py> для выполнения вычислений над многочленами; \n\n" +
                                                              "Лепов Алексей \n" + " - разработка программного модуля <main.py> построения графического интерфейса и связка всех модулей.\n")
        self.label_info_authors.grid(row=2, column=0, sticky="we", padx=15, pady=15)


        # =============================================================================================================
        # ================================ Правое окно - функции для натуральных числе ================================
        # =============================================================================================================


        # Настройка макета сетки
        self.frame_right_natnum.rowconfigure(14, weight=10)
        self.frame_right_natnum.columnconfigure(0, weight=1)
        self.frame_right_natnum.columnconfigure(1, weight=1)
        self.frame_right_natnum.columnconfigure(2, weight=0)

        self.frame_body_natnum = customtkinter.CTkFrame(master=self.frame_right_natnum)
        self.frame_body_natnum.grid(row=0, column=0, columnspan=2, rowspan=1, pady=20, padx=20, sticky="new")
        self.frame_body_natnum.rowconfigure(0, weight=1)
        self.frame_body_natnum.columnconfigure(0, weight=1)

        self.frame_radio_natnum = customtkinter.CTkFrame(master=self.frame_right_natnum)
        self.frame_radio_natnum.grid(row=0, column=2, columnspan=2, rowspan=1, pady=20, padx=20, sticky="new")
        self.frame_radio_natnum.rowconfigure(0, weight=1)
        self.frame_radio_natnum.columnconfigure(0, weight=1)

        # =============================================================================================================

        self.label_info_natnum = customtkinter.CTkLabel(master=self.frame_body_natnum,
                                                        text="Натуральные числа с нулем (n; A[..])",
                                                        text_font=("Roboto Medium", -16))
        self.label_info_natnum.grid(row=0, column=0, pady=10, padx=10)

        self.label_info_natnum1 = customtkinter.CTkLabel(master=self.frame_body_natnum, height=100,
                                                         text_font=("Roboto Medium", -16), fg_color=("white", "gray38"),
                                                         justify=tkinter.LEFT,
                                                         text="Сравнение натуральных чисел: \n2 - если первое больше второго,\n 0, если равно, 1 иначе.")
        self.label_info_natnum1.grid(row=1, column=0, sticky="we", padx=15, pady=15)

        self.entry_natnum1 = customtkinter.CTkEntry(master=self.frame_body_natnum, width=120,
                                                    placeholder_text="Введите число", text="")
        self.entry_natnum1.grid(row=2, column=0, columnspan=2, pady=20, padx=20, sticky="we")
        self.entry_natnum2 = customtkinter.CTkEntry(master=self.frame_body_natnum, width=120,
                                                    placeholder_text="Введите второе число", text="")
        self.entry_natnum2.grid(row=3, column=0, columnspan=2, pady=20, padx=20, sticky="we")
        self.entry_natnum3 = customtkinter.CTkEntry(master=self.frame_body_natnum, width=120,
                                                    placeholder_text="Введите третье число", text="")
        self.entry_natnum3.grid(row=4, column=0, columnspan=2, pady=20, padx=20, sticky="we")

        self.button_calculate_natnums = customtkinter.CTkButton(master=self.frame_body_natnum, text="Вычислить",
                                                                fg_color=("gray75", "gray30"), width=180, height=40,
                                                                command=self.button_calculate_natnums_event)
        self.button_calculate_natnums.grid(row=5, column=0, pady=10, padx=20)

        self.label_res_natnum = customtkinter.CTkLabel(master=self.frame_body_natnum, height=80,
                                                       text_font=("Roboto Medium", -16), fg_color=("white", "gray38"),
                                                       justify=tkinter.LEFT, text="")
        self.label_res_natnum.grid(row=6, column=0, sticky="nwe", padx=15, pady=15)

        # =============================================================================================================

        self.radio_var_natnum = tkinter.IntVar(value=0)

        self.radio_button_COM_NN_D = customtkinter.CTkRadioButton(master=self.frame_radio_natnum,
                                                                  variable=self.radio_var_natnum, value=0, text="",
                                                                  command=self.radio_natnums_event_0)
        self.radio_button_COM_NN_D.grid(row=1, column=2, pady=10, padx=20, sticky="n")
        self.label_rad_COM_NN_D = customtkinter.CTkLabel(master=self.frame_radio_natnum, height=20, text="Сравнение",
                                                         text_font=("Roboto Medium", -14))
        self.label_rad_COM_NN_D.grid(row=1, column=3, pady=10, padx=20, sticky="n")

        self.radio_button_NZER_N_B = customtkinter.CTkRadioButton(master=self.frame_radio_natnum,
                                                                  variable=self.radio_var_natnum, value=1, text="",
                                                                  command=self.radio_natnums_event_1)
        self.radio_button_NZER_N_B.grid(row=2, column=2, pady=10, padx=20, sticky="n")
        self.label_rad_NZER_N_B = customtkinter.CTkLabel(master=self.frame_radio_natnum, height=20,
                                                         text="Проверка на ноль", text_font=("Roboto Medium", -14))
        self.label_rad_NZER_N_B.grid(row=2, column=3, pady=10, padx=20, sticky="n")

        self.radio_button_ADD_1N_N = customtkinter.CTkRadioButton(master=self.frame_radio_natnum,
                                                                  variable=self.radio_var_natnum, value=2, text="",
                                                                  command=self.radio_natnums_event_2)
        self.radio_button_ADD_1N_N.grid(row=3, column=2, pady=10, padx=20, sticky="n")
        self.label_rad_ADD_1N_N = customtkinter.CTkLabel(master=self.frame_radio_natnum, height=20,
                                                         text="Добавление единицы", text_font=("Roboto Medium", -14))
        self.label_rad_ADD_1N_N.grid(row=3, column=3, pady=10, padx=20, sticky="n")

        self.radio_button_ADD_NN_N = customtkinter.CTkRadioButton(master=self.frame_radio_natnum,
                                                                  variable=self.radio_var_natnum, value=3, text="",
                                                                  command=self.radio_natnums_event_3)
        self.radio_button_ADD_NN_N.grid(row=4, column=2, pady=10, padx=20, sticky="n")
        self.label_rad_ADD_NN_N = customtkinter.CTkLabel(master=self.frame_radio_natnum, height=20, text="Сложение",
                                                         text_font=("Roboto Medium", -14))
        self.label_rad_ADD_NN_N.grid(row=4, column=3, pady=10, padx=20, sticky="n")

        self.radio_button_SUB_NN_N = customtkinter.CTkRadioButton(master=self.frame_radio_natnum,
                                                                  variable=self.radio_var_natnum, value=4, text="",
                                                                  command=self.radio_natnums_event_4)
        self.radio_button_SUB_NN_N.grid(row=5, column=2, pady=10, padx=20, sticky="n")
        self.label_rad_SUB_NN_N = customtkinter.CTkLabel(master=self.frame_radio_natnum, height=20, text="Вычитание",
                                                         text_font=("Roboto Medium", -14))
        self.label_rad_SUB_NN_N.grid(row=5, column=3, pady=10, padx=20, sticky="n")

        self.radio_button_MUL_ND_N = customtkinter.CTkRadioButton(master=self.frame_radio_natnum,
                                                                  variable=self.radio_var_natnum, value=5, text="",
                                                                  command=self.radio_natnums_event_5)
        self.radio_button_MUL_ND_N.grid(row=6, column=2, pady=10, padx=20, sticky="n")
        self.label_rad_MUL_ND_N = customtkinter.CTkLabel(master=self.frame_radio_natnum, height=20, text="Умножение на цифру",
                                                         text_font=("Roboto Medium", -14))
        self.label_rad_MUL_ND_N.grid(row=6, column=3, pady=10, padx=20, sticky="n")

        self.radio_button_MUL_Nk_N = customtkinter.CTkRadioButton(master=self.frame_radio_natnum,
                                                                  variable=self.radio_var_natnum, value=6, text="",
                                                                  command=self.radio_natnums_event_6)
        self.radio_button_MUL_Nk_N.grid(row=7, column=2, pady=10, padx=20, sticky="n")
        self.label_rad_MUL_Nk_N = customtkinter.CTkLabel(master=self.frame_radio_natnum, height=20,
                                                         text="Умножение на 10^k", text_font=("Roboto Medium", -14))
        self.label_rad_MUL_Nk_N.grid(row=7, column=3, pady=10, padx=20, sticky="n")

        self.radio_button_MUL_NN_N = customtkinter.CTkRadioButton(master=self.frame_radio_natnum,
                                                                  variable=self.radio_var_natnum, value=7, text="",
                                                                  command=self.radio_natnums_event_7)
        self.radio_button_MUL_NN_N.grid(row=8, column=2, pady=10, padx=20, sticky="n")
        self.label_rad_MUL_NN_N = customtkinter.CTkLabel(master=self.frame_radio_natnum, height=20,
                                                         text="Умножение натуральных чисел",
                                                         text_font=("Roboto Medium", -14))
        self.label_rad_MUL_NN_N.grid(row=8, column=3, pady=10, padx=20, sticky="n")

        self.radio_button_SUB_NDN_N = customtkinter.CTkRadioButton(master=self.frame_radio_natnum,
                                                                   variable=self.radio_var_natnum, value=8, text="",
                                                                   command=self.radio_natnums_event_8)
        self.radio_button_SUB_NDN_N.grid(row=9, column=2, pady=10, padx=20, sticky="n")
        self.label_rad_SUB_NDN_N = customtkinter.CTkLabel(master=self.frame_radio_natnum, height=20,
                                                          text="Вычитание умноженного на цифру",
                                                          text_font=("Roboto Medium", -14))
        self.label_rad_SUB_NDN_N.grid(row=9, column=3, pady=10, padx=20, sticky="n")

        self.radio_button_DIV_NN_Dk = customtkinter.CTkRadioButton(master=self.frame_radio_natnum,
                                                                   variable=self.radio_var_natnum, value=9, text="",
                                                                   command=self.radio_natnums_event_9)
        self.radio_button_DIV_NN_Dk.grid(row=10, column=2, pady=10, padx=20, sticky="n")
        self.label_rad_DIV_NN_Dk = customtkinter.CTkLabel(master=self.frame_radio_natnum, height=20,
                                                          text="Первая цифра от деления",
                                                          text_font=("Roboto Medium", -14))
        self.label_rad_DIV_NN_Dk.grid(row=10, column=3, pady=10, padx=20, sticky="n")

        self.radio_button_DIV_NN_N = customtkinter.CTkRadioButton(master=self.frame_radio_natnum,
                                                                  variable=self.radio_var_natnum, value=10, text="",
                                                                  command=self.radio_natnums_event_10)
        self.radio_button_DIV_NN_N.grid(row=11, column=2, pady=10, padx=20, sticky="n")
        self.label_rad_DIV_NN_N = customtkinter.CTkLabel(master=self.frame_radio_natnum, height=20,
                                                         text="Частное от деление", text_font=("Roboto Medium", -14))
        self.label_rad_DIV_NN_N.grid(row=11, column=3, pady=10, padx=20, sticky="n")

        self.radio_button_MOD_NN_N = customtkinter.CTkRadioButton(master=self.frame_radio_natnum,
                                                                  variable=self.radio_var_natnum, value=11, text="",
                                                                  command=self.radio_natnums_event_11)
        self.radio_button_MOD_NN_N.grid(row=12, column=2, pady=10, padx=20, sticky="n")
        self.label_rad_MOD_NN_N = customtkinter.CTkLabel(master=self.frame_radio_natnum, height=20,
                                                         text="Остаток от деления", text_font=("Roboto Medium", -14))
        self.label_rad_MOD_NN_N.grid(row=12, column=3, pady=10, padx=20, sticky="n")

        self.radio_button_GCF_NN_N = customtkinter.CTkRadioButton(master=self.frame_radio_natnum,
                                                                  variable=self.radio_var_natnum, value=12, text="",
                                                                  command=self.radio_natnums_event_12)
        self.radio_button_GCF_NN_N.grid(row=13, column=2, pady=10, padx=20, sticky="n")
        self.label_rad_GCF_NN_N = customtkinter.CTkLabel(master=self.frame_radio_natnum, height=20, text="НОД",
                                                         text_font=("Roboto Medium", -14))
        self.label_rad_GCF_NN_N.grid(row=13, column=3, pady=10, padx=20, sticky="n")

        self.radio_button_LCM_NN_N = customtkinter.CTkRadioButton(master=self.frame_radio_natnum,
                                                                  variable=self.radio_var_natnum, value=13, text="",
                                                                  command=self.radio_natnums_event_13)
        self.radio_button_LCM_NN_N.grid(row=14, column=2, pady=10, padx=20, sticky="n")
        self.label_rad_LCM_NN_N = customtkinter.CTkLabel(master=self.frame_radio_natnum, height=20, text="НОК",
                                                         text_font=("Roboto Medium", -14))
        self.label_rad_LCM_NN_N.grid(row=14, column=3, pady=10, padx=20, sticky="n")

        self.hide_entry_natnum()
        self.radio_natnums_event2()


        # =============================================================================================================
        # =================================== Правое окно - функции для целых чисел ===================================
        # =============================================================================================================


        # Настройка макета сетки
        self.frame_right_integer.rowconfigure(14, weight=10)
        self.frame_right_integer.columnconfigure(0, weight=1)
        self.frame_right_integer.columnconfigure(1, weight=1)
        self.frame_right_integer.columnconfigure(2, weight=0)

        self.frame_body_integer = customtkinter.CTkFrame(master=self.frame_right_integer)
        self.frame_body_integer.grid(row=0, column=0, columnspan=2, rowspan=1, pady=20, padx=20, sticky="new")
        self.frame_body_integer.rowconfigure(0, weight=1)
        self.frame_body_integer.columnconfigure(0, weight=1)

        self.frame_radio_integer = customtkinter.CTkFrame(master=self.frame_right_integer)
        self.frame_radio_integer.grid(row=0, column=2, columnspan=2, rowspan=1, pady=20, padx=20, sticky="new")
        self.frame_radio_integer.rowconfigure(0, weight=1)
        self.frame_radio_integer.columnconfigure(0, weight=1)

        # =============================================================================================================

        self.label_info_integer = customtkinter.CTkLabel(master=self.frame_body_integer,
                                                         text="Целые числа (b, n; A[..])",
                                                         text_font=("Roboto Medium", -16))
        self.label_info_integer.grid(row=0, column=0, pady=10, padx=10)

        self.label_info_integer1 = customtkinter.CTkLabel(master=self.frame_body_integer, height=100,
                                                          text_font=("Roboto Medium", -16),
                                                          fg_color=("white", "gray38"),
                                                          justify=tkinter.LEFT,
                                                          text="Абсолютная величина числа, \nрезультат - натуральное")
        self.label_info_integer1.grid(row=1, column=0, sticky="we", padx=15, pady=15)

        self.entry_integer1 = customtkinter.CTkEntry(master=self.frame_body_integer, width=120,
                                                     placeholder_text="Введите число", text="")
        self.entry_integer1.grid(row=2, column=0, columnspan=2, pady=20, padx=20, sticky="we")
        self.entry_integer2 = customtkinter.CTkEntry(master=self.frame_body_integer, width=120,
                                                     placeholder_text="Введите второе число", text="")
        self.entry_integer2.grid(row=3, column=0, columnspan=2, pady=20, padx=20, sticky="we")

        self.button_calculate_integer = customtkinter.CTkButton(master=self.frame_body_integer, text="Вычислить",
                                                                fg_color=("gray75", "gray30"), width=180, height=40,
                                                                command=self.button_calculate_integer_event)
        self.button_calculate_integer.grid(row=4, column=0, pady=10, padx=20)

        self.label_res_integer = customtkinter.CTkLabel(master=self.frame_body_integer, height=80,
                                                        text_font=("Roboto Medium", -16), fg_color=("white", "gray38"),
                                                        justify=tkinter.LEFT, text="")
        self.label_res_integer.grid(row=5, column=0, sticky="nwe", padx=15, pady=15)

        # =============================================================================================================

        self.radio_var_integer = tkinter.IntVar(value=0)

        self.radio_button_ABS_Z_N = customtkinter.CTkRadioButton(master=self.frame_radio_integer,
                                                                 variable=self.radio_var_integer, value=0, text="",
                                                                 command=self.radio_integer_event_0)
        self.radio_button_ABS_Z_N.grid(row=1, column=2, pady=10, padx=20, sticky="n")
        self.label_rad_ABS_Z_N = customtkinter.CTkLabel(master=self.frame_radio_integer, height=20,
                                                        text="Абсолютная величина", text_font=("Roboto Medium", -14))
        self.label_rad_ABS_Z_N.grid(row=1, column=3, pady=10, padx=20, sticky="n")

        self.radio_button_POZ_Z_D = customtkinter.CTkRadioButton(master=self.frame_radio_integer,
                                                                 variable=self.radio_var_integer, value=1, text="",
                                                                 command=self.radio_integer_event_1)
        self.radio_button_POZ_Z_D.grid(row=2, column=2, pady=10, padx=20, sticky="n")
        self.label_rad_POZ_Z_D = customtkinter.CTkLabel(master=self.frame_radio_integer, height=20,
                                                        text="Определение положительности",
                                                        text_font=("Roboto Medium", -14))
        self.label_rad_POZ_Z_D.grid(row=2, column=3, pady=10, padx=20, sticky="n")

        self.radio_button_MUL_ZM_Z = customtkinter.CTkRadioButton(master=self.frame_radio_integer,
                                                                  variable=self.radio_var_integer, value=2, text="",
                                                                  command=self.radio_integer_event_2)
        self.radio_button_MUL_ZM_Z.grid(row=3, column=2, pady=10, padx=20, sticky="n")
        self.label_rad_MUL_ZM_Z = customtkinter.CTkLabel(master=self.frame_radio_integer, height=20,
                                                         text="Умножение на (-1)", text_font=("Roboto Medium", -14))
        self.label_rad_MUL_ZM_Z.grid(row=3, column=3, pady=10, padx=20, sticky="n")

        self.radio_button_TRANS_N_Z = customtkinter.CTkRadioButton(master=self.frame_radio_integer,
                                                                   variable=self.radio_var_integer, value=3, text="",
                                                                   command=self.radio_integer_event_3)
        self.radio_button_TRANS_N_Z.grid(row=4, column=2, pady=10, padx=20, sticky="n")
        self.label_rad_TRANS_N_Z = customtkinter.CTkLabel(master=self.frame_radio_integer, height=20,
                                                          text="Преобразование N в Z", text_font=("Roboto Medium", -14))
        self.label_rad_TRANS_N_Z.grid(row=4, column=3, pady=10, padx=20, sticky="n")

        self.radio_button_TRANS_Z_N = customtkinter.CTkRadioButton(master=self.frame_radio_integer,
                                                                   variable=self.radio_var_integer, value=4, text="",
                                                                   command=self.radio_integer_event_4)
        self.radio_button_TRANS_Z_N.grid(row=5, column=2, pady=10, padx=20, sticky="n")
        self.label_rad_TRANS_Z_N = customtkinter.CTkLabel(master=self.frame_radio_integer, height=20,
                                                          text="Преобразование Z⩾0 в N",
                                                          text_font=("Roboto Medium", -14))
        self.label_rad_TRANS_Z_N.grid(row=5, column=3, pady=10, padx=20, sticky="n")

        self.radio_button_ADD_ZZ_Z = customtkinter.CTkRadioButton(master=self.frame_radio_integer,
                                                                  variable=self.radio_var_integer, value=5, text="",
                                                                  command=self.radio_integer_event_5)
        self.radio_button_ADD_ZZ_Z.grid(row=6, column=2, pady=10, padx=20, sticky="n")
        self.label_rad_ADD_ZZ_Z = customtkinter.CTkLabel(master=self.frame_radio_integer, height=20,
                                                         text="Сложение целых чисел", text_font=("Roboto Medium", -14))
        self.label_rad_ADD_ZZ_Z.grid(row=6, column=3, pady=10, padx=20, sticky="n")

        self.radio_button_SUB_ZZ_Z = customtkinter.CTkRadioButton(master=self.frame_radio_integer,
                                                                  variable=self.radio_var_integer, value=6, text="",
                                                                  command=self.radio_integer_event_6)
        self.radio_button_SUB_ZZ_Z.grid(row=7, column=2, pady=10, padx=20, sticky="n")
        self.label_rad_SUB_ZZ_Z = customtkinter.CTkLabel(master=self.frame_radio_integer, height=20,
                                                         text="Вычитание целых чисел", text_font=("Roboto Medium", -14))
        self.label_rad_SUB_ZZ_Z.grid(row=7, column=3, pady=10, padx=20, sticky="n")

        self.radio_button_MUL_ZZ_Z = customtkinter.CTkRadioButton(master=self.frame_radio_integer,
                                                                  variable=self.radio_var_integer, value=7, text="",
                                                                  command=self.radio_integer_event_7)
        self.radio_button_MUL_ZZ_Z.grid(row=8, column=2, pady=10, padx=20, sticky="n")
        self.label_rad_MUL_ZZ_Z = customtkinter.CTkLabel(master=self.frame_radio_integer, height=20,
                                                         text="Умножение целых чисел", text_font=("Roboto Medium", -14))
        self.label_rad_MUL_ZZ_Z.grid(row=8, column=3, pady=10, padx=20, sticky="n")

        self.radio_button_DIV_ZZ_Z = customtkinter.CTkRadioButton(master=self.frame_radio_integer,
                                                                  variable=self.radio_var_integer, value=8, text="",
                                                                  command=self.radio_integer_event_8)
        self.radio_button_DIV_ZZ_Z.grid(row=9, column=2, pady=10, padx=20, sticky="n")
        self.label_rad_DIV_ZZ_Z = customtkinter.CTkLabel(master=self.frame_radio_integer, height=20,
                                                         text="Частное от деления", text_font=("Roboto Medium", -14))
        self.label_rad_DIV_ZZ_Z.grid(row=9, column=3, pady=10, padx=20, sticky="n")

        self.radio_button_MOD_ZZ_Z = customtkinter.CTkRadioButton(master=self.frame_radio_integer,
                                                                  variable=self.radio_var_integer, value=9, text="",
                                                                  command=self.radio_integer_event_9)
        self.radio_button_MOD_ZZ_Z.grid(row=10, column=2, pady=10, padx=20, sticky="n")
        self.label_rad_MOD_ZZ_Z = customtkinter.CTkLabel(master=self.frame_radio_integer, height=20,
                                                         text="Остаток от деления", text_font=("Roboto Medium", -14))
        self.label_rad_MOD_ZZ_Z.grid(row=10, column=3, pady=10, padx=20, sticky="n")

        self.hide_entry_integer()
        self.radio_integer_event1()


        # =============================================================================================================
        # =============================== Правое окно - функции для рациональных чисел ================================
        # =============================================================================================================


        # Настройка макета сетки
        self.frame_right_rational.rowconfigure(14, weight=10)
        self.frame_right_rational.columnconfigure(0, weight=1)
        self.frame_right_rational.columnconfigure(1, weight=1)
        self.frame_right_rational.columnconfigure(2, weight=0)

        self.frame_body_rational = customtkinter.CTkFrame(master=self.frame_right_rational)
        self.frame_body_rational.grid(row=0, column=0, columnspan=2, rowspan=1, pady=20, padx=20, sticky="new")
        self.frame_body_rational.rowconfigure(0, weight=1)
        self.frame_body_rational.columnconfigure(0, weight=1)

        self.frame_radio_rational = customtkinter.CTkFrame(master=self.frame_right_rational)
        self.frame_radio_rational.grid(row=0, column=2, columnspan=2, rowspan=1, pady=20, padx=20, sticky="new")
        self.frame_radio_rational.rowconfigure(0, weight=1)
        self.frame_radio_rational.columnconfigure(0, weight=1)

        # =============================================================================================================

        self.label_info_rational = customtkinter.CTkLabel(master=self.frame_body_rational,
                                                          text="Рациональные числа (дроби) — пара (целое/натуральное)",
                                                          text_font=("Roboto Medium", -16))
        self.label_info_rational.grid(row=0, column=0, pady=10, padx=10)

        self.label_info_rational1 = customtkinter.CTkLabel(master=self.frame_body_rational, height=100,
                                                           text_font=("Roboto Medium", -16),
                                                           fg_color=("white", "gray38"),
                                                           justify=tkinter.LEFT,
                                                           text="Сокращение дроби")
        self.label_info_rational1.grid(row=1, column=0, sticky="we", padx=15, pady=15)

        # Начало описания окна для записи рациональных чисел

        self.frame_entry_rational1 = customtkinter.CTkFrame(master=self.frame_body_rational)
        self.frame_entry_rational1.grid(row=2, column=2, columnspan=2, rowspan=1, pady=0, padx=0, sticky="new")
        self.frame_entry_rational1.rowconfigure(0, weight=1)
        self.frame_entry_rational1.columnconfigure(0, weight=1)

        self.entry_rational1_num = customtkinter.CTkEntry(master=self.frame_entry_rational1, width=120,
                                                          placeholder_text="Числитель первого числа", text="")
        self.entry_rational1_num.grid(row=0, column=0, columnspan=1, pady=20, padx=20, sticky="we")
        self.entry_rational1_den = customtkinter.CTkEntry(master=self.frame_entry_rational1, width=120,
                                                          placeholder_text="Знаменатель", text="")
        self.entry_rational1_den.grid(row=0, column=1, columnspan=1, pady=20, padx=20, sticky="we")

        self.frame_entry_rational2 = customtkinter.CTkFrame(master=self.frame_body_rational)
        self.frame_entry_rational2.grid(row=3, column=2, columnspan=2, rowspan=1, pady=0, padx=0, sticky="new")
        self.frame_entry_rational2.rowconfigure(0, weight=1)
        self.frame_entry_rational2.columnconfigure(0, weight=1)

        self.entry_rational2_num = customtkinter.CTkEntry(master=self.frame_entry_rational2, width=120,
                                                          placeholder_text="Числитель второго числа", text="")
        self.entry_rational2_num.grid(row=0, column=0, columnspan=1, pady=20, padx=20, sticky="we")
        self.entry_rational2_den = customtkinter.CTkEntry(master=self.frame_entry_rational2, width=120,
                                                          placeholder_text="Знаменатель", text="")
        self.entry_rational2_den.grid(row=0, column=1, columnspan=1, pady=20, padx=20, sticky="we")

        self.entry_rational1 = customtkinter.CTkEntry(master=self.frame_body_rational, width=120,
                                                      placeholder_text="Введите второе число", text="")
        self.entry_rational1.grid(row=2, column=0, columnspan=2, pady=20, padx=20, sticky="we")

        # Конец описания окна для записи рациональных чисел

        self.button_calculate_rational = customtkinter.CTkButton(master=self.frame_body_rational, text="Вычислить",
                                                                 fg_color=("gray75", "gray30"), width=180, height=40,
                                                                 command=self.button_calculate_rational_event)
        self.button_calculate_rational.grid(row=4, column=0, pady=10, padx=20)

        self.label_res_rational = customtkinter.CTkLabel(master=self.frame_body_rational, height=80,
                                                         text_font=("Roboto Medium", -16), fg_color=("white", "gray38"),
                                                         justify=tkinter.LEFT, text="")
        self.label_res_rational.grid(row=5, column=0, sticky="nwe", padx=15, pady=15)

        # =============================================================================================================

        self.radio_var_rational = tkinter.IntVar(value=0)

        self.radio_button_RED_Q_Q = customtkinter.CTkRadioButton(master=self.frame_radio_rational,
                                                                 variable=self.radio_var_rational, value=0, text="",
                                                                 command=self.radio_rational_event_0)
        self.radio_button_RED_Q_Q.grid(row=1, column=2, pady=10, padx=20, sticky="n")
        self.label_rad_RED_Q_Q = customtkinter.CTkLabel(master=self.frame_radio_rational, height=20,
                                                        text="Сокращение дроби", text_font=("Roboto Medium", -14))
        self.label_rad_RED_Q_Q.grid(row=1, column=3, pady=10, padx=20, sticky="n")

        self.radio_button_INT_Q_B = customtkinter.CTkRadioButton(master=self.frame_radio_rational,
                                                                 variable=self.radio_var_rational, value=1, text="",
                                                                 command=self.radio_rational_event_1)
        self.radio_button_INT_Q_B.grid(row=2, column=2, pady=10, padx=20, sticky="n")
        self.label_rad_INT_Q_B = customtkinter.CTkLabel(master=self.frame_radio_rational, height=20,
                                                        text="Проверка на целое", text_font=("Roboto Medium", -14))
        self.label_rad_INT_Q_B.grid(row=2, column=3, pady=10, padx=20, sticky="n")

        self.radio_button_TRANS_Z_Q = customtkinter.CTkRadioButton(master=self.frame_radio_rational,
                                                                   variable=self.radio_var_rational, value=2, text="",
                                                                   command=self.radio_rational_event_2)
        self.radio_button_TRANS_Z_Q.grid(row=3, column=2, pady=10, padx=20, sticky="n")
        self.label_rad_TRANS_Z_Q = customtkinter.CTkLabel(master=self.frame_radio_rational, height=20,
                                                          text="Преобразование Z в Q", text_font=("Roboto Medium", -14))
        self.label_rad_TRANS_Z_Q.grid(row=3, column=3, pady=10, padx=20, sticky="n")

        self.radio_button_TRANS_Q_Z = customtkinter.CTkRadioButton(master=self.frame_radio_rational,
                                                                   variable=self.radio_var_rational, value=3, text="",
                                                                   command=self.radio_rational_event_3)
        self.radio_button_TRANS_Q_Z.grid(row=4, column=2, pady=10, padx=20, sticky="n")
        self.label_rad_TRANS_Q_Z = customtkinter.CTkLabel(master=self.frame_radio_rational, height=20,
                                                          text="Преобразование Q в Z", text_font=("Roboto Medium", -14))
        self.label_rad_TRANS_Q_Z.grid(row=4, column=3, pady=10, padx=20, sticky="n")

        self.radio_button_ADD_QQ_Q = customtkinter.CTkRadioButton(master=self.frame_radio_rational,
                                                                  variable=self.radio_var_rational, value=4, text="",
                                                                  command=self.radio_rational_event_4)
        self.radio_button_ADD_QQ_Q.grid(row=5, column=2, pady=10, padx=20, sticky="n")
        self.label_rad_ADD_QQ_Q = customtkinter.CTkLabel(master=self.frame_radio_rational, height=20,
                                                         text="Сложение дробей", text_font=("Roboto Medium", -14))
        self.label_rad_ADD_QQ_Q.grid(row=5, column=3, pady=10, padx=20, sticky="n")

        self.radio_button_SUB_QQ_Q = customtkinter.CTkRadioButton(master=self.frame_radio_rational,
                                                                  variable=self.radio_var_rational, value=5, text="",
                                                                  command=self.radio_rational_event_5)
        self.radio_button_SUB_QQ_Q.grid(row=6, column=2, pady=10, padx=20, sticky="n")
        self.label_rad_SUB_QQ_Q = customtkinter.CTkLabel(master=self.frame_radio_rational, height=20,
                                                         text="Вычитание дробей", text_font=("Roboto Medium", -14))
        self.label_rad_SUB_QQ_Q.grid(row=6, column=3, pady=10, padx=20, sticky="n")

        self.radio_button_MUL_QQ_Q = customtkinter.CTkRadioButton(master=self.frame_radio_rational,
                                                                  variable=self.radio_var_rational, value=6, text="",
                                                                  command=self.radio_rational_event_6)
        self.radio_button_MUL_QQ_Q.grid(row=7, column=2, pady=10, padx=20, sticky="n")
        self.label_rad_MUL_QQ_Q = customtkinter.CTkLabel(master=self.frame_radio_rational, height=20,
                                                         text="Умножение дробей", text_font=("Roboto Medium", -14))
        self.label_rad_MUL_QQ_Q.grid(row=7, column=3, pady=10, padx=20, sticky="n")

        self.radio_button_DIV_QQ_Q = customtkinter.CTkRadioButton(master=self.frame_radio_rational,
                                                                  variable=self.radio_var_rational, value=7, text="",
                                                                  command=self.radio_rational_event_7)
        self.radio_button_DIV_QQ_Q.grid(row=8, column=2, pady=10, padx=20, sticky="n")
        self.label_rad_DIV_QQ_Q = customtkinter.CTkLabel(master=self.frame_radio_rational, height=20,
                                                         text="Деление дробей ", text_font=("Roboto Medium", -14))
        self.label_rad_DIV_QQ_Q.grid(row=8, column=3, pady=10, padx=20, sticky="n")

        self.hide_entry_rational()
        self.radio_rational_event1()


        # =============================================================================================================
        # =================================== Правое окно - функции для многочленов ===================================
        # =============================================================================================================


        # Настройка макета сетки
        self.frame_right_polynual.rowconfigure(14, weight=10)
        self.frame_right_polynual.columnconfigure(0, weight=1)
        self.frame_right_polynual.columnconfigure(1, weight=1)
        self.frame_right_polynual.columnconfigure(2, weight=0)

        self.frame_body_polynual = customtkinter.CTkFrame(master=self.frame_right_polynual)
        self.frame_body_polynual.grid(row=0, column=0, columnspan=2, rowspan=1, pady=20, padx=20, sticky="new")
        self.frame_body_polynual.rowconfigure(0, weight=1)
        self.frame_body_polynual.columnconfigure(0, weight=1)

        self.frame_radio_polynual = customtkinter.CTkFrame(master=self.frame_right_polynual)
        self.frame_radio_polynual.grid(row=0, column=2, columnspan=2, rowspan=1, pady=20, padx=20, sticky="new")
        self.frame_radio_polynual.rowconfigure(0, weight=1)
        self.frame_radio_polynual.columnconfigure(0, weight=1)

        # =============================================================================================================

        self.label_info_polynual = customtkinter.CTkLabel(master=self.frame_body_polynual,
                                                          text="Многочлен с рациональными коэффициентами",
                                                          text_font=("Roboto Medium", -16))
        self.label_info_polynual.grid(row=0, column=0, pady=10, padx=10)

        self.label_info_polynual1 = customtkinter.CTkLabel(master=self.frame_body_polynual, height=100,
                                                           text_font=("Roboto Medium", -16),
                                                           fg_color=("white", "gray38"),
                                                           justify=tkinter.LEFT,
                                                           text="Сложение многочленов")
        self.label_info_polynual1.grid(row=1, column=0, sticky="we", padx=15, pady=15)

        self.entry_polynual1 = customtkinter.CTkEntry(master=self.frame_body_polynual, width=120,
                                                      placeholder_text="Введите коэффициенты многочлена через < > (1/2 0 1 3/2)",
                                                      text="")
        self.entry_polynual1.grid(row=2, column=0, columnspan=2, pady=20, padx=20, sticky="we")
        self.entry_polynual2 = customtkinter.CTkEntry(master=self.frame_body_polynual, width=120,
                                                      placeholder_text="Введите коэффициенты второго многочлена через < > (1/2 0 1 3/2)",
                                                      text="")
        self.entry_polynual2.grid(row=3, column=0, columnspan=2, pady=20, padx=20, sticky="we")

        # Начало описания окна для записи рациональных чисел

        self.frame_entry_rational = customtkinter.CTkFrame(master=self.frame_body_polynual)
        self.frame_entry_rational.grid(row=3, column=2, columnspan=2, rowspan=1, pady=0, padx=0, sticky="new")
        self.frame_entry_rational.rowconfigure(0, weight=1)
        self.frame_entry_rational.columnconfigure(0, weight=1)

        self.entry_rational_num = customtkinter.CTkEntry(master=self.frame_entry_rational, width=120,
                                                         placeholder_text="Числитель дроби", text="")
        self.entry_rational_num.grid(row=0, column=0, columnspan=1, pady=20, padx=20, sticky="we")
        self.entry_rational_den = customtkinter.CTkEntry(master=self.frame_entry_rational, width=120,
                                                         placeholder_text="Знаменатель", text="")
        self.entry_rational_den.grid(row=0, column=1, columnspan=1, pady=20, padx=20, sticky="we")

        # Конец описания окна для записи рациональных чисел

        self.entry_polynual3 = customtkinter.CTkEntry(master=self.frame_body_polynual, width=120,
                                                      placeholder_text="Введите степень k числа X", text="")
        self.entry_polynual3.grid(row=4, column=0, columnspan=2, pady=20, padx=20, sticky="we")

        self.button_calculate_polynual = customtkinter.CTkButton(master=self.frame_body_polynual, text="Вычислить",
                                                                 fg_color=("gray75", "gray30"), width=180, height=40,
                                                                 command=self.button_calculate_polynual_event)
        self.button_calculate_polynual.grid(row=5, column=0, pady=10, padx=20)

        self.label_res_polynual = customtkinter.CTkLabel(master=self.frame_body_polynual, height=80,
                                                         text_font=("Roboto Medium", -16), fg_color=("white", "gray38"),
                                                         justify=tkinter.LEFT, text="")
        self.label_res_polynual.grid(row=6, column=0, sticky="nwe", padx=15, pady=15)

        # =============================================================================================================         

        self.radio_var_polynual = tkinter.IntVar(value=0)

        self.radio_button_ADD_PP_P = customtkinter.CTkRadioButton(master=self.frame_radio_polynual,
                                                                  variable=self.radio_var_polynual, value=0, text="",
                                                                  command=self.radio_polynual_event_0)
        self.radio_button_ADD_PP_P.grid(row=1, column=2, pady=10, padx=20, sticky="n")
        self.label_rad_ADD_PP_P = customtkinter.CTkLabel(master=self.frame_radio_polynual, height=20,
                                                         text="Сложение многочленов", text_font=("Roboto Medium", -14))
        self.label_rad_ADD_PP_P.grid(row=1, column=3, pady=10, padx=20, sticky="n")

        self.radio_button_SUB_PP_P = customtkinter.CTkRadioButton(master=self.frame_radio_polynual,
                                                                  variable=self.radio_var_polynual, value=1, text="",
                                                                  command=self.radio_polynual_event_1)
        self.radio_button_SUB_PP_P.grid(row=2, column=2, pady=10, padx=20, sticky="n")
        self.label_rad_SUB_PP_P = customtkinter.CTkLabel(master=self.frame_radio_polynual, height=20,
                                                         text="Вычитание многочленов", text_font=("Roboto Medium", -14))
        self.label_rad_SUB_PP_P.grid(row=2, column=3, pady=10, padx=20, sticky="n")

        self.radio_button_MUL_PQ_P = customtkinter.CTkRadioButton(master=self.frame_radio_polynual,
                                                                  variable=self.radio_var_polynual, value=2, text="",
                                                                  command=self.radio_polynual_event_2)
        self.radio_button_MUL_PQ_P.grid(row=3, column=2, pady=10, padx=20, sticky="n")
        self.label_rad_MUL_PQ_P = customtkinter.CTkLabel(master=self.frame_radio_polynual, height=20,
                                                         text="Умножение на Q", text_font=("Roboto Medium", -14))
        self.label_rad_MUL_PQ_P.grid(row=3, column=3, pady=10, padx=20, sticky="n")

        self.radio_button_MUL_Pxk_P = customtkinter.CTkRadioButton(master=self.frame_radio_polynual,
                                                                   variable=self.radio_var_polynual, value=3, text="",
                                                                   command=self.radio_polynual_event_3)
        self.radio_button_MUL_Pxk_P.grid(row=4, column=2, pady=10, padx=20, sticky="n")
        self.label_rad_MUL_Pxk_P = customtkinter.CTkLabel(master=self.frame_radio_polynual, height=20,
                                                          text="Умножение на степень числа X",
                                                          text_font=("Roboto Medium", -14))
        self.label_rad_MUL_Pxk_P.grid(row=4, column=3, pady=10, padx=20, sticky="n")

        self.radio_button_LED_P_Q = customtkinter.CTkRadioButton(master=self.frame_radio_polynual,
                                                                 variable=self.radio_var_polynual, value=4, text="",
                                                                 command=self.radio_polynual_event_4)
        self.radio_button_LED_P_Q.grid(row=5, column=2, pady=10, padx=20, sticky="n")
        self.label_rad_LED_P_Q = customtkinter.CTkLabel(master=self.frame_radio_polynual, height=20,
                                                        text="Старший коэффициент", text_font=("Roboto Medium", -14))
        self.label_rad_LED_P_Q.grid(row=5, column=3, pady=10, padx=20, sticky="n")

        self.radio_button_DEG_P_N = customtkinter.CTkRadioButton(master=self.frame_radio_polynual,
                                                                 variable=self.radio_var_polynual, value=5, text="",
                                                                 command=self.radio_polynual_event_5)
        self.radio_button_DEG_P_N.grid(row=6, column=2, pady=10, padx=20, sticky="n")
        self.label_rad_DEG_P_N = customtkinter.CTkLabel(master=self.frame_radio_polynual, height=20,
                                                        text="Степень многочлена", text_font=("Roboto Medium", -14))
        self.label_rad_DEG_P_N.grid(row=6, column=3, pady=10, padx=20, sticky="n")

        self.radio_button_FAC_P_Q = customtkinter.CTkRadioButton(master=self.frame_radio_polynual,
                                                                 variable=self.radio_var_polynual, value=6, text="",
                                                                 command=self.radio_polynual_event_6)
        self.radio_button_FAC_P_Q.grid(row=7, column=2, pady=10, padx=20, sticky="n")
        self.label_rad_FAC_P_Q = customtkinter.CTkLabel(master=self.frame_radio_polynual, height=20,
                                                        text="Вынесение НОК и НОД", text_font=("Roboto Medium", -14))
        self.label_rad_FAC_P_Q.grid(row=7, column=3, pady=10, padx=20, sticky="n")

        self.radio_button_MUL_PP_P = customtkinter.CTkRadioButton(master=self.frame_radio_polynual,
                                                                  variable=self.radio_var_polynual, value=7, text="",
                                                                  command=self.radio_polynual_event_7)
        self.radio_button_MUL_PP_P.grid(row=8, column=2, pady=10, padx=20, sticky="n")
        self.label_rad_MUL_PP_P = customtkinter.CTkLabel(master=self.frame_radio_polynual, height=20,
                                                         text="Умножение многочленов", text_font=("Roboto Medium", -14))
        self.label_rad_MUL_PP_P.grid(row=8, column=3, pady=10, padx=20, sticky="n")

        self.radio_button_DIV_PP_P = customtkinter.CTkRadioButton(master=self.frame_radio_polynual,
                                                                  variable=self.radio_var_polynual, value=8, text="",
                                                                  command=self.radio_polynual_event_8)
        self.radio_button_DIV_PP_P.grid(row=9, column=2, pady=10, padx=20, sticky="n")
        self.label_rad_DIV_PP_P = customtkinter.CTkLabel(master=self.frame_radio_polynual, height=20,
                                                         text="Частное от дления P на P",
                                                         text_font=("Roboto Medium", -14))
        self.label_rad_DIV_PP_P.grid(row=9, column=3, pady=10, padx=20, sticky="n")

        self.radio_button_MOD_PP_P = customtkinter.CTkRadioButton(master=self.frame_radio_polynual,
                                                                  variable=self.radio_var_polynual, value=9, text="",
                                                                  command=self.radio_polynual_event_9)
        self.radio_button_MOD_PP_P.grid(row=10, column=2, pady=10, padx=20, sticky="n")
        self.label_rad_MOD_PP_P = customtkinter.CTkLabel(master=self.frame_radio_polynual, height=20,
                                                         text="Остаток от деления P на P",
                                                         text_font=("Roboto Medium", -14))
        self.label_rad_MOD_PP_P.grid(row=10, column=3, pady=10, padx=20, sticky="n")

        self.radio_button_GCF_PP_P = customtkinter.CTkRadioButton(master=self.frame_radio_polynual,
                                                                  variable=self.radio_var_polynual, value=10, text="",
                                                                  command=self.radio_polynual_event_10)
        self.radio_button_GCF_PP_P.grid(row=11, column=2, pady=10, padx=20, sticky="n")
        self.label_rad_GCF_PP_P = customtkinter.CTkLabel(master=self.frame_radio_polynual, height=20,
                                                         text="НОД многочленов", text_font=("Roboto Medium", -14))
        self.label_rad_GCF_PP_P.grid(row=11, column=3, pady=10, padx=20, sticky="n")

        self.radio_button_DER_P_P = customtkinter.CTkRadioButton(master=self.frame_radio_polynual,
                                                                 variable=self.radio_var_polynual, value=11, text="",
                                                                 command=self.radio_polynual_event_11)
        self.radio_button_DER_P_P.grid(row=12, column=2, pady=10, padx=20, sticky="n")
        self.label_rad_DER_P_P = customtkinter.CTkLabel(master=self.frame_radio_polynual, height=20,
                                                        text="Производная многочлена", text_font=("Roboto Medium", -14))
        self.label_rad_DER_P_P.grid(row=12, column=3, pady=10, padx=20, sticky="n")

        self.radio_button_NMR_P_P = customtkinter.CTkRadioButton(master=self.frame_radio_polynual,
                                                                 variable=self.radio_var_polynual, value=12, text="",
                                                                 command=self.radio_polynual_event_12)
        self.radio_button_NMR_P_P.grid(row=13, column=2, pady=10, padx=20, sticky="n")
        self.label_rad_NMR_P_P = customtkinter.CTkLabel(master=self.frame_radio_polynual, height=20,
                                                        text="Преобразование многочлена",
                                                        text_font=("Roboto Medium", -14))
        self.label_rad_NMR_P_P.grid(row=13, column=3, pady=10, padx=20, sticky="n")

        self.hide_entry_polynual()
        self.radio_polynual_event2()


        # =============================================================================================================
        # ====================================== Присвение значений по умолчанию ======================================
        # =============================================================================================================
        
        
        self.hide_menu_frames()
        self.frame_right_info.grid(row=0, column=1, sticky="nswe", padx=20, pady=20)

        self.switch_dark_theme.select()
        if self.switch_dark_theme.get() == 1:
            self.button_info.configure(fg_color=("gray75", "#5c8da4"))
        else:
            self.button_info.configure(fg_color=("#7db8d4"))

        self.radio_button_COM_NN_D.select()
        self.radio_button_ABS_Z_N.select()
        self.radio_button_RED_Q_Q.select()
        self.radio_button_ADD_PP_P.select()


    # =============================================================================================================
    # ============================== Функции для выполнения арифметических действий ===============================
    # =============================================================================================================


    def button_calculate_natnums_event(self):
        try:
            if (self.radio_var_natnum.get() == 0):
                self.label_res_natnum.configure(
                    text=str(nat_cmp(NaturalNumber(self.entry_natnum1.get()), NaturalNumber(self.entry_natnum2.get()))))
            elif (self.radio_var_natnum.get() == 1):
                self.label_res_natnum.configure(text=str(NaturalNumber(self.entry_natnum1.get()).is_zero()))
            elif (self.radio_var_natnum.get() == 2):
                n = NaturalNumber(self.entry_natnum1.get())
                n.add_1()
                self.label_res_natnum.configure(text=str(n))
            elif (self.radio_var_natnum.get() == 3):
                self.label_res_natnum.configure(text=str(nat_sum(NaturalNumber(self.entry_natnum1.get()), NaturalNumber(self.entry_natnum2.get()))))
            elif (self.radio_var_natnum.get() == 4):
                self.label_res_natnum.configure(text=str(nat_sub(NaturalNumber(self.entry_natnum1.get()), NaturalNumber(self.entry_natnum2.get()))))
            elif (self.radio_var_natnum.get() == 5):
                self.label_res_natnum.configure(text=str(
                    nat_mul_by_digit(NaturalNumber(str(self.entry_natnum1.get())), int(self.entry_natnum2.get()))))
            elif (self.radio_var_natnum.get() == 6):
                self.label_res_natnum.configure(text=str(nat_mul_by_10_pow(NaturalNumber(str(self.entry_natnum1.get())),
                                                                           NaturalNumber(
                                                                               str(self.entry_natnum2.get())))))
            elif (self.radio_var_natnum.get() == 7):
                self.label_res_natnum.configure(text=str(nat_mul(NaturalNumber(str(self.entry_natnum1.get())),
                                                                 NaturalNumber(str(self.entry_natnum2.get())))))
            elif (self.radio_var_natnum.get() == 8):
                self.label_res_natnum.configure(text=str(SUB_NDN_N(NaturalNumber(str(self.entry_natnum1.get())),
                                                                   NaturalNumber(str(self.entry_natnum2.get())),
                                                                   int(self.entry_natnum3.get()))))
            elif (self.radio_var_natnum.get() == 9):
                self.label_res_natnum.configure(text=str(DIV_NN_Dk(NaturalNumber(str(self.entry_natnum1.get())),
                                                                   NaturalNumber(str(self.entry_natnum2.get())))))
            elif (self.radio_var_natnum.get() == 10):
                self.label_res_natnum.configure(text=str(nat_div(NaturalNumber(str(self.entry_natnum1.get())),
                                                                 NaturalNumber(str(self.entry_natnum2.get())))))
            elif (self.radio_var_natnum.get() == 11):
                self.label_res_natnum.configure(text=str(nat_mod(NaturalNumber(str(self.entry_natnum1.get())),
                                                                 NaturalNumber(str(self.entry_natnum2.get())))))
            elif (self.radio_var_natnum.get() == 12):
                self.label_res_natnum.configure(text=str(nat_gcd(NaturalNumber(str(self.entry_natnum1.get())),
                                                                 NaturalNumber(str(self.entry_natnum2.get())))))
            elif (self.radio_var_natnum.get() == 13):
                self.label_res_natnum.configure(text=str(nat_lcm(NaturalNumber(str(self.entry_natnum1.get())),
                                                                 NaturalNumber(str(self.entry_natnum2.get())))))
        except ValueError:
            self.label_res_natnum.configure(text="Неверное значение переменной!")
        except TypeError:
            self.label_res_natnum.configure(text="Неверный тип данных!")
        except ZeroDivisionError:
            self.label_res_natnum.configure(text="Деление на ноль!")
        print("Нажата кнопка для вычисления натуральных чисел")

    def button_calculate_integer_event(self):
        try:
            if (self.radio_var_integer.get() == 0):
                self.label_res_integer.configure(text=str(ABS_Z_N(Integer(self.entry_integer1.get()))))
            elif (self.radio_var_integer.get() == 1):
                self.label_res_integer.configure(text=str(POZ_Z_D(Integer(self.entry_integer1.get()))))
            elif (self.radio_var_integer.get() == 2):
                self.label_res_integer.configure(text=str(MUL_ZM_Z(Integer(self.entry_integer1.get()))))
            elif (self.radio_var_integer.get() == 3):
                self.label_res_integer.configure(text=str(TRANS_N_Z(NaturalNumber(self.entry_integer1.get()))))
            elif (self.radio_var_integer.get() == 4):
                self.label_res_integer.configure(text=str(TRANS_Z_N(Integer(self.entry_integer1.get()))))
            elif (self.radio_var_integer.get() == 5):
                self.label_res_integer.configure(
                    text=str(ADD_ZZ_Z(Integer(self.entry_integer1.get()), Integer(self.entry_integer2.get()))))
            elif (self.radio_var_integer.get() == 6):
                self.label_res_integer.configure(
                    text=str(SUB_ZZ_Z(Integer(self.entry_integer1.get()), Integer(self.entry_integer2.get()))))
            elif (self.radio_var_integer.get() == 7):
                self.label_res_integer.configure(
                    text=str(MUL_ZZ_Z(Integer(self.entry_integer1.get()), Integer(self.entry_integer2.get()))))
            elif (self.radio_var_integer.get() == 8):
                self.label_res_integer.configure(
                    text=str(DIV_ZZ_Z(Integer(self.entry_integer1.get()), Integer(self.entry_integer2.get()))))
            elif (self.radio_var_integer.get() == 9):
                self.label_res_integer.configure(
                    text=str(MOD_ZZ_Z(Integer(self.entry_integer1.get()), Integer(self.entry_integer2.get()))))
        except ValueError:
            self.label_res_integer.configure(text="Неверное значение переменной!")
        except TypeError:
            self.label_res_integer.configure(text="Неверный тип данных!")
        except ZeroDivisionError:
            self.label_res_integer.configure(text="Деление на ноль!")
        print("Нажата кнопка для вычисления целых чисел")

    def button_calculate_rational_event(self):
        try:
            if (self.radio_var_rational.get() == 0):
                self.label_res_rational.configure(
                    text=str(RED_Q_Q(RationalNumber(self.entry_rational1_num.get(), self.entry_rational1_den.get()))))
            elif (self.radio_var_rational.get() == 1):
                self.label_res_rational.configure(
                    text=str(INT_Q_B(RationalNumber(self.entry_rational1_num.get(), self.entry_rational1_den.get()))))
            elif (self.radio_var_rational.get() == 2):
                self.label_res_rational.configure(text=str(TRANS_Z_Q(Integer(self.entry_rational1.get()))))
            elif (self.radio_var_rational.get() == 3):
                self.label_res_rational.configure(
                    text=str(TRANS_Q_Z(RationalNumber(self.entry_rational1_num.get(), self.entry_rational1_den.get()))))
            elif (self.radio_var_rational.get() == 4):
                self.label_res_rational.configure(text=str(
                    ADD_QQ_Q(RationalNumber(self.entry_rational1_num.get(), self.entry_rational1_den.get()),
                             RationalNumber(self.entry_rational2_num.get(), self.entry_rational2_den.get()))))
            elif (self.radio_var_rational.get() == 5):
                self.label_res_rational.configure(text=str(
                    SUB_QQ_Q(RationalNumber(self.entry_rational1_num.get(), self.entry_rational1_den.get()),
                             RationalNumber(self.entry_rational2_num.get(), self.entry_rational2_den.get()))))
            elif (self.radio_var_rational.get() == 6):
                self.label_res_rational.configure(text=str(
                    MUL_QQ_Q(RationalNumber(self.entry_rational1_num.get(), self.entry_rational1_den.get()),
                             RationalNumber(self.entry_rational2_num.get(), self.entry_rational2_den.get()))))
            elif (self.radio_var_rational.get() == 7):
                self.label_res_rational.configure(text=str(
                    DIV_QQ_Q(RationalNumber(self.entry_rational1_num.get(), self.entry_rational1_den.get()),
                             RationalNumber(self.entry_rational2_num.get(), self.entry_rational2_den.get()))))
        except ValueError:
            self.label_res_rational.configure(text="Неверное значение переменной!")
        except TypeError:
            self.label_res_rational.configure(text="Неверный тип данных!")
        except ZeroDivisionError:
            self.label_res_rational.configure(text="Деление на ноль!")
        print("Нажата кнопка для вычисления рациональных чисел")

    def button_calculate_polynual_event(self):

        arr1 = self.entry_polynual1.get().replace(",", " ").split()
        arr1 = list(map(lambda x: (x.split("/") if "/" in x else [x, '1']), arr1))
        print(arr1)
        ratio_arr1 = [RationalNumber(x[0], x[1]) for x in arr1[::-1]]

        arr2 = self.entry_polynual2.get().replace(",", " ").split()
        arr2 = list(map(lambda x: (x.split("/") if "/" in x else [x, '1']), arr2))
        ratio_arr2 = [RationalNumber(x[0],x[1]) for x in arr2[::-1]]
        print(ratio_arr1, ratio_arr2)
        try:
            if (self.radio_var_polynual.get() == 0):
                self.label_res_polynual.configure(
                    text=str(ADD_PP_P(Polynom(ratio_arr1), Polynom(ratio_arr2))))
            elif (self.radio_var_polynual.get() == 1):
                self.label_res_polynual.configure(
                    text=str(SUB_PP_P(Polynom(ratio_arr1), Polynom(ratio_arr2))))
            elif (self.radio_var_polynual.get() == 2):
                self.label_res_polynual.configure(
                    text=str(MUL_PQ_P(Polynom(ratio_arr1),
                                      RationalNumber(self.entry_rational_num.get(), self.entry_rational_den.get()))))
            elif (self.radio_var_polynual.get() == 3):
                print(self.entry_polynual2.get())
                self.label_res_polynual.configure(
                    text=str(MUL_Pxk_P(Polynom(ratio_arr1), NaturalNumber(self.entry_polynual3.get()))))
            elif (self.radio_var_polynual.get() == 4):
                self.label_res_polynual.configure(text=str(LED_P_Q(Polynom(ratio_arr1))))
            elif (self.radio_var_polynual.get() == 5):
                self.label_res_polynual.configure(text=str(DEG_P_N(Polynom(ratio_arr1))))
            elif (self.radio_var_polynual.get() == 6):
                self.label_res_polynual.configure(text=str(FAC_P_Q(Polynom(ratio_arr1))[1]))
            elif (self.radio_var_polynual.get() == 7):
                self.label_res_polynual.configure(
                    text=str(MUL_PP_P(Polynom(ratio_arr1), Polynom(ratio_arr2))))
            elif (self.radio_var_polynual.get() == 8):
                self.label_res_polynual.configure(
                    text=str(DIV_PP_P(Polynom(ratio_arr1), Polynom(ratio_arr2))))
            elif (self.radio_var_polynual.get() == 9):
                self.label_res_polynual.configure(
                    text=str(MOD_PP_P(Polynom(ratio_arr1), Polynom(ratio_arr2))))
            elif (self.radio_var_polynual.get() == 10):
                self.label_res_polynual.configure(
                    text=str(GCF_PP_P(Polynom(ratio_arr1), Polynom(ratio_arr2))))
            elif (self.radio_var_polynual.get() == 11):
                self.label_res_polynual.configure(text=str(DER_P_P(Polynom(ratio_arr1))))
            elif (self.radio_var_polynual.get() == 12):
                self.label_res_polynual.configure(text=str(NMR_P_P(Polynom(ratio_arr1))))
        except ValueError:
            self.label_res_polynual.configure(text="Неверное значение переменной!")
        except TypeError:
            self.label_res_polynual.configure(text="Неверный тип данных!")
        except ZeroDivisionError:
            self.label_res_polynual.configure(text="Деление на ноль!")
        print("Нажата кнопка для вычисления многочленов")


    # =============================================================================================================
    # ======================================== Функции выбора радио-кнопки ========================================
    # =============================================================================================================


    def radio_natnums_event_0(self):
        self.radio_natnums_event2()
        self.label_info_natnum1.configure(
            text="Сравнение натуральных чисел: \n2 - если первое больше второго,\n0, если равно, 1 иначе.")

    def radio_natnums_event_1(self):
        self.radio_natnums_event1()
        self.label_info_natnum1.configure(
            text="Проверка на ноль: если число \nне равно нулю, то «true» иначе \n«false»")

    def radio_natnums_event_2(self):
        self.radio_natnums_event1()
        self.label_info_natnum1.configure(text="Добавление единицы к натуральному\n числу")

    def radio_natnums_event_3(self):
        self.radio_natnums_event2()
        self.label_info_natnum1.configure(text="Сложение натуральных чисел")

    def radio_natnums_event_4(self):
        self.radio_natnums_event2()
        self.label_info_natnum1.configure(
            text="Вычитание из первого большего \nнатурального числа второго \nменьшего или равного")

    def radio_natnums_event_5(self):
        self.radio_natnums_event2()
        self.label_info_natnum1.configure(text="Умножение натурального числа \nна цифру")

    def radio_natnums_event_6(self):
        self.radio_natnums_event2()
        self.label_info_natnum1.configure(text="Умножение натурального числа \nна 10^k")

    def radio_natnums_event_7(self):
        self.radio_natnums_event2()
        self.label_info_natnum1.configure(text="Умножение натуральных чисел")

    def radio_natnums_event_8(self):
        self.radio_natnums_event3()
        self.label_info_natnum1.configure(
            text="Вычитание из натурального другого \nнатурального, умноженного на \nцифру для случая с неотрицательным \nрезультатом")

    def radio_natnums_event_9(self):
        self.radio_natnums_event2()
        self.label_info_natnum1.configure(
            text="Вычисление первой цифры деления \nбольшего натурального на меньшее, \nдомноженное на 10^k,где k - номер \nпозиции этой цифры (номер считается с нуля)")

    def radio_natnums_event_10(self):
        self.radio_natnums_event2()
        self.label_info_natnum1.configure(
            text="Частное от деления большего натурального \nчисла на меньшее или равное натуральное \nс остатком (делитель отличен от нуля)")

    def radio_natnums_event_11(self):
        self.radio_natnums_event2()
        self.label_info_natnum1.configure(
            text="Остаток от деления большего натурального \nчисла на меньшее или равное натуральное \nс остатком (делитель отличен от нуля)")

    def radio_natnums_event_12(self):
        self.radio_natnums_event2()
        self.label_info_natnum1.configure(text="НОД натуральных чисел")

    def radio_natnums_event_13(self):
        self.radio_natnums_event2()
        self.label_info_natnum1.configure(text="НОК натуральных чисел")

    # =============================================================================================================

    def radio_integer_event_0(self):
        self.radio_integer_event1()
        self.label_info_integer1.configure(text="Абсолютная величина числа, \nрезультат - натуральное")

    def radio_integer_event_1(self):
        self.radio_integer_event1()
        self.label_info_integer1.configure(
            text="Определение положительности числа \n(2 - положительное, 0 — равное \nнулю, 1 - отрицательное)")

    def radio_integer_event_2(self):
        self.radio_integer_event1()
        self.label_info_integer1.configure(text="Умножение целого на (-1)")

    def radio_integer_event_3(self):
        self.radio_integer_event1()
        self.label_info_integer1.configure(text="Преобразование натурального в целое")

    def radio_integer_event_4(self):
        self.radio_integer_event1()
        self.label_info_integer1.configure(text="Преобразование целого неотрицательного\n в натуральное")

    def radio_integer_event_5(self):
        self.radio_integer_event2()
        self.label_info_integer1.configure(text="Сложение целых чисел")

    def radio_integer_event_6(self):
        self.radio_integer_event2()
        self.label_info_integer1.configure(text="Вычитание целых чисел")

    def radio_integer_event_7(self):
        self.radio_integer_event2()
        self.label_info_integer1.configure(text="Умножение целых чисел")

    def radio_integer_event_8(self):
        self.radio_integer_event2()
        self.label_info_integer1.configure(text="Частное от деления целого на целое \n(делитель отличен от нуля)")

    def radio_integer_event_9(self):
        self.radio_integer_event2()
        self.label_info_integer1.configure(text="Остаток от деления целого на целое \n(делитель отличен от нуля)")

    # =============================================================================================================

    def radio_rational_event_0(self):
        self.radio_rational_event1()
        self.label_info_rational1.configure(text="Сокращение дроби")

    def radio_rational_event_1(self):
        self.radio_rational_event1()
        self.label_info_rational1.configure(
            text="Проверка на целое, если рациональное \nчисло является целым, то «да», \nиначе «нет»")

    def radio_rational_event_2(self):
        self.radio_rational_eventZ()
        self.label_info_rational1.configure(text="Преобразование целого в дробное")

    def radio_rational_event_3(self):
        self.radio_rational_event1()
        self.label_info_rational1.configure(text="Преобразование дробного в целое \n(если знаменатель равен 1)")

    def radio_rational_event_4(self):
        self.radio_rational_event2()
        self.label_info_rational1.configure(text="Сложение дробей")

    def radio_rational_event_5(self):
        self.radio_rational_event2()
        self.label_info_rational1.configure(text="Вычитание дробей")

    def radio_rational_event_6(self):
        self.radio_rational_event2()
        self.label_info_rational1.configure(text="Умножение дробей")

    def radio_rational_event_7(self):
        self.radio_rational_event2()
        self.label_info_rational1.configure(text="Деление дробей (делитель \nотличен от нуля)")

    # =============================================================================================================

    def radio_polynual_event_0(self):
        self.radio_polynual_event2()
        self.label_info_polynual1.configure(text="Сложение многочленов")

    def radio_polynual_event_1(self):
        self.radio_polynual_event2()
        self.label_info_polynual1.configure(text="Вычитание многочленов")

    def radio_polynual_event_2(self):
        self.radio_polynual_event_q()
        self.label_info_polynual1.configure(text="Умножение многочлена на рациональное \nчисло")

    def radio_polynual_event_3(self):
        self.radio_polynual_event_k()
        self.label_info_polynual1.configure(text="Умножение многочлена на x^k")

    def radio_polynual_event_4(self):
        self.radio_polynual_event1()
        self.label_info_polynual1.configure(text="Старший коэффициент многочлена")

    def radio_polynual_event_5(self):
        self.radio_polynual_event1()
        self.label_info_polynual1.configure(text="Степень многочлена")

    def radio_polynual_event_6(self):
        self.radio_polynual_event1()
        self.label_info_polynual1.configure(
            text="Вынесение из многочлена НОК знаменателей \nкоэффициентов и НОД числителей")

    def radio_polynual_event_7(self):
        self.radio_polynual_event2()
        self.label_info_polynual1.configure(text="Умножение многочленов")

    def radio_polynual_event_8(self):
        self.radio_polynual_event2()
        self.label_info_polynual1.configure(text="Частное от деления многочлена на \nмногочлен при делении с остатком")

    def radio_polynual_event_9(self):
        self.radio_polynual_event2()
        self.label_info_polynual1.configure(text="Остаток от деления многочлена на \nмногочлен при делении с остатком")

    def radio_polynual_event_10(self):
        self.radio_polynual_event2()
        self.label_info_polynual1.configure(text="НОД многочленов")

    def radio_polynual_event_11(self):
        self.radio_polynual_event1()
        self.label_info_polynual1.configure(text="Производная многочлена")

    def radio_polynual_event_12(self):
        self.radio_polynual_event1()
        self.label_info_polynual1.configure(text="Преобразование многочлена — кратные \nкорни в простые")


    # =============================================================================================================
    # ====================================== Функции для загрузки полей ввода =====================================
    # =============================================================================================================


    def radio_natnums_event1(self):
        self.hide_entry_natnum()
        self.entry_natnum1.grid(row=2, column=0, columnspan=2, pady=20, padx=20, sticky="we")

    def radio_natnums_event2(self):
        self.hide_entry_natnum()
        self.entry_natnum1.grid(row=2, column=0, columnspan=2, pady=20, padx=20, sticky="we")
        self.entry_natnum2.grid(row=3, column=0, columnspan=2, pady=20, padx=20, sticky="we")

    def radio_natnums_event3(self):
        self.hide_entry_natnum()
        self.entry_natnum1.grid(row=2, column=0, columnspan=2, pady=20, padx=20, sticky="we")
        self.entry_natnum2.grid(row=3, column=0, columnspan=2, pady=20, padx=20, sticky="we")
        self.entry_natnum3.grid(row=4, column=0, columnspan=2, pady=20, padx=20, sticky="we")

    # =============================================================================================================

    def radio_integer_event1(self):
        self.hide_entry_integer()
        self.entry_integer1.grid(row=2, column=0, columnspan=2, pady=20, padx=20, sticky="we")

    def radio_integer_event2(self):
        self.hide_entry_integer()
        self.entry_integer1.grid(row=2, column=0, columnspan=2, pady=20, padx=20, sticky="we")
        self.entry_integer2.grid(row=3, column=0, columnspan=2, pady=20, padx=20, sticky="we")

    # =============================================================================================================

    def radio_rational_event1(self):
        self.hide_entry_rational()
        self.frame_entry_rational1.grid(row=2, column=0, columnspan=2, pady=20, padx=20, sticky="we")
        self.entry_rational1_num.grid(row=0, column=0, columnspan=1, pady=5, padx=5, sticky="we")
        self.entry_rational1_den.grid(row=0, column=1, columnspan=1, pady=5, padx=5, sticky="ew")

    def radio_rational_event2(self):
        self.hide_entry_rational()
        self.frame_entry_rational1.grid(row=2, column=0, columnspan=2, pady=20, padx=20, sticky="we")
        self.entry_rational1_num.grid(row=0, column=0, columnspan=1, pady=5, padx=5, sticky="we")
        self.entry_rational1_den.grid(row=0, column=1, columnspan=1, pady=5, padx=5, sticky="ew")
        self.frame_entry_rational2.grid(row=3, column=0, columnspan=2, pady=20, padx=20, sticky="we")
        self.entry_rational2_num.grid(row=0, column=0, columnspan=1, pady=5, padx=5, sticky="we")
        self.entry_rational2_den.grid(row=0, column=1, columnspan=1, pady=5, padx=5, sticky="ew")

    def radio_rational_eventZ(self):
        self.hide_entry_rational()
        self.entry_rational1.grid(row=2, column=0, columnspan=2, pady=20, padx=20, sticky="we")

    # =============================================================================================================

    def radio_polynual_event_k(self):  # степень k числа x
        self.hide_entry_polynual()
        self.entry_polynual1.grid(row=2, column=0, columnspan=2, pady=20, padx=20, sticky="we")
        self.entry_polynual3.grid(row=3, column=0, columnspan=2, pady=20, padx=20, sticky="we")

    def radio_polynual_event_q(self):  # рациональное число
        self.hide_entry_polynual()
        self.entry_polynual1.grid(row=2, column=0, columnspan=2, pady=20, padx=20, sticky="we")
        self.frame_entry_rational.grid(row=3, column=0, columnspan=2, pady=20, padx=20, sticky="we")
        self.entry_rational_num.grid(row=0, column=0, columnspan=1, pady=5, padx=5, sticky="we")
        self.entry_rational_den.grid(row=0, column=1, columnspan=1, pady=5, padx=5, sticky="ew")

    def radio_polynual_event1(self):
        self.hide_entry_polynual()
        self.entry_polynual1.grid(row=2, column=0, columnspan=2, pady=20, padx=20, sticky="we")

    def radio_polynual_event2(self):
        self.hide_entry_polynual()
        self.entry_polynual1.grid(row=2, column=0, columnspan=2, pady=20, padx=20, sticky="we")
        self.entry_polynual2.grid(row=3, column=0, columnspan=2, pady=20, padx=20, sticky="we")

    def radio_polynual_event3(self):
        self.hide_entry_polynual()
        self.entry_polynual1.grid(row=2, column=0, columnspan=2, pady=20, padx=20, sticky="we")
        self.entry_polynual2.grid(row=3, column=0, columnspan=2, pady=20, padx=20, sticky="we")
        self.entry_polynual3.grid(row=4, column=0, columnspan=2, pady=20, padx=20, sticky="we")


    # =============================================================================================================
    # ================================= Функции для вызова окон и других функций ==================================
    # =============================================================================================================


    def hide_entry_natnum(self):
        self.entry_natnum1.grid_forget()
        self.entry_natnum2.grid_forget()
        self.entry_natnum3.grid_forget()

    def hide_entry_integer(self):
        self.entry_integer1.grid_forget()
        self.entry_integer2.grid_forget()

    def hide_entry_rational(self):
        self.entry_rational1.grid_forget()
        self.entry_rational1_num.grid_forget()
        self.entry_rational1_den.grid_forget()
        self.entry_rational2_num.grid_forget()
        self.entry_rational2_den.grid_forget()
        self.frame_entry_rational2.grid_forget()
        self.frame_entry_rational1.grid_forget()

    def hide_entry_polynual(self):
        self.entry_polynual1.grid_forget()
        self.entry_polynual2.grid_forget()
        self.entry_polynual3.grid_forget()
        self.entry_rational_num.grid_forget()
        self.entry_rational_den.grid_forget()
        self.frame_entry_rational.grid_forget()

    def hide_menu_frames(self):
        self.frame_right_info.grid_forget()
        self.frame_right_natnum.grid_forget()
        self.frame_right_integer.grid_forget()
        self.frame_right_rational.grid_forget()
        self.frame_right_polynual.grid_forget()
        self.button_info.configure(fg_color=("gray75", "gray30"))
        self.button_natnum.configure(fg_color=("gray75", "gray30"))
        self.button_integer.configure(fg_color=("gray75", "gray30"))
        self.button_rational.configure(fg_color=("gray75", "gray30"))
        self.button_polynual.configure(fg_color=("gray75", "gray30"))

    def hide_radio_frames(self):
        self.frame_body_natnum.grid_forget()
        self.frame_body_integer.grid_forget()
        self.frame_body_rational.grid_forget()
        self.frame_body_polynual.grid_forget()


    # =============================================================================================================
    # ================================= Функции для управления параметрами окон ===================================
    # =============================================================================================================


    def button_info_event(self):
        self.hide_menu_frames()
        self.frame_right_info.grid(row=0, column=1, sticky="nswe", padx=20, pady=20)
        if self.switch_dark_theme.get() == 1:
            self.button_info.configure(fg_color=("gray75", "#5c8da4"))
        else:
            self.button_info.configure(fg_color=("#7db8d4"))
        print("Нажата кнопка вызова окна для выполнения функций для отображения информации о программе")

    def button_natnum_event(self):
        self.hide_menu_frames()
        self.frame_right_natnum.grid(row=0, column=1, sticky="nswe", padx=20, pady=20)
        if self.switch_dark_theme.get() == 1:
            self.button_natnum.configure(fg_color=("gray75", "#5c8da4"))
        else:
            self.button_natnum.configure(fg_color=("#7db8d4"))
        print("Нажата кнопка вызова окна для выполнения функций для натуральных чисел")

    def button_integer_event(self):
        self.hide_menu_frames()
        self.frame_right_integer.grid(row=0, column=1, sticky="nswe", padx=20, pady=20)
        if self.switch_dark_theme.get() == 1:
            self.button_integer.configure(fg_color=("gray75", "#5c8da4"))
        else:
            self.button_integer.configure(fg_color=("#7db8d4"))
        print("Нажата кнопка вызова окна для выполнения функций для целых чисел")

    def button_rational_event(self):
        self.hide_menu_frames()
        self.frame_right_rational.grid(row=0, column=1, sticky="nswe", padx=20, pady=20)
        if self.switch_dark_theme.get() == 1:
            self.button_rational.configure(fg_color=("gray75", "#5c8da4"))
        else:
            self.button_rational.configure(fg_color=("#7db8d4"))
        print("Нажата кнопка вызова окна для выполнения функций для рациональных чисел")

    def button_polynual_event(self):
        self.hide_menu_frames()
        self.frame_right_polynual.grid(row=0, column=1, sticky="nswe", padx=20, pady=20)
        if self.switch_dark_theme.get() == 1:
            self.button_polynual.configure(fg_color=("gray75", "#5c8da4"))
        else:
            self.button_polynual.configure(fg_color=("#7db8d4"))
        print("Нажата кнопка вызова окна для выполнения функций для многочленов")

    def change_mode(self):
        if self.switch_dark_theme.get() == 1:
            customtkinter.set_appearance_mode("Dark")
        else:
            customtkinter.set_appearance_mode("Light")

    def on_closing(self, event=0):
        self.destroy()

    def start(self):
        self.mainloop()


    # =============================================================================================================
    # ======================================== Иничиализация программы ============================================
    # =============================================================================================================


if __name__ == "__main__":
    app = App()
    app.start()