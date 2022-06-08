import sys
import serial
import queue
import time
import random
from enum import IntEnum


from PySide6 import QtWidgets, QtCore, QtSerialPort
from ui_main import Ui_MainWindow


class CommandLevelEnum(IntEnum):
    EMERGENCY = 1
    STATUS = 2
    NORMAL = 3


class FlowWorker(QtCore.QObject):
    send_log = QtCore.Signal(str)
    send_command = QtCore.Signal(str)
    send_percentange = QtCore.Signal(int)

    command_list = []
    current_line = 0
    current_command = ''

    def set_command_list(self, command_list: list):
        self.send_log.emit('set command list')
        self.command_list = command_list

    def do_terminate(self):
        self.command_list = []
        self.current_line = 0
        self.current_command = ''

    def process_response(self, response: bytes):
        compare = response == b'FlowDone\r\n'
        if compare and self.current_line < len(self.command_list):
            self.send_log.emit('next')
            self.start_flow()

    def start_flow(self):
        command = self.command_list[self.current_line]
        self.current_command = command
        self.send_command.emit(command)
        self.current_line += 1



class CommandWorker(QtCore.QObject):
    send_log = QtCore.Signal(str)
    receive_response = QtCore.Signal(bytes)

    command_queue = queue.PriorityQueue()

    serial = None
    running_flow = False

    def open_uart(self, port: str):
        self.serial = QtSerialPort.QSerialPort()
        self.serial.setPortName(port)
        self.serial.setBaudRate(115200)
        result = self.serial.open(QtCore.QIODevice.ReadWrite)
        self.send_log.emit(f'uart open: {result}')
        self.serial.readyRead.connect(self.read_response)

    @QtCore.Slot()
    def read_response(self):
        if self.serial and self.serial.isOpen() and self.serial.canReadLine():
            response = self.serial.readLine()
            # 韌體短時間回傳多筆會沒讀乾淨
            if len(response) > 0:
                self.receive_response.emit(response)
                self.send_log.emit(f'response: {response}')
                self.read_response()

    @QtCore.Slot(str)
    def send_command(self, command: str):
        if self.serial and self.serial.isOpen():
            formatted_command = f'{command}\r\n'.encode('utf8')
            self.serial.write(formatted_command)
            self.send_log.emit(f'sending: {formatted_command}')
        else:
            self.send_log.emit('no serail port')


class MainController(QtWidgets.QMainWindow):

    send_command = QtCore.Signal(str)
    open_uart_connection = QtCore.Signal(str)
    send_terminate = QtCore.Signal()
    send_continue = QtCore.Signal()
    send_suspend = QtCore.Signal()

    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.get_com_ports()

        self.ui.refresh_comports_button.released.connect(self.get_com_ports)
        self.ui.open_comports_button.released.connect(self.open_uart)

        # 正常執行
        self.ui.start_button.released.connect(self.start_flow)
        self.ui.home_button.released.connect(self.send_home_command)

        # 啟動/中斷/暫停/繼續
        self.ui.move_button.released.connect(self.send_move_command)
        self.ui.terminate_button.released.connect(self.send_terminate_command)
        self.ui.suspend_button.released.connect(self.send_suspend_command)
        self.ui.continue_button.released.connect(self.send_continue_command)

        # Command
        self.worker_thread = QtCore.QThread()
        self.worker = CommandWorker()
        self.worker.moveToThread(self.worker_thread)
        self.worker_thread.start()

        self.worker.send_log.connect(self.write_log)

        self.open_uart_connection.connect(self.worker.open_uart)
        self.send_command.connect(self.worker.send_command)

        # Flow
        self.flow_thread = QtCore.QThread()
        self.flow_worker = FlowWorker()
        self.flow_worker.moveToThread(self.flow_thread)

        self.flow_thread.started.connect(self.flow_worker.start_flow)
        self.flow_worker.send_log.connect(self.write_log)
        self.flow_worker.send_command.connect(self.worker.send_command)
        self.worker.receive_response.connect(self.flow_worker.process_response)

    def send_continue_command(self):
        self.send_command.emit('suspend[0]')

    def send_suspend_command(self):
        self.send_command.emit('suspend[1]')

    def send_terminate_command(self):
        self.send_command.emit('suspend[2]')

    def send_move_command(self):
        # command = 'MoveStnX	20	x	x	x	x	x	x	x	x	x	x	x	x	x	x	x'
        command = 'MoveStnX\t20\tx\tx\tx\tx\tx\tx\tx\tx\tx\tx\tx\tx\tx\tx\tx'
        self.send_command.emit(command)

    def send_home_command(self):
        self.send_command.emit('home')

    def open_uart(self):
        port = self.ui.ports_combobox.currentText()
        self.open_uart_connection.emit(port)

    def write_log(self, message: str):
        self.ui.log_list.addItem(message)

    def start_flow(self):
        count = self.ui.command_list.count()
        self.flow_thread.quit()

        command_list = []
        for i in range(count):
            command = self.ui.command_list.item(i).text()
            command_list.append(command)
        self.running_flow = True

        self.flow_worker.do_terminate()
        self.flow_worker.set_command_list(command_list)
        self.flow_thread.start()

    def get_com_ports(self):
        self.ui.ports_combobox.clear()
        self.com_ports = [port.portName()
                          for port in QtSerialPort.QSerialPortInfo().availablePorts()]
        self.ui.ports_combobox.addItems(self.com_ports)


if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)

    window = MainController()
    window.show()
    sys.exit(app.exec())
