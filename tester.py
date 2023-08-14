import logging
import os
from io import TextIOWrapper
from struct import unpack
from time import time
from typing import List, Tuple

import matplotlib.pyplot as plt
from serial import Serial

TIME_STEP = 0.0001
FILTRATION_TIME = 0.002
logging.basicConfig(level=logging.INFO)


class WrongStartDataError(Exception):
    """Raised when the start data is not correct"""

    def __init__(self):
        super().__init__()
        logging.error("Wrong start data")


class WrongMessageLengthError(Exception):
    """Raised when the message length is not correct"""

    def __init__(self):
        super().__init__()
        logging.error("Wrong message length")


class OscParse:
    def __init__(self, data):
        """OscParse initialization

        Parameters
        ----------
        data
            The `data` parameter is the input data that will be used to initialize the object.

        """
        self.data = data
        self.feeder = [[] for _ in range(18)]
        self.control = [[] for _ in range(6)]
        self.parsed_data = []

        self._parse_data()

    def _parse_data(self):
        # reading 1000 bytes from data
        res = unpack("<1000Q", self.data)

        # parsing data
        for n, ll in enumerate(res):
            self.parsed_data.append([])

            for bit in range(42):
                # print(ll)
                b = (ll >> bit) & 1
                self.parsed_data[n].append(b)

            # parse feeders bits
            for i in range(18):
                self.feeder[i].append(
                    -self.parsed_data[n][i] + self.parsed_data[n][i + 18]
                )

            # parse control bits
            for i in range(36, 42):
                self.control[i - 36].append(1 - self.parsed_data[n][i])

    def save_to_file(self, filename):
        """The function saves the parsed data to a file, with each item in the data written on a new line.

        Parameters
        ----------
        filename
            The `filename` parameter is a string that represents the filename of the file that you want to save the
        data to.

        """
        with open(f"{filename}", "w") as f:
            for i in self.parsed_data:
                f.write(" ".join(map(str, i)) + "\n")

    def create_plot(self):
        """The `create_plot` function creates a plot with multiple subplots, each displaying a different
        set of data.

        Returns
        -------
            a matplotlib figure object.

        """
        fig, axis = plt.subplots(18 + 6, 1, sharex=True, sharey=False)
        fig.set_size_inches(15, 8)

        for i in range(18):
            axis[i].plot(self.feeder[i])
            self._plot_settings(axis, i)
            axis[i].annotate(
                f"feeder{i}",
                (-0.03, 0.5),
                xycoords="axes fraction",
                ha="right",
                va="center",
            )

        # 0 bit = ArcA; //'a' команда канала А
        # 1 bit = ArcB; //'b' команда канала Б
        # 2 bit = emA; // 'a' от динамика
        # 3 bit = emВ; // 'b' от динамика
        # 4 bit = arcB_check; // Реле фидера канала А
        # 5 bit = arcB_check; // Реле фидера канала В

        for i in range(18, 18 + 6):
            axis[i].plot(self.control[i - 18])
            self._plot_settings(axis, i)

        axis[18].annotate(
            "ArcA", (-0.03, 0.5), xycoords="axes fraction", ha="right", va="center"
        )
        axis[19].annotate(
            "ArcB", (-0.03, 0.5), xycoords="axes fraction", ha="right", va="center"
        )
        axis[20].annotate(
            "emA", (-0.03, 0.5), xycoords="axes fraction", ha="right", va="center"
        )
        axis[21].annotate(
            "emB", (-0.03, 0.5), xycoords="axes fraction", ha="right", va="center"
        )
        axis[22].annotate(
            "arcA_check",
            (-0.03, 0.5),
            xycoords="axes fraction",
            ha="right",
            va="center",
        )
        axis[23].annotate(
            "arcB_check",
            (-0.03, 0.5),
            xycoords="axes fraction",
            ha="right",
            va="center",
        )

        return fig

    def _plot_settings(self, axis, i):
        axis[i].spines["right"].set_visible(False)
        axis[i].spines["left"].set_visible(False)
        axis[i].set_title(f"")
        axis[i].set_ylim([-1.1, 1.1])
        axis[i].set_yticks([])


class Message:
    """Class that contains one message from COM port"""

    codes = {
        "x": "Появление напряжения на управляющем входе имитатора ДЗ фидера A",
        "y": "Появление напряжения на управляющем входе имитатора ДЗ фидера B",
        "X": "Пропадание напряжения на управляющем входе имитатора ДЗ фидера A",
        "Y": "Пропадание напряжения на управляющем входе имитатора ДЗ фидера B",
        "a": "Напряжение на динамике имитатора ДЗ фидера A",
        "b": "Напряжение на динамике имитатора ДЗ фидера B",
        "A": "Замкнут выход IOI, настроеные на сигнал обнаружения дуги фидера A",
        "B": "Замкнут выход IOI, настроеные на сигнал обнаружения дуги фидера B",
        "T": "Импульс отключения в цепи ЭМ ОВ",
        "p": "pong",
        "t": "Время с начала теста",
        "z": "Ответ на запрос сброса счетчика времени",
        "Z": "Ответ на запрос сброса счетчика времени",
        "q": "Ответ на запрос сброса счетчика времени",
        "Q": "Ответ на запрос сброса счетчика времени",
    }

    def __init__(self, bmessage: bytes):
        """Message initialization.

        Parameters
        ----------
        bmessage : bytes
            message from COM port to parse

        """
        if bmessage is None:
            raise ValueError("message must be defined")

        self.bmessage = bmessage
        self.code, self.number, self.time = self._parse_message()

    def _parse_message(self) -> Tuple[str, int, int]:
        if len(self.bmessage) != 5:
            raise WrongMessageLengthError()

        first, second, _, third = unpack("<cBcH", self.bmessage)

        return first.decode(), second, third

    # def get_message(self) -> Tuple[str, int, int]:
    #     return self.message

    def __str__(self):
        return f"Message: {self.code} {self.number} at time: {round(self.time*TIME_STEP, 4)}, {self.codes[self.code]}"


class Logger:
    """Class that handles logging of tests"""

    def __init__(self, test_number: int, folder: str, handler: logging.Handler = None):
        """Logger initialization

        Parameters
        ----------
        test_number : int
            The test number is an integer that represents the specific test being performed. It is used to
        identify and differentiate between different tests.
        folder : str
            The `folder` parameter is a string that represents the directory or folder where the logs will
        be stored. It is used to specify the location where the log files will be saved.
        handler : logging.Handler
            The `handler` parameter is an optional parameter of type `logging.Handler`. It is used to
        specify a custom logging handler that will be used for logging messages. If no handler is
        provided, the default logging handler will be used.

        """
        logger = logging.getLogger()

        if handler and len(logger.handlers) < 2:
            logger.addHandler(handler)

        self.test_number = test_number
        self.log = ""
        self.errors = 0
        self.completed = False
        self.folder = folder
        self._log()

    def save_osc_txt(self, filename: str, osc: OscParse):
        """The function `save_osc_txt` saves an oscilloscope data as a text file.

        Parameters
        ----------
        filename : str
            A string representing the filename of the file to be saved.
        osc : OscParse
            The `osc` parameter is an instance of the `OscParse` class.

        """
        txt_dir = f"{self.folder}/osc/txt"

        if not os.path.exists(txt_dir):
            logging.info(f"{txt_dir} not found, creating it")
            os.makedirs(txt_dir)

        osc.save_to_file(f"{txt_dir}/{filename}.txt")
        logging.info(f"{txt_dir}/{filename}.txt oscilloscope data saved")

    def save_osc_png(self, filename: str, osc: OscParse):
        """The function `save_osc_png` saves an oscilloscope data as a PNG image file.

        Parameters
        ----------
        filename : str
            A string representing the filename of the PNG file to be saved.
        osc : OscParse
            The `osc` parameter is an instance of the `OscParse` class.

        """
        png_dir = f"{self.folder}/osc/png"

        if not os.path.exists(png_dir):
            logging.info(f"{png_dir} not found, creating it")
            os.makedirs(png_dir)

        fig = osc.create_plot()
        fig.savefig(f"{png_dir}/{filename}.png")
        plt.close(fig)
        logging.info("png oscilloscope data saved")

    def _log(self):
        logging.info(f"=================Test {self.test_number}==================")
        self.log += f"=================Test {self.test_number}==================\n"

    def info(self, line: str):
        """The "info" function logs info message.

        Parameters
        ----------
        line : str
            The `line` parameter is a string that represents the log message that needs to be
        displayed.

        """
        logging.info(line)
        self.log += f"{line}\n"

    def error(self, error: str):
        """The function "error" logs error message.

        Parameters
        ----------
        error : str
            The "error" parameter is a string that represents the error message that needs to be
        displayed.

        """
        logging.error(error)
        self.log += f"Error: {error}\n"
        self.errors += 1

    def warning(self, important: str):
        """The function "warning" logs warning message.

        Parameters
        ----------
        important : str
            The "important" parameter is a string that represents the warning message that needs to be
        displayed.

        """
        logging.warning(important)
        self.log += f"!!!!Important: {important}!!!!\n"

    def finished_successfully(self):
        """The function "finished_successfully" is a method that logs that the test is
        finished successfully.

        """
        logging.info(f"=============Test {self.test_number} finished=============")
        self.log += f"=============Test {self.test_number} finished=============\n"

    def finished_with_errors(self):
        """The function "finished_with_errors" is a method that logs that the test is
        finished with errors.
        """
        logging.error(f"=======Test {self.test_number} finished with errors=======")
        self.log += f"=======Test {self.test_number} finished with errors=======\n"

    def save_feeders_data(
        self, feeders: List[int], required_feeders: List[int], filename: str
    ):
        """The function `save_feeders_data` saves feeders data to a csv file.

        Parameters
        ----------
        feeders : List[int]
            A list of integers representing the feeders that need to be saved.
        required_feeders : List[int]
            A list of integers representing the feeders that were expected to open.
        filename : str
            The filename parameter is a string that represents the name of the file.

        """
        csv_file_path = self._path("/feeder_logs", filename, ".csv")

        if not os.path.exists(csv_file_path):
            with open(csv_file_path, "w") as file:
                self._create_feeders_data(file, feeders, required_feeders)

        with open(csv_file_path, "a") as file:
            self._continue_feeders_data(feeders, file)

        return csv_file_path

    def _continue_feeders_data(self, feeders, file):
        file.write(f"test #{self.test_number};")

        for i in feeders:
            if feeders[i] is None:
                file.write("inf" + ";")
            else:
                file.write(f"{str(feeders[i])};")

        file.write("\n")

    def _create_feeders_data(
        self, file: TextIOWrapper, feeders: List[int], required_feeders: List[int]
    ):
        file.write("feeders;")

        for i in feeders:
            file.write(f"{str(i)};")

        file.write("\n")
        file.write("expected;")

        for i in feeders:
            if i in required_feeders:
                file.write("Open" + ";")
            else:
                file.write("Still" + ";")

        file.write("\n")

    def save_log(self, filename):
        """The function saves a log to a specified file.

        Parameters
        ----------
        filename
            The filename parameter is a string that represents the name of the file where the log will be
        saved.

        """
        log_file_path = self._path("/logs", filename, ".txt")

        with open(log_file_path, "a" if os.path.exists(log_file_path) else "w") as f:
            f.write(self.log)

        return log_file_path

    def _path(self, folder, filename, extension):
        feeder_logs_dir = f"{self.folder}{folder}"

        if not os.path.exists(feeder_logs_dir):
            os.makedirs(feeder_logs_dir)

        return f"{feeder_logs_dir}/{filename}{extension}"


class ElArc:
    table_OB = [True, False, False]

    table_PB = [False, True, False]

    table_feeder = [False, False, True]

    def __init__(self, feeder: int, compartment: int, feeders: List[int]):
        """ElArc initialization

        Parameters
        ----------
        feeder : int [0-19]
            An integer representing the feeder number .
        compartment : int [0-2]
            An integer representing the number of compartments in the feeder system.
        feeders : List[int]
            The `feeders` parameter is a list of integers. It represents all available feeders.
        """

        if feeder < 0 or feeder > 19:
            raise ValueError("feeder must be in range [0, 19]")

        if compartment < 0 or compartment > 2:
            raise ValueError("compartment must be in range [0, 2]")

        if feeder not in feeders:
            raise ValueError("feeder must be in the list of feeders")

        self.compartment = compartment
        self.feeder = feeder
        self.feeders = {i: False for i in feeders}

        return self._check_required_feeders(feeder, compartment)

    def _check_required_feeders(self, feeder, compartment):
        if self.compartment == 0 or compartment == 1:
            for i in self.feeders:
                self.feeders[i] = True
            return

        if self.feeder == 0:
            table = ElArc.table_OB
        elif self.feeder == 1:
            table = ElArc.table_PB
        else:
            table = ElArc.table_feeder

        if table[0]:
            self.feeders[0] = True
        if table[1]:
            self.feeders[1] = True
        if table[2]:
            self.feeders[feeder] = True

    def get_feeders(self):
        return self.feeders


class Test:
    def __init__(
        self,
        logger: Logger,
        serial_port: Serial,
        channel: str = "a",
        starting_letter: str = "q",
        feeders: List[int] = None,
        required_feeders: List[int] = None,
        el_arc: ElArc = None,
        connection_type: str = None,
        arc_detection_type: str = None,
        timestamp=None,
        save_osc_txt: bool = True,
        save_osc_png: bool = False,
        test_time: int = 6,
    ):
        """Test Initialization

        Parameters
        ----------
        logger : Logger
            The logger parameter is of type Logger, which is a logging object used for logging messages and
        errors in the code.
        serial_port : Serial
            The serial port to communicate with the hardware device.
        channel : str, optional [a, b]
            Thel channe parameter is a string that represents the channel to be used. ("a" by default)
        starting_letter : str, optional
            The starting letter parameter is a string that represents starting code for the tester.
        feeders : List[int] (only if el_arc is not specified)
            The `feeders` parameter is a list of integers that represents the feeders available for the
        system.
        required_feeders : List[int] (only if el_arc is not specified)
            The `required_feeders` parameter is a list of integers that specifies the feeders that are
        expected to open.
        el_arc : ElArc
        connection_type: str
        arc_detection_type: str
        timestamp
            The `timestamp` parameter is used to specify a timestamp for the logs. It is an
        optional parameter and if not provided, it will default to time.time()
        save_osc_txt : bool, optional
            The `save_osc_txt` parameter is a boolean flag that determines whether the oscilloscope data
        should be saved as a text file.
        save_osc_png : bool, optional
            The `save_osc_png` parameter is a boolean flag that determines whether to save the Open Sound
        Control (OSC) data as a PNG file.
        test_time : int, optional
            The `test_time` parameter is an integer that represents the duration of the test in seconds.

        """
        if connection_type is None:
            raise ValueError("connection_type must be defined")
        else:
            self.connection_type = connection_type
        if arc_detection_type is None:
            raise ValueError("arc_detection_type must be defined")
        else:
            self.arc_detection_type = arc_detection_type
        if timestamp is None:
            raise ValueError("timestamp must be defined")
        else:
            self.timestamp = timestamp
        if el_arc is None and required_feeders is None and feeders is None:
            raise ValueError("el_arc or feeders must be defined")

        if el_arc != None and (feeders != None or required_feeders != None):
            raise ValueError("el_arc and feeders cannot be defined at the same time")

        if channel not in ["a", "b"]:
            raise ValueError("channel must be a or b")

        self.channel = channel
        self.serial_port = serial_port
        self.starting_letter = starting_letter
        self.test_time = test_time
        self.logger = logger

        if el_arc is None:
            self.feeders = {i: None for i in feeders}
            self.required_feeders = {i: None for i in required_feeders}
        else:
            el_arc_feeders = el_arc.get_feeders()
            self.feeders = {i: None for i in el_arc_feeders}
            self.required_feeders = {
                i: None for i in filter(lambda x: el_arc_feeders[x], el_arc_feeders)
            }
            self.logger.info(f"feeders: {self.feeders.keys()}")
            self.logger.info(f"required feeders: {self.required_feeders.keys()}")
            self.logger.info(f"feeder with elarc: {el_arc.feeder}/{el_arc.compartment}")
            self.logger.info(f"connection type: {self.connection_type}")
            self.logger.info(f"arc detection type: {self.arc_detection_type}")

        self.errors = []
        self.messages = []

        self.done = False
        self.missfire = False

        self.data = b""
        self.complete_data = b""

        self.start_time = time()
        self.arc_time = None

        self.save_osc_png = save_osc_png
        self.save_osc_txt = save_osc_txt

    def _read_serial(self) -> bytes:
        return self.serial_port.read_all()

    def start_test(self):
        """The start_test function is used to begin a test."""
        old_data = self.serial_port.read_all()

        if len(old_data) != 0:
            self.logger.warning(f"Old data found: {old_data}")

        # starting sequence
        self.serial_port.write(b"s")
        self.serial_port.write(self.starting_letter.encode())
        self.serial_port.write(self.channel.encode())
        start_data = b""

        # lengh of responce is 8bits exactly
        while len(start_data) < 7:
            data = self._read_serial()
            start_data += data
            self.complete_data += data

        self.logger.info("Start data received")
        # Check if start data is correct
        if (
            start_data[:7]
            != b"s\xaa" + self.starting_letter.encode() + b"\xaa@\x00\x00"
        ):
            self.logger.error(f"Wrong start data: {start_data[:7]}")
            self.logger.finished_with_errors()
            return

        # Remove start data
        self.data = start_data[7:]
        self.logger.info("Test started")

        self._main_loop()

    def _read_data(self):
        data = self._read_serial()
        self.data += data
        self.complete_data += data

    def _split_data(self) -> List[Message]:
        messages = []

        while len(self.data) >= 5:
            bmessage = self.data[:5]
            self.data = self.data[5:]
            messages.append(Message(bmessage))

        return messages

    def _read_osc(self):
        self.serial_port.write(b"o")
        self.data += self.serial_port.read(8002)

        # first two bits are response b"o\xff"
        return self.data[2:]

    def _main_loop(self) -> Tuple[dict, list]:
        while time() - self.start_time < self.test_time:
            self._read_data()

            # if we have less than 5 new bits - we don't have any complete messages
            if len(self.data) < 5:
                continue
            new_messages = self._get_new_messages()

            for message in new_messages:
                self._parse_message(message)

            # Check if all required feeders are open
            if list(self.required_feeders.values()).count(None) == 0:
                self.done = True

        print(self.feeders)
        if self.save_osc_png or self.save_osc_txt:
            self._oscilloscope()

        self.logger.info(f"complete data: {str(self.complete_data)}")
        if self.done and not self.missfire:
            self.logger.finished_successfully()
        else:
            self.logger.warning("Test failed")
            if not self.done:
                self.logger.error("Failed feeders: ")
                for feeder in self.required_feeders:
                    if self.feeders[feeder] is None:
                        self.logger.error(f"--------feeder {feeder}")

            if self.missfire:
                self.logger.warning("Wrong feeders: ")
                for feeder in self.feeders:
                    if (
                        feeder not in self.required_feeders
                        and self.feeders[feeder] != None
                    ):
                        self.logger.warning(f"--------feeder {feeder}")

            self.logger.finished_with_errors()

    def _oscilloscope(self):
        logging.info("Parsing oscilloscope data")
        osc = OscParse(self._read_osc())
        logging.info("oscilloscope data parsed")

        logging.info("Saving oscilloscope data")
        if self.save_osc_txt:
            self.logger.save_osc_txt(
                filename=f"osc save_osc{self.timestamp}.txt", osc=osc
            )

        if self.save_osc_png:
            self.logger.save_osc_png(filename=f"osc {self.timestamp}.png", osc=osc)

    def _get_new_messages(self):
        new_messages = self._split_data()
        self.messages.extend(new_messages)

        return new_messages

    def _parse_message(self, message: Message):
        if message.code == "T":  # response from feeder
            if (
                self.arc_time is None
            ):  # for some reason feeder responded earlier than arc happend
                self.feeders[message.number] = (
                    message.time * TIME_STEP - FILTRATION_TIME
                )
            else:
                self.feeders[message.number] = (
                    message.time * TIME_STEP - self.arc_time - FILTRATION_TIME
                )

            if message.number in self.required_feeders:
                if self.arc_time is None:
                    self.logger.error("feeder reaction before arc")
                    self.required_feeders[message.number] = (
                        message.time * TIME_STEP - FILTRATION_TIME
                    )
                else:
                    self.required_feeders[message.number] = (
                        message.time * TIME_STEP - self.arc_time - FILTRATION_TIME
                    )
                self.logger.info(
                    f"feeder {message.number} time: {round(self.required_feeders[message.number], 4)}"
                )
            else:
                self.logger.error(
                    f"Wrong feeder {message.number} time: {round(message.time, 4)}"
                )
                self.missfire = True
        elif message.code in ["a", "b"]:  # arc generated on channel a or b
            self.arc_time = message.time * TIME_STEP
            self.logger.info(str(message))
        else:
            self.logger.info(str(message))
