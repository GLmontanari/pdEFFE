import sys
import PyPDF2

from PyQt5.QtCore import QFile, QTextStream, QDir, QFileInfo
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QGridLayout
from PyQt5.QtWidgets import QPushButton, QCheckBox, QFileDialog, QMessageBox


class DocPanel(QWidget):  # TODO: sostituire con QtQuick DoubleSlider
    def __init__(self, parent):  # qui
        super(DocPanel, self).__init__(parent)  # e qui mi serve per chiamare il metodo 'load_file'

        d_panel = QWidget(self)
        page_left = QPushButton('<-', self)
        page_right = QPushButton('->', self)
        load_btn = QPushButton('Load PDF', self)
        load_btn.clicked.connect(self.parent().load_file)  # bug

        layout = QGridLayout()
        layout.addWidget(d_panel, 0, 0, 1, 2)
        layout.addWidget(page_left, 1, 0, 1, 1)
        layout.addWidget(page_right, 1, 1, 1, 1)
        layout.addWidget(load_btn, 2, 0, 1, 2)
        self.setLayout(layout)
        self.setMinimumSize(150, 200)


# Working code
class MainWindow(QMainWindow):
    def __init__(self):  # qui : , parent=None
        super(MainWindow, self).__init__()  # e qui : parent

        # Globals
        self.cwd = ''  # memorizza l'ultima cartella aperta
        self.files_list = []

        # Appearance
        self.setWindowTitle("Go pdf!")
        # self.setWindowIcon(QIcon('icons/test-tube.png'))
        self.resize(500, 200)

        container_widget = QWidget()
        self.setCentralWidget(container_widget)

        # Row1
        self.merge_chbox = QCheckBox()
        self.merge_chbox.stateChanged.connect(self.enable_append)

        # Row2
        panel1 = DocPanel(parent=self)  # TODO: sostituire con QtQuick DoubleSlider
        self.panel2 = DocPanel(parent=self)  # TODO: sostituire con QtQuick DoubleSlider
        self.panel2.setEnabled(False)  # all'inizio è disabilitato

        # Row3
        self.act_btn = QPushButton('Do it!')
        self.act_btn.clicked.connect(self.crunch_files)

        # Layout
        layout = QGridLayout(container_widget)

        # Row1
        layout.addWidget(self.merge_chbox, 0, 2, 1, 1)

        # Row2
        layout.addWidget(panel1, 1, 0, 1, 2)
        layout.addWidget(self.panel2, 1, 3, 1, 2)

        # Row3
        layout.addWidget(self.act_btn, 2, 2, 1, 1)
        self.setLayout(layout)

        # self.resize(QGuiApplication.primaryScreen().availableSize() * 3 / 5)

    # SLOTS
    def enable_append(self):
        if self.merge_chbox.isChecked():
            self.panel2.setEnabled(True)  # abilita il caricamento di un secondo file solo se vuoi fare il 'merge'
        else:
            self.panel2.setEnabled(False)

    def load_file(self):
        # devo fare '_' perchè ritorna una tupla
        filename, _ = QFileDialog.getOpenFileName(None, 'Open file', self.cwd, 'Text files (*.pdf)')

        if not all(filename):
            msg_box = QMessageBox()
            msg_box.setText("Error : empty path")
            msg_box.exec()
            return

        # memorizza l'ultima cartella aperta
        self.cwd = QFileInfo(filename).path()  # TODO: più pitonese
        self.files_list.append(filename)  # in pratica non sto occupando memoria perchè non ho ancora caricato il file
        # TODO: impedire di caricare più di 2 file

    def crunch_files(self):
        # se ci sono 2 pdf, fai il 'merge'
        if len(self.files_list) == 2:
            merger = PyPDF2.PdfFileMerger()
            for elem in self.files_list:
                merger.append(PyPDF2.PdfFileReader(open(elem, 'rb')))

        # alla fine salva su disco
        filename, _ = QFileDialog.getSaveFileName(self, "Save merged PDF", "", "pdf files (*.pdf)")
        # TODO: aggiungere controllo
        # TODO: cosa fare quando esiste già un file con lo stesso nome? sovrascrivere?
        merger.write(filename)


def main():
    app = QApplication(sys.argv)

    # app_path = os.path.abspath(os.getcwd())
    # style_path = app_path + '/stylesheet.qss'
    # file = QFile(style_path)

    # file = QFile('style.qss')

    # file.open(QFile.ReadOnly)
    # stream = QTextStream(file.readAll())
    # app.setStyleSheet(stream.readAll())

    m_window = MainWindow()
    m_window.show()
    app.exec_()


if __name__ == '__main__':
    main()  # mi serve solo per fare la chiamata da shell, dopo l'installazione
