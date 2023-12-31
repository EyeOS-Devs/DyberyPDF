import sys
from PySide6.QtWidgets import *
from PySide6 import QtGui
from PySide6.QtCore import *
from uiScripts.ui_Main import Ui_MainWindow
import pypdf
import os

dyberyPdfMergerVer = "0.0.1"

license = f"""
DyberyPDF Merger, Version {dyberyPdfMergerVer}
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

    def resizeEvent(self, event: QtGui.QResizeEvent):
        super().resizeEvent(event)
        self.centralwidget.resize(event.size())
        self.gridLayoutWidget.resize(QSize(event.size().width() - 19, event.size().height() - 66))
        
    def mergePDFs(self):
        filesToMergeR = [self.pdfList.model().index(i, 0) for i in range(self.pdfList.model().rowCount())]
        #filesToMergeR = self.pdfList.items()
        print(filesToMergeR)
        filesToMerge = []

        for file in filesToMergeR:
            filesToMerge.append(file.data())

        print(filesToMerge)
        pdfMerger = pypdf.PdfMerger(strict=False)

        for file in filesToMerge:
            bookmark_name = os.path.splitext(os.path.basename(file))[0]
            pdfMerger.append(fileobj=open(file, "rb"), import_outline=False, outline_item=bookmark_name)

        filename, filter = QFileDialog.getSaveFileName(parent=self, caption="Save merged PDF file", dir=".", filter="PDF document (*.pdf);;All files (*.*)")

        if filename:
            pdfMerger.write(fileobj=open(filename, "wb+"))
            pdfMerger.close()

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
                self.pdfList.addItem(filename)

    def removeSelectedFiles(self):
        self.pdfList.takeItem(self.pdfList.currentIndex().row())

    def connectSignalsSlots(self):
        self.actionClose.triggered.connect(self.closeApp)
        self.actionAbout_DyberyPDF_Merger.triggered.connect(self.aboutDyberyPDFM)
        self.actionAbout_Qt.triggered.connect(self.aboutQt)
        self.addFileBtn.clicked.connect(self.addFileDialogs)
        self.mergeBtn.clicked.connect(self.mergePDFs)
        self.pdfList.setDragDropMode(QAbstractItemView.InternalMove)
        self.removeFileBtn.clicked.connect(self.removeSelectedFiles)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec())