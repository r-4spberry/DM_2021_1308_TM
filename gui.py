import logging
import os
import threading
import time
import tkinter as tk
import tkinter.messagebox as msg
import tkinter.scrolledtext as ScrolledText
import configparser
import sys

from datetime import datetime
from tkinter import INSERT, filedialog, ttk

import customtkinter as ctk
from PIL import Image
from serial import Serial
from serial.serialutil import SerialException
from serial.tools.list_ports_windows import comports
from wakepy import keep
from typing import List
from tester import ElArc, Logger, Test


class MyLabelFrame(tk.LabelFrame):
    labelframes = []

    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)

        self.configure(relief=tk.FLAT)

        self.labelframes.append(self)

    @classmethod
    def change_mode(cls, dark):
        for i in cls.labelframes:
            if dark:
                i.configure(bg="#2B2B2B")
                i.configure(fg="#FFFFFF")
            else:
                i.configure(bg="#DBDBDB")
                i.configure(fg="#000000")


# The WidgetLogger class is a logging handler.
class WidgetLogger(logging.Handler):
    def __init__(self, widget):
        """WidgetLogger initialization.

        Parameters
        ----------
        widget
            The "widget" parameter is the text widget that you want to work with.

        """
        logging.Handler.__init__(self)

        self.widget = widget

    def emit(self, record):  # sourcery skip: extract-duplicate-method
        fully_scrolled_down = self.widget.yview()[1] == 1.0
        if ctk.get_appearance_mode() == "Light":
            self.widget.tag_config("test", foreground="#039660")
            self.widget.tag_config("error", foreground="#8B0000")
            self.widget.tag_config("important", foreground="#00008B")
            self.widget.tag_config("normal", foreground="black")
        else:
            self.widget.tag_config("test", foreground="green")
            self.widget.tag_config("error", foreground="red")
            self.widget.tag_config("important", foreground="blue")
            self.widget.tag_config("normal", foreground="white")
        # print(ctk.get_appearance_mode())
        if "=================" in record.msg:
            self.widget.insert(INSERT, record.msg + "\n\n", "test")
        elif record.levelno == 40:
            self.widget.insert(INSERT, record.msg + "\n\n", "error")
        elif record.levelno == 30:
            self.widget.insert(INSERT, record.msg + "\n\n", "important")
        else:
            self.widget.insert(INSERT, record.msg + "\n\n", "normal")

        if fully_scrolled_down:
            self.widget.see(tk.END)


class GUI:
    def __init__(self):
        # print(__name__)
        self.end_test = False

    def draw(self, first=False):
        """The function `draw` is used to update the graphical interface by placing and configuring various
        buttons and labels based on certain conditions.

        Parameters
        ----------
        first, optional
            The `first` parameter is a boolean flag that indicates whether it is the first time the `draw`
        method is being called. If `first` is `True`, then the `initial_draw` method is called before
        the rest of the code in the `draw` method is executed.

        """
        if first:
            self._initial_draw()

        n = 0
        for i in range(20):
            self.feeder_buttons[i][0].place_forget()
            self.feeder_buttons[i][1].place_forget()
            self.feeder_buttons[i][2].place_forget()
            self.feeder_labels[i].place_forget()

            if (
                self.pressed_button_a[0] != None
                and self.checkboxes[self.pressed_button_a[0]].get() == 0
            ):
                self.feeder_buttons[self.pressed_button_a[0]][
                    self.pressed_button_a[1]
                ].configure(fg_color="grey")
                self.pressed_button_a = [None, None]

            if (
                self.pressed_button_b[0] != None
                and self.checkboxes[self.pressed_button_b[0]].get() == 0
            ):
                self.feeder_buttons[self.pressed_button_b[0]][
                    self.pressed_button_b[1]
                ].configure(fg_color="grey")
                self.pressed_button_b = [None, None]

            if self.checkboxes[i].get() == 1:
                self.con_labels[i].configure(fg_color="green", bg_color="green")
            else:
                self.con_labels[i].configure(fg_color="grey", bg_color="grey")
            self.con_labels[i].lift()

            if i >= 10:
                self.con_labels[i].place(x=549 - ((i - 10) * 50) - 20, y=28 + 60)
            else:
                self.con_labels[i].place(x=99 + i * 50 - 20, y=287 + 60)

            if i in self.ext_con:
                continue

            if self.checkboxes[i].get() == 1:
                self.feeder_labels[i].configure(anchor="center")
                self.feeder_labels[i].place(x=30 + (n * 45), y=390 + 100)

                self.feeder_buttons[i][0].place(x=30 + (n * 45), y=420 + 100)
                self.feeder_buttons[i][1].place(x=30 + (n * 45), y=470 + 100)
                self.feeder_buttons[i][2].place(x=30 + (n * 45), y=540 + 100)

                n += 1

        self.line.place_forget()
        if len(self.ext_con) != 0:
            self.line.place(
                x=30 + (n * 45) + 8, y=385 + 100, height=5 + 5 + 50 + 70 + 50 + 30
            )

        for i in range(20):
            if i not in self.ext_con:
                continue
            if self.checkboxes[i].get() == 1:
                self.feeder_labels[i].configure(anchor="center")
                self.feeder_labels[i].place(x=30 + (n * 45) + 20, y=390 + 100)

                self.feeder_buttons[i][0].place(x=30 + (n * 45) + 20, y=420 + 100)
                self.feeder_buttons[i][1].place(x=30 + (n * 45) + 20, y=470 + 100)
                self.feeder_buttons[i][2].place(x=30 + (n * 45) + 20, y=540 + 100)

                n += 1

    def _initial_draw(self):
        """The function `initial_draw` sets the initial positions of various widgets on the GUI."""

        self.pic_label.place(x=50, y=60 + 30 - 2)
        self.tabview.place(x=630, y=30 * 2)

        for i in range(10):
            self.checkboxes[i].place(x=101 + i * 50 - 20, y=313 + 60)

        for i in range(19, 9, -1):
            self.checkboxes[i].place(x=552 - ((i - 10) * 50) - 20, y=0 + 60)

        self.disable_all.place(x=630, y=30)

        for n, widget in enumerate(self.settings):
            widget.grid(column=n // 5, row=n % 5, padx=60, pady=5)

        for n, widget in enumerate(self.test):
            widget.grid(column=n // 5, row=n % 5, padx=60, pady=5)
        self.log.pack(padx=5, pady=5)

    def _on_closing(self):
        """The function checks if the user wants to quit and if so, destroys the window and sets the
        end_test variable to True.
        """
        if msg.askokcancel("Quit", "Do you want to quit?"):
            self.window.destroy()
            self.end_test = True

    def _ext_con_check(self, widget, n):
        if n in self.ext_con:
            self.ext_con.remove(n)
            widget.configure(text=f"{n}")
        else:
            self.ext_con.append(n)
            widget.configure(text=f"ext{n}")

        self.draw()

    def main(self):
        """
        The main function creates a GUI window and sets up various widgets and buttons for feeder
        testing.
        """
        self.window = ctk.CTk()
        self.window.title("Feeder testing")
        self.window.geometry("1200x730")
        self.window.resizable(False, False)

        config = configparser.ConfigParser()
        config.read("settings.ini")

        self.checkboxes = [None for _ in range(20)]
        self.feeder_labels = []
        self.feeder_buttons = [[] for _ in range(20)]
        self.feeder_buttons_enabled = [False for _ in range(20)]
        self.con_labels = [None for _ in range(20)]
        self.pressed_button_a = [None, None]
        self.pressed_button_b = [None, None]
        self.after_id = None

        self.ext_con = []

        for i in range(10):
            self.checkboxes[i] = ctk.CTkCheckBox(
                self.window, text=f"", command=self.draw
            )
            self.con_labels[i] = ctk.CTkButton(
                self.window, text=f"{i}", width=31, height=21, text_color="white"
            )
            self.con_labels[i].configure(
                command=lambda widget=self.con_labels[i], n=i: self._ext_con_check(
                    widget, n
                )
            )

        for i in range(19, 9, -1):
            self.checkboxes[i] = ctk.CTkCheckBox(
                self.window, text=f"", command=self.draw
            )
            self.con_labels[i] = ctk.CTkButton(
                self.window, text=f"{i}", width=31, height=20, text_color="white"
            )
            self.con_labels[i].configure(
                command=lambda widget=self.con_labels[i], n=i: self._ext_con_check(
                    widget, n
                )
            )

        for i in range(20):
            self._create_feeder_widgets(i)

        self.line = ttk.Separator(self.window, orient=ctk.VERTICAL)
        self.disable_all = ctk.CTkButton(
            self.window,
            fg_color="grey",
            text_color="white",
            text="Disable all",
            command=self._disable_all_feeders,
        )
        self.window.protocol("WM_DELETE_WINDOW", self._on_closing)

        self.tabview = ctk.CTkTabview(self.window, width=540)
        self.tabview.add("Test")
        self.tabview.add("Log")
        self.tabview.add("Settings")

        self.Dselect_style = MyLabelFrame(
            self.tabview.tab("Settings"), text="Dark mode:"
        )
        self.Fselect_style = ctk.CTkSwitch(
            self.Dselect_style, command=lambda: self._configure_style(), text=""
        )

        dark = int(config["variables"]["dark"])
        if dark:
            self.Fselect_style.select()
        else:
            self.Fselect_style.deselect()

        self.Fselect_style.grid(column=0, row=0)
        self.style = ttk.Style()
        self._configure_style(True)

        # self.Lcom_port = ctk.CTkLabel(
        #     self.tabview.tab("Settings"), text="COM port:"
        # )
        # self.Lbaudrate = ctk.CTkLabel(
        #     self.tabview.tab("Settings"), text="Select baudrate:"
        # )
        # self.Lconnection_type = ctk.CTkLabel(
        #     self.tabview.tab("Settings"), text="Connection type:"
        # )
        # self.Larc_type = ctk.CTkLabel(
        #     self.tabview.tab("Settings"), text="Arc detection type:"
        # )

        self.Dcom_port = MyLabelFrame(self.tabview.tab("Settings"), text="COM port:")

        self.Dbaudrate = MyLabelFrame(self.tabview.tab("Settings"), text="Baudrate:")

        self.Dconnection_type = MyLabelFrame(
            self.tabview.tab("Settings"), text="Connection type:"
        )

        self.Darc_type = MyLabelFrame(
            self.tabview.tab("Settings"), text="Arc detection type:"
        )

        self.Fcom_port = ctk.CTkComboBox(
            self.Dcom_port,
            values=["Select COM port"] + list(map(lambda x: list(x)[0], comports())),
        )

        def _update_com_ports():
            if ["Select COM port"] + list(
                map(lambda x: list(x)[0], comports())
            ) != self.Fcom_port._values:
                self.Fcom_port.configure(
                    values=["Select COM port"]
                    + list(map(lambda x: list(x)[0], comports()))
                )
            self.Fcom_port.after(1000, _update_com_ports)

        self.Fcom_port.after(1000, _update_com_ports)

        self.Fbaudrate = ctk.CTkComboBox(
            self.Dbaudrate,
            values=["Select baudrate"] + list(map(str, Serial.BAUDRATES)),
        )
        self.Fconnection_type = ctk.CTkComboBox(
            self.Dconnection_type,
            values=["Select connection type"] + ["Wireless Lan", "ArcNet"],
        )
        self.Farc_type = ctk.CTkComboBox(
            self.Darc_type,
            values=["Select arc type"] + ["General", "Alternative"],
        )

        self.Fcom_port.set(config["variables"]["com"])
        self.Fbaudrate.set(config["variables"]["baudrate"])
        self.Fconnection_type.set(config["variables"]["connection_type"])
        self.Farc_type.set(config["variables"]["arc_type"])

        self.Fcom_port.configure(state="readonly")
        self.Fbaudrate.configure(state="readonly")
        self.Fconnection_type.configure(state="readonly")
        self.Farc_type.configure(state="readonly")

        self.Fbaudrate.grid(column=0, row=0)
        self.Fcom_port.grid(column=0, row=0)
        self.Fconnection_type.grid(column=0, row=0)
        self.Farc_type.grid(column=0, row=0)

        self.Bstart_test = ctk.CTkButton(
            self.tabview.tab("Test"), text="Start tests", command=self._start_tests
        )
        self.Bend_test = ctk.CTkButton(
            self.tabview.tab("Test"), text="End tests", command=self._end_tests
        )
        self.Bend_test.configure(state="disabled")
        self.Bkill_test = ctk.CTkButton(
            self.tabview.tab("Test"), text="Kill tests", command=self._kill_tests
        )
        self.Bkill_test.configure(state="disabled")
        self.log = ScrolledText.ScrolledText(
            self.tabview.tab("Log"), width=55, height=17
        )
        self.CBsave_png = ctk.CTkCheckBox(
            self.tabview.tab("Test"),
            text="Save png oscillogram",
            command=self._save_png,
        )
        self.save_png = self.CBsave_png.get()

        self.Dfolder = MyLabelFrame(self.tabview.tab("Settings"), text="Folder:")

        self.Bfolder = ctk.CTkButton(
            self.Dfolder, text="Set test folder", command=self._get_folder
        )
        self.Bfolder.grid(column=0, row=0)
        self.folder = "Standard"

        pilimg = Image.open(self.resource_path("res/new_cb.png"))
        self.pic = ctk.CTkImage(pilimg, size=pilimg.size)
        self.pic_label = ctk.CTkLabel(
            self.window,
            image=self.pic,
            width=pilimg.size[0],
            height=pilimg.size[1],
            text="",
        )

        # self.Lnumber_of_tests = ctk.CTkLabel(self.tabview.tab("Test"), text="Number of tests:")
        # self.Ltest_time = ctk.CTkLabel(self.tabview.tab("Test"), text="Test time:")
        # self.Ltime_between = ctk.CTkLabel(self.tabview.tab("Test"), text="Time between tests:")
        # self.Loverlap_time = ctk.CTkLabel(self.tabview.tab("Test"), text="Overlap time:")

        self.Dnumber_of_tests = MyLabelFrame(
            self.tabview.tab("Test"), text="Number of tests:"
        )
        self.Dtest_time = MyLabelFrame(self.tabview.tab("Test"), text="Test time:")
        self.Dtime_between = MyLabelFrame(
            self.tabview.tab("Test"), text="Time between tests:"
        )
        # self.Doverlap_time = MyLabelFrame(
        #     self.tabview.tab("Test"), text="Overlap time:"
        # )
        self.Ddelay_time = MyLabelFrame(
            self.tabview.tab("Test"), text="Delay time (s):"
        )

        self.Fnumber_of_tests = ctk.CTkEntry(self.Dnumber_of_tests)
        self.Ftest_time = ctk.CTkEntry(self.Dtest_time)
        self.Ftime_between = ctk.CTkEntry(self.Dtime_between)
        # self.foverlap_time = ctk.CTkEntry(
        #     self.Doverlap_time, placeholder_text="Overlap time"
        # )
        self.Fdelay_time = ctk.CTkEntry(self.Ddelay_time)

        self.Fnumber_of_tests.grid(row=0, column=0)
        self.Fnumber_of_tests.insert(0, "1")
        self.Ftest_time.grid(row=0, column=0)
        self.Ftest_time.insert(0, "5")
        self.Ftime_between.grid(row=0, column=0)
        self.Ftime_between.insert(0, "0")
        self.Fdelay_time.grid(row=0, column=0)
        self.Fdelay_time.insert(0, "0")
        self.test = [
            self.Dnumber_of_tests,
            self.Dtest_time,
            self.Dtime_between,
            self.CBsave_png,
            self.Ddelay_time,
            self.Bstart_test,
            self.Bend_test,
            self.Bkill_test,
        ]

        self.settings = [
            self.Dfolder,
            self.Dcom_port,
            self.Dbaudrate,
            self.Dconnection_type,
            self.Darc_type,
            self.Dselect_style,
        ]

        self._configure_style(True)
        self.draw(True)
        self.window.mainloop()

    def _configure_style(self, first=False):
        # print(#print(ctk.get_appearance_mode()))
        if self.Fselect_style.get():
            self._set_style("dark", "#2B2B2B", "white")
            MyLabelFrame.change_mode(True)
            if not first:
                self.log.configure(background="#202020", foreground="white")
        else:
            self._set_style("light", "#DBDBDB", "black")
            MyLabelFrame.change_mode(False)
            if not first:
                self.log.configure(background="white", foreground="black")
        if not first:
            self.draw(True)
        else:
            self.style.configure(
                "TLabelframe",
                background="grey",
                bordercolor="#2B2B2B",
            )
            self.style.configure(
                "Tlabelframe.Label", background="grey", foreground="white"
            )

    def _set_style(self, arg0, background, foreground):
        ctk.set_appearance_mode(arg0)

    def _create_feeder_widgets(self, i):
        self.feeder_labels.append(
            ctk.CTkLabel(self.window, text=f"{i}", width=40, height=30)
        )
        self.feeder_buttons[i].append(
            ctk.CTkButton(self.window, fg_color="grey", text="СШ", width=40, height=50)
        )
        self.feeder_buttons[i][0].configure(
            command=lambda widget=[self.feeder_buttons[i][0], i, 0]: self._button(widget)
        )
        self.feeder_buttons[i].append(
            ctk.CTkButton(self.window, fg_color="grey", text="BB", width=40, height=70)
        )
        self.feeder_buttons[i][1].configure(
            command=lambda widget=[self.feeder_buttons[i][1], i, 1]: self._button(widget)
        )
        self.feeder_buttons[i].append(
            ctk.CTkButton(self.window, fg_color="grey", text="KO", width=40, height=50)
        )
        self.feeder_buttons[i][2].configure(
            command=lambda widget=[self.feeder_buttons[i][2], i, 2]: self._button(widget)
        )

    def _save_png(self):
        self.save_png = self.CBsave_png.get()

    def _get_folder(self):
        folder = filedialog.askdirectory()

        if len(os.listdir(folder)) != 0 and not msg.askyesno(
            "Warning",
            "Selected Folder is not empty, do you want to continue?",
            master=self.window,
        ):
            return

        self.folder = folder
        self.Lfolder.configure(text=f"Folder: {self.folder}")

    def _checks(self):
        if self.Fcom_port.get() == "Select COM port":
            msg.showerror("Error", "Select COM port", master=self.window)
            return False

        if self.Fbaudrate.get() == "Select baudrate":
            msg.showerror("Error", "Select baudrate", master=self.window)
            return False

        if (
            not self.Fnumber_of_tests.get().isnumeric()
            or int(self.Fnumber_of_tests.get()) < 1
        ):
            msg.showerror(
                "Error",
                "Number of tests must be a positive integer",
                master=self.window,
            )
            return False

        if not self.Ftest_time.get().isnumeric() or float(self.Ftest_time.get()) < 5:
            msg.showerror(
                "Error",
                "Test time must be a positive float, at lest 5s",
                master=self.window,
            )
            return False

        if not self.Fdelay_time.get().isnumeric() or float(self.Fdelay_time.get()) < 0:
            msg.showerror(
                "Error",
                "Delay time must be a positive float",
                master=self.window,
            )
            return False

        if (
            not self.Ftime_between.get().isnumeric()
            or float(self.Ftime_between.get()) < 0
        ):
            msg.showerror(
                "Error",
                "Time between tests must be a positive float",
                master=self.window,
            )
            return False
        # if self.pressed_button_b[0] != None and (
        #     not self.foverlap_time.get().isnumeric
        #     or float(self.foverlap_time.get()) < 0
        # ):
        #     msg.showerror(
        #         "Error", "Overlap time must be a positive float", master=self.window
        #     )
        #     return False

        # if (
        #     self.pressed_button_b[0] != None
        #     and float(self.Ftest_time.get()) - float(self.foverlap_time.get()) < 3
        # ):
        #     msg.showerror(
        #         "Error",
        #         "Difference between test time and overlap time must be at least 3s",
        #         master=self.window,
        #     )
        #     return False

        if self.pressed_button_a == [None, None] and self.pressed_button_b == [
            None,
            None,
        ]:
            msg.showerror(
                "Error",
                "Select at lest one feeder compartment for an arc",
                master=self.window,
            )
            return False

        return True

    def _generate_el_arc(self, channel) -> ElArc:
        if channel == "a":
            return ElArc(
                feeder=self.pressed_button_a[0],
                compartment=self.pressed_button_a[1],
                feeders=list(
                    filter(lambda x: self.checkboxes[x].get() == 1, range(20))
                ),
            )
        elif channel == "b":
            return ElArc(
                feeder=self.pressed_button_b[0],
                compartment=self.pressed_button_b[1],
                feeders=list(
                    filter(lambda x: self.checkboxes[x].get() == 1, range(20))
                ),
            )
        else:
            raise ValueError("Unknown channel")

    def resource_path(self, relative_path):
        """Get absolute path to resource, works for dev and for PyInstaller"""
        try:
            # PyInstaller creates a temp folder and stores path in _MEIPASS
            base_path = sys._MEIPASS
        except Exception:
            base_path = os.path.abspath(".")

        return os.path.join(base_path, relative_path)

    def _end_tests(self):
        if self.after_id is None:
            self.end_test = True
            self.Bend_test.configure(state="disabled")
        else:
            self.window.after_cancel(self.after_id)
            self.after_id = None
            self.Bend_test.configure(state="disabled")
            self.Bstart_test.configure(state="normal")
            fbuttons = []
            for i in self.feeder_buttons:
                fbuttons += i
            for widget in [self.Bstart_test] + fbuttons + self.checkboxes:
                widget.configure(state="normal")
            self.Bend_test.configure(state="disabled")

    def _kill_tests(self):
        pass

    def _start_tests(self):
        def _start_tests_thread():
            self.after_id = None
            self.end_test = False
            if not self._checks():
                return

            with keep.running() as k:
                fbuttons = []
                for i in self.feeder_buttons:
                    fbuttons += i
                for widget in [self.Bstart_test] + fbuttons + self.checkboxes:
                    widget.configure(state="disabled")
                self.Bend_test.configure(state="normal")
                with Serial() as ser:
                    ser.baudrate = int(self.Fbaudrate.get())
                    ser.port = self.Fcom_port.get()
                    ser.timeout = 1
                    try:
                        ser.open()
                    except SerialException:
                        msg.showerror(
                            "Error", "Can not open a serial port", master=self.window
                        )
                        for widget in [self.Bstart_test] + fbuttons + self.checkboxes:
                            widget.configure(state="normal")
                        self.Bend_test.configure(state="disabled")
                        return
                    thread = None
                    timestamp = datetime.now().strftime("%d-%m-%Y %H-%M-%S")
                    channels = []
                    if self.pressed_button_a != [None, None]:
                        channels.append("a")
                    if self.pressed_button_b != [None, None]:
                        channels.append("b")
                    for i in range(int(self.Fnumber_of_tests.get())):
                        for channel in channels:
                            if self.end_test:
                                break
                            thread = threading.Thread(
                                target=_test,
                                args=(
                                    i,
                                    timestamp,
                                    ser,
                                    self._generate_el_arc(channel),
                                    channel,
                                ),
                            )
                            thread.start()
                            while thread.is_alive():
                                time.sleep(0.1)
                            time.sleep(int(self.Ftime_between.get()))

                for widget in [self.Bstart_test] + fbuttons + self.checkboxes:
                    widget.configure(state="normal")
                self.Bend_test.configure(state="disabled")

        def _start_thread():
            self.thread = threading.Thread(target=_start_tests_thread)
            self.thread.start()

        if not self._checks():
            return
        fbuttons = []
        for i in self.feeder_buttons:
            fbuttons += i
        for widget in [self.Bstart_test] + fbuttons + self.checkboxes:
            widget.configure(state="disabled")
        self.Bend_test.configure(state="normal")
        self.after_id = self.window.after(
            int(self.Fdelay_time.get()) * 1000, _start_thread
        )

        def _test(i, timestamp, ser, el_arc, channel):
            # print(channel)
            handler = WidgetLogger(self.log)
            folder = (
                f"tests/testing #{timestamp}/test {channel}"
                if self.folder == "Standard"
                else f"{self.folder}/test {channel}"
            )
            logger = Logger(test_number=i, folder=folder, handler=handler)
            # set timestamp as dd-mm-YYYY ss:mm:hh
            test = Test(
                logger=logger,
                serial_port=ser,
                channel=channel,
                starting_letter="z"
                if i % 4 == 0
                else "Z"
                if i % 4 == 1
                else "q"
                if i % 4 == 2
                else "Q",
                el_arc=el_arc,
                arc_detection_type=self.Farc_type.get(),
                connection_type=self.Fconnection_type.get(),
                timestamp=f"{timestamp} #{str(i)}",
                save_osc_png=self.save_png,
                test_time=float(self.Ftest_time.get()),
            )
            test.start_test()

            # except Exception as e:
            #     logger.error("Internal error: " + str(e))
            #     logger.finished_with_errors()

            logger.save_log(f"log {timestamp}")
            logger.save_feeders_data(
                test.feeders, test.required_feeders, f"feeders {timestamp}"
            )

    def _button(self, widget):
        if self.pressed_button_a == widget[1:]:
            widget[0].configure(fg_color="grey")
            self.pressed_button_a = [None, None]
        elif self.pressed_button_b == widget[1:]:
            widget[0].configure(fg_color="grey")
            self.pressed_button_b = [None, None]
        elif self.pressed_button_a == [None, None]:
            widget[0].configure(fg_color="green")
            self.pressed_button_a = widget[1:]
        elif self.pressed_button_b == [None, None]:
            widget[0].configure(fg_color="blue")
            self.pressed_button_b = widget[1:]

    def _disable_all_feeders(self):
        for i in range(20):
            self.checkboxes[i].deselect()
        for n, i in enumerate(self.con_labels):
            if n in self.ext_con:
                self._ext_con_check(i, n)
        self.draw()


ctk.set_appearance_mode("light")
GUI().main()
