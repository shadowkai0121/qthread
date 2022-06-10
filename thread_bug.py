from PySide6.QtWidgets import QApplication, QMainWindow, QWidget
from PySide6.QtCore import QThread, QObject
import sys, time

class Worker(QObject):
    def start(self):
        print(time.time(), flush=True)
        QThread.sleep(5)

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.worker = Worker()
        self.my_thread = QThread()
        self.worker.moveToThread(self.my_thread)
        self.my_thread.started.connect(self.worker.start)
        self.my_thread.finished.connect(self.thread_finished)
        self.my_thread.start()
    
    def thread_finished(self):
        print('123', flush=True)
    def closeEvent(self, event):
        # 確保 thread 任務執行完成後才退出
        self.my_thread.quit()
        self.my_thread.wait()
        super().closeEvent(event)

def log():
    print('123', flush=True)
app = QApplication()
window = Window()

window.show()

sys.exit(app.exec())


