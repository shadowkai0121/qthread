from concurrent.futures import thread
from PySide6 import QtWidgets
from PySide6.QtCore import QThread, QThreadPool, QObject, QTimer, Signal
import threading
import time, random

# print(QThread.idealThreadCount()) # 取得當前硬體最佳的執行緒數量

class Worker(QObject):
    work = ''
    def do_work(self, work):
        print(f'thread[{threading.current_thread().name}]: {threading.get_ident()} do work', flush=True)
        self.work = work
        self.run()
    def run(self):
        print(f'thread[{threading.current_thread().name}]: {threading.get_ident()} actived', flush=True)
        # time.sleep(random.randint(1, 3))
        # self.run()


class Window(QtWidgets.QWidget):
    do_work = Signal(str)
    worker_list = []
    thread_list = []
    
    def __init__(self):
        super().__init__()
        vbox = QtWidgets.QVBoxLayout()
        self.main_thread_label = QtWidgets.QLabel(f'Main Thread: {threading.current_thread().getName()} {threading.get_ident()}')

        button = QtWidgets.QPushButton('Add Thread')
        button.released.connect(self.add_thread)

        event_button = QtWidgets.QPushButton('Random Event')
        event_button.released.connect(self.random_event)

        self.total_label = QtWidgets.QLabel(f'current active thread: {threading.activeCount()}')
        vbox.addWidget(self.main_thread_label)
        vbox.addWidget(button)
        vbox.addWidget(self.total_label)
        vbox.addWidget(event_button)

        self.setLayout(vbox)

        # Timer 實際上會在 main thread 執行
        self.active_count_timer = QTimer()
        self.active_count_timer.timeout.connect(self.active_thread_count)
        self.active_count_timer.start(1000)
    def random_event(self):
        # print('event', flush=True)
        # 在主執行緒執行
        # total = len(self.worker_list)
        # 在主執行緒執行會沒有效果
        # self.worker_list[random.randint(0, total - 1)].do_work('event')

        # 使用 signal-slot 才會進入 thread 執行
        self.do_work.emit('event')


    def active_thread_count(self):
        # print(f'timer thread: {threading.current_thread().getName()} {threading.get_ident()}', flush=True)
        self.total_label.setText(f'current active thread: {threading.activeCount()}')

    def add_thread(self):
        index = len(self.thread_list)
        # Worker 與 Thread 都必須有參照才能執行
        worker = Worker()
        self.worker_list.append(worker)
        self.thread_list.append(QThread())

        self.do_work.connect(worker.do_work)
        
        self.thread_list[index].started.connect(self.worker_list[index].run)

        self.worker_list[index].moveToThread(self.thread_list[index])

        self.thread_list[index].start()
       


app = QtWidgets.QApplication()
window = Window()
window.show()

app.exec()