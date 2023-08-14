import sys
from PySide6.QtWidgets import *
from PySide6 import QtGui
from PySide6.QtCore import QTimer, QSize
from uiScripts.ui_Main import Ui_MainWindow

license = """
DyberyPDF Merger
Copyright (C) 2023 DyberyOS Developers

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""

class Window(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        # This function initializes and runs EmuGUI
        try:
            super().__init__(parent)

        except:
            super().__init__()
        
        self.setupUi(self)
        self.connectSignalsSlots()
        self.pdfFilesToMerge = []
        self.pdfmodel = QtGui.QStandardItemModel()
        self.pdfList.setModel(self.pdfmodel)

    def resizeEvent(self, event: QtGui.QResizeEvent):
        super().resizeEvent(event)
        self.centralwidget.resize(event.size())
        self.gridLayoutWidget.resize(QSize(event.size().width() - 19, event.size().height() - 66))
        

    def closeApp(self):
        self.close()

    def aboutDyberyPDFM(self):
        QMessageBox.about(self, "About DyberyPDF Merger", license)

    def aboutQt(self):
        QMessageBox.aboutQt(self)

    def addFileDialogs(self):
        filenames, filter = QFileDialog.getOpenFileNames(parent=self, caption='Select PDF files', dir='.', filter='PDF document (*.pdf);;All files (*.*)')

        if filenames:
            for filename in filenames:
                item = QtGui.QStandardItem(filename)
                self.pdfmodel.appendRow(item)

    def connectSignalsSlots(self):
        self.actionClose.triggered.connect(self.closeApp)
        self.actionAbout_DyberyPDF_Merger.triggered.connect(self.aboutDyberyPDFM)
        self.actionAbout_Qt.triggered.connect(self.aboutQt)
        self.addFileBtn.clicked.connect(self.addFileDialogs)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec())