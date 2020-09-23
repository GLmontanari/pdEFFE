import sys
from PyQt5.QtCore import QFile, QTextStream
from PyQt5.QtWidgets import QMainWindow, QApplication


# Working code
class MainWindow(QMainWindow):
    def __init__(self):  # qui : , parent=None
        super(MainWindow, self).__init__()  # e qui : parent


def main():
    app = QApplication(sys.argv)

    # stylesheet, path1
    # app_path = os.path.abspath(os.getcwd())
    # style_path = app_path + '/stylesheet.qss'
    # file = QFile(style_path)

    # stylesheet, path2
    # file = QFile('style.qss')

    # file.open(QFile.ReadOnly)
    # stream = QTextStream(file.readAll())
    # app.setStyleSheet(stream.readAll())

    m_window = MainWindow()
    m_window.show()
    app.exec_()


if __name__ == '__main__':
    main()  # mi serve solo per fare la chiamata da shell, dopo l'installazione
