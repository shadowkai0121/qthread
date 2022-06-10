from concurrent.futures import thread
from tokenize import Single
from PySide6 import QtWidgets
from PySide6.QtCore import QThread, QThreadPool, QRunnable, QObject, QTimer, Signal, Slot
import threading
import time
import random

# Runnable 沒辦法靠 slot 接收其他訊號?
# Slot 不管在 QRunnable 或者 QObject 都會變成在 MainThread 執行

def current_thread():
    return f'thread[{threading.current_thread().name}][{threading.get_ident()}]: '

class WorkerSlot(QObject):
    def __init__(self, worker):
        super().__init__()
        self.worker = worker

    @Slot()
    def do_event(self):
        print(current_thread() + 'receive event', flush=True)
        QThreadPool.globalInstance().start(self.worker)
        

class WorkerSignal(QObject):
    finished = Signal()

class Worker(QRunnable):
    def __init__(self):
        super().__init__()
        self.signal = WorkerSignal()
        self.slot = WorkerSlot(self)
    # @Slot()
    # def do_event(self):
    #     print(current_thread() + 'receive event', flush=True)
    #     self.run()
    @Slot()
    def run(self):
        print(current_thread() + 'work start', flush=True)
        time.sleep(random.randint(1, 3))
        print(current_thread() + 'work done', flush=True)
        self.signal.finished.emit()


class Window(QtWidgets.QWidget):
    do_event = Signal()
    def __init__(self):
        super().__init__()
        vbox = QtWidgets.QVBoxLayout()
        self.main_thread_label = QtWidgets.QLabel(
            f'Main Thread: {current_thread()}')

        button = QtWidgets.QPushButton('Add Thread')
        button.released.connect(self.add_thread)

        event_button = QtWidgets.QPushButton('Random Event')
        event_button.released.connect(self.random_event)

        self.total_label = QtWidgets.QLabel(
            f'current active thread: {threading.activeCount()}')
        vbox.addWidget(self.main_thread_label)
        vbox.addWidget(button)
        vbox.addWidget(self.total_label)
        vbox.addWidget(event_button)

        self.setLayout(vbox)


        self.active_count_timer = QTimer()
        self.active_count_timer.timeout.connect(self.active_thread_count)
        self.active_count_timer.start(1000)

        self.worker = Worker()
        # worker 會在 run 結束後直接被刪除
        self.worker.setAutoDelete(False)
        self.do_event.connect(self.worker.do_event)
        QThreadPool.globalInstance().start(self.worker)

        QThreadPool.globalInstance().setExpiryTimeout(1000)
    def log(self):
        print('123', flush=True)

    def random_event(self):
        self.do_event.emit()

    def active_thread_count(self):
        # print(f'timer thread: {threading.current_thread().getName()} {threading.get_ident()}', flush=True)
        self.total_label.setText(f'current active thread: {threading.activeCount()}')

    def add_thread(self):
        worker = Worker()
        worker.signal.finished.connect(self.log)
        self.do_event.connect(worker.slot.do_event)
        QThreadPool.globalInstance().start(worker)


app = QtWidgets.QApplication()
window = Window()
window.show()

app.exec()
