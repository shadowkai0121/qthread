import sys
import serial
import queue
import time
import random


from serial.tools import list_ports
from PySide6 import QtWidgets, QtCore
from ui_main import Ui_MainWindow
from enum import IntEnum


class CommandLevelEnum(IntEnum):
    EMERGENCY = 1
    STATUS = 2
    NORMAL = 3


class CommandWorker(QtCore.QThread):
    '''
    負責處裡 command 讀寫的執行緒
    '''
    send_log = QtCore.Signal(str)

    command_queue = queue.PriorityQueue()
    '''
    負責接受介面產生的指令
    由迴圈循序執行每項指令
    '''

    port = None
    serial = None

    waiting_ack = False
    waiting_flow_done = False

    has_emergency_command = False

    def __init__(self):
        super().__init__()

    def set_command(self, command: str):
        self.send_log.emit(f'received command: {command}')
        formatted_command = command + '\r\n'
        self.command_queue.put(
            (CommandLevelEnum.NORMAL, formatted_command.encode('utf8'))
        )

    def continue_flow(self):
        command = 'suspend[0]\r\n'.encode('utf8')
        self.send_log.emit('continue flow')
        self.has_emergency_command = True
        self.command_queue.put((CommandLevelEnum.EMERGENCY, command))

    def suspend_flow(self):
        command = 'suspend[1]\r\n'.encode('utf8')
        self.send_log.emit(f'receive suspend {command}')
        self.has_emergency_command = True
        self.command_queue.put((CommandLevelEnum.EMERGENCY, command))

    def terminate_flow(self):
        command = 'suspend[2]\r\n'.encode('utf8')
        self.send_log.emit(f'receive terminate {command}')
        self.has_emergency_command = True
        # terminate 直接重置 Queue
        self.command_queue = queue.PriorityQueue()
        self.command_queue.put((CommandLevelEnum.EMERGENCY, command))

    def open_uart(self, port):
        self.serial = serial.Serial(port, 115200)
        self.send_log.emit(f'open uart')

    def port_is_close(self):
        return self.serial is None or not self.serial.is_open
    
    def wating_response(self):
        return self.waiting_ack or self.waiting_flow_done

    def process_response(self, response: bytes):
        result = response.decode('utf8').lower()
        if result.find('ack') > -1:
            self.send_log.emit('ack response')
            self.waiting_ack = False
            self.waiting_flow_done = True
        elif result.find('flowdone') > -1:
            self.send_log.emit('flowdone response')
            self.waiting_flow_done = False
        elif result.find('suspend') > -1:
            self.send_log.emit('suspend response')
            self.has_emergency_command = False
        return result

    def run(self):
        while True:
            if self.port_is_close():
                time.sleep(1)
                continue

            if self.wating_response() and not self.has_emergency_command:
                response = self.serial.readline()
                if len(response) > 0:
                    response = self.process_response(response)
                    self.send_log.emit(f'response: {response}')
                continue

            if self.command_queue.empty():
                time.sleep(1)
                continue
            

            priority, command = self.command_queue.get()

            self.send_log.emit(f'current command: {command}')

            self.waiting_ack = True
            self.serial.write(command)
            time.sleep(0.1)




class MainController(QtWidgets.QMainWindow):
    command_worker = CommandWorker()

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
        self.ui.start_button.released.connect(self.start_process)
        self.ui.home_button.released.connect(self.send_home_command)

        # 啟動/中斷/暫停/繼續
        self.ui.move_button.released.connect(self.send_move_command)
        self.ui.terminate_button.released.connect(self.send_terminate_command)
        self.send_terminate.connect(self.command_worker.terminate_flow)
        self.ui.suspend_button.released.connect(self.send_suspend_command)
        self.ui.continue_button.released.connect(self.send_continue_command)
        self.send_suspend.connect(self.command_worker.suspend_flow)
        self.send_continue.connect(self.command_worker.continue_flow)

        self.send_command.connect(self.command_worker.set_command)
        self.open_uart_connection.connect(self.command_worker.open_uart)

        self.command_worker.send_log.connect(self.write_log)
        self.command_worker.start()

    def send_continue_command(self):
        self.send_continue.emit()

    def send_suspend_command(self):
        self.send_suspend.emit()

    def send_terminate_command(self):
        self.send_terminate.emit()

    def send_move_command(self):
        # command = 'MoveStnX	20	x	x	x	x	x	x	x	x	x	x	x	x	x	x	x'
        command = 'MoveStnX\t20\tx\tx\tx\tx\tx\tx\tx\tx\tx\tx\tx\tx\tx\tx\tx'
        self.send_command.emit(command)

    def send_home_command(self):
        self.send_command.emit('home')

    def open_uart(self):
        port = self.ui.ports_combobox.currentText()
        if self.command_worker.isFinished():
            self.command_worker.start()
        self.open_uart_connection.emit(port)

    def write_log(self, message: str):
        self.ui.log_list.addItem(message)

    def start_process(self):
        count = self.ui.command_list.count()

        for i in range(count):
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
