import sys
import serial
import queue
import time
import random

from serial.tools import list_ports
from PySide6 import QtWidgets, QtCore
from ui_main import Ui_MainWindow


class CommandWorker(QtCore.QThread):
    '''
    負責處裡指令的發送與讀寫的執行緒
    '''
    send_logger = QtCore.Signal(str)
    received = QtCore.Signal()
    finished = QtCore.Signal()

    command_queue = queue.Queue()
    '''
    負責接受介面產生的指令
    由迴圈循序執行每項指令
    '''


    port = None
    serial = None

    def __init__(self):
        super().__init__()

    def set_command(self, command: str):
        '''
        Slot
        接收由 GUI 產生的指令 Signal
        '''
        command = f'{command}\r\n'.encode("utf8")
        self.send_logger.emit(f'received command: {command}')
        self.command_queue.put(command)

    def open_uart(self, port):
        self.serial = serial.Serial(port, 115200)
        self.send_logger.emit(f'open uart: {self.serial.is_open}')

    def run(self):
        while True:
            if not self.serial or not self.serial.is_open or self.command_queue.empty():
                continue

            command = self.command_queue.get()

            self.command_queue.task_done()

            self.send_logger.emit(f'sending command: {command}')

            start_time = time.time()
            self.serial.write(command)

            response = None 

            # 部分指令的結束訊號為 b'FlowDone\r\n'
            # 通過判斷結束訊號決定是否有未讀取的韌體回傳
            while response != b'FlowDone\r\n':
                response = self.serial.readline()
                self.send_logger.emit(f'response: {response}')

                # 放不放好像都不影響但是有的文章建議要 sleep
                time.sleep(5)
            
            self.send_logger.emit(f'time: {time.time() - start_time}')
        self.finished.emit()
        self.exec()


class MainController(QtWidgets.QMainWindow):
    command_worker = CommandWorker()
    send_command = QtCore.Signal(str)
    open_uart_connection = QtCore.Signal(str)

    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.get_com_ports()

        self.ui.refresh_comports_button.released.connect(self.get_com_ports)
        self.ui.start_button.released.connect(self.start_process)
        self.ui.open_comports_button.released.connect(self.open_uart)
        self.ui.home_button.released.connect(self.send_home_command)

        self.send_command.connect(self.command_worker.set_command)
        self.open_uart_connection.connect(self.command_worker.open_uart)

        self.command_worker.send_logger.connect(self.write_log)
        self.command_worker.start()

    def send_home_command(self):
        self.ui.log_list.addItem('click home button')
        self.send_command.emit('home')

    def open_uart(self):
        port = self.ui.ports_combobox.currentText()
        self.open_uart_connection.emit(port)

    def write_log(self, message: str):
        self.ui.log_list.addItem(message)

    def start_process(self):
        self.write_log('click start')
        count = self.ui.command_list.count()

        for i in range(count):
            time.sleep(1)
            self.ui.command_list.setCurrentRow(i)
            command = self.ui.command_list.currentItem().text()
            self.send_command.emit(command)

    def get_com_ports(self):
        self.ui.ports_combobox.clear()
        self.com_ports = [port.name for port in list_ports.comports()]
        self.ui.ports_combobox.addItems(self.com_ports)


if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)

    window = MainController()
    window.show()
    sys.exit(app.exec())