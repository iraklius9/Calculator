import math

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QTimer


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")

        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName("stackedWidget")

        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")

        self.gridLayout = QtWidgets.QGridLayout(self.page)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 43, QtWidgets.QSizePolicy.Minimum,
                                           QtWidgets.QSizePolicy.MinimumExpanding)
        self.gridLayout.addItem(spacerItem, 2, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(294, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 3, 0, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 44, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem2, 9, 1, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.gridLayout.addItem(spacerItem3, 6, 1, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.gridLayout.addItem(spacerItem4, 8, 1, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(293, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem5, 3, 2, 1, 1)

        self.wre = QtWidgets.QRadioButton(self.page)
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(12)
        self.wre.setFont(font)
        self.wre.setObjectName("wre")

        self.buttonGroup = QtWidgets.QButtonGroup(MainWindow)
        self.buttonGroup.setObjectName("buttonGroup")
        self.buttonGroup.addButton(self.wre)

        self.gridLayout.addWidget(self.wre, 3, 1, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(293, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem6, 1, 2, 1, 1)

        self.otxkutxedi = QtWidgets.QRadioButton(self.page)
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(12)
        self.otxkutxedi.setFont(font)
        self.otxkutxedi.setObjectName("otxkutxedi")
        self.buttonGroup.addButton(self.otxkutxedi)

        self.gridLayout.addWidget(self.otxkutxedi, 7, 1, 1, 1)
        spacerItem7 = QtWidgets.QSpacerItem(20, 44, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem7, 0, 1, 1, 1)
        spacerItem8 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.gridLayout.addItem(spacerItem8, 4, 1, 1, 1)

        self.samkutxedi = QtWidgets.QRadioButton(self.page)
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(12)
        self.samkutxedi.setFont(font)
        self.samkutxedi.setObjectName("samkutxedi")
        self.buttonGroup.addButton(self.samkutxedi)

        self.gridLayout.addWidget(self.samkutxedi, 5, 1, 1, 1)
        spacerItem9 = QtWidgets.QSpacerItem(294, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem9, 1, 0, 1, 1)
        spacerItem10 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem10, 11, 1, 1, 1)

        self.choose = QtWidgets.QPushButton(self.page)

        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.choose.sizePolicy().hasHeightForWidth())
        self.choose.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(12)
        self.choose.setFont(font)
        self.choose.setObjectName("choose")
        self.gridLayout.addWidget(self.choose, 10, 1, 1, 1)

        self.satauri = QtWidgets.QLabel(self.page)
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        self.satauri.setFont(font)
        self.satauri.setObjectName("satauri")
        self.gridLayout.addWidget(self.satauri, 1, 1, 1, 1)

        self.stackedWidget.addWidget(self.page)
        self.wre_page = QtWidgets.QWidget()
        self.wre_page.setObjectName("wre_page")

        self.enter_radius = QtWidgets.QLineEdit(self.wre_page)
        self.enter_radius.setGeometry(QtCore.QRect(170, 170, 221, 41))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(12)
        self.enter_radius.setFont(font)
        self.enter_radius.setObjectName("enter_radius")

        self.wre_gamotvla = QtWidgets.QPushButton(self.wre_page)
        self.wre_gamotvla.setGeometry(QtCore.QRect(430, 170, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(12)
        self.wre_gamotvla.setFont(font)
        self.wre_gamotvla.setObjectName("wre_gamotvla")
        self.wre_gamotvla.clicked.connect(self.wre2pr)
        self.wre_gamotvla.clicked.connect(self.wre2prr)

        self.label1 = QtWidgets.QLabel(self.wre_page)
        self.label1.setText(
            "                                                                                                                     ")
        self.label1.setGeometry(QtCore.QRect(250, 50, 150, 41))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(12)
        self.label1.setFont(font)
        self.label1.adjustSize()

        self.wre_sigrdze = QtWidgets.QLabel(self.wre_page)
        self.wre_sigrdze.setGeometry(QtCore.QRect(180, 330, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(12)
        self.wre_sigrdze.setFont(font)
        self.wre_sigrdze.setObjectName("wre_sigrdze")

        self.wre_fartobi = QtWidgets.QLabel(self.wre_page)
        self.wre_fartobi.setGeometry(QtCore.QRect(180, 390, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(12)
        self.wre_fartobi.setFont(font)
        self.wre_fartobi.setObjectName("wre_fartobi")

        self.wre_fartobi_answer = QtWidgets.QLCDNumber(self.wre_page)
        self.wre_fartobi_answer.setGeometry(QtCore.QRect(320, 390, 250, 31))
        self.wre_fartobi_answer.setObjectName("wre_fartobi_answer")

        self.wre_sigrdze_answer = QtWidgets.QLCDNumber(self.wre_page)
        self.wre_sigrdze_answer.setGeometry(QtCore.QRect(320, 330, 250, 31))
        self.wre_sigrdze_answer.setObjectName("wre_sigrdze_answer")

        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        self.wre_fartobi_answer.setSizePolicy(sizePolicy)
        self.wre_sigrdze_answer.setSizePolicy(sizePolicy)

        self.back_wre = QtWidgets.QPushButton(self.wre_page)
        self.back_wre.setGeometry(QtCore.QRect(0, 0, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(12)
        self.back_wre.setFont(font)
        self.back_wre.setObjectName("back_wre")

        self.stackedWidget.addWidget(self.wre_page)
        self.samkutxedi_page = QtWidgets.QWidget()
        self.samkutxedi_page.setObjectName("samkutxedi_page")

        self.back_samkutxedi = QtWidgets.QPushButton(self.samkutxedi_page)
        self.back_samkutxedi.setGeometry(QtCore.QRect(0, 0, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(12)
        self.back_samkutxedi.setFont(font)
        self.back_samkutxedi.setObjectName("back_samkutxedi")

        self.label = QtWidgets.QLabel(self.samkutxedi_page)
        self.label.setText("                                                                                                                                                           ")

        self.label.setGeometry(QtCore.QRect(105, 80, 150, 41))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.adjustSize()

        self.splitter_4 = QtWidgets.QSplitter(self.samkutxedi_page)
        self.splitter_4.setGeometry(QtCore.QRect(110, 170, 311, 131))
        self.splitter_4.setOrientation(QtCore.Qt.Vertical)
        self.splitter_4.setObjectName("splitter_4")
        self.splitter = QtWidgets.QSplitter(self.splitter_4)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.A = QtWidgets.QLabel(self.splitter)
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(12)

        self.A.setFont(font)
        self.A.setObjectName("A")
        self.A_input = QtWidgets.QLineEdit(self.splitter)
        self.A_input.setObjectName("A_input")
        self.splitter_2 = QtWidgets.QSplitter(self.splitter_4)
        self.splitter_2.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_2.setObjectName("splitter_2")
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(12)
        self.A_input.setFont(font)
        self.A_input.adjustSize()

        self.B = QtWidgets.QLabel(self.splitter_2)
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(12)
        self.B.setFont(font)
        self.B.setObjectName("B")
        self.B_input = QtWidgets.QLineEdit(self.splitter_2)
        self.B_input.setObjectName("B_input")
        self.splitter_3 = QtWidgets.QSplitter(self.splitter_4)
        self.splitter_3.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_3.setObjectName("splitter_3")
        self.B_input.setFont(font)
        self.B_input.adjustSize()

        self.C = QtWidgets.QLabel(self.splitter_3)
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(12)
        self.C.setFont(font)
        self.C.setObjectName("C")
        self.C_input = QtWidgets.QLineEdit(self.splitter_3)
        self.C_input.setObjectName("C_input")
        self.C_input.setFont(font)
        self.C_input.adjustSize()

        self.samkutxedi_gamotvla = QtWidgets.QPushButton(self.samkutxedi_page)
        self.samkutxedi_gamotvla.setGeometry(QtCore.QRect(514, 180, 171, 101))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.samkutxedi_gamotvla.setFont(font)
        self.samkutxedi_gamotvla.setObjectName("samkutxedi_gamotvla")
        self.samkutxedi_gamotvla.clicked.connect(self.samkutxedi_area)

        self.samkutxedi_answer = QtWidgets.QLCDNumber(self.samkutxedi_page)
        self.samkutxedi_answer.setGeometry(QtCore.QRect(510, 310, 171, 101))
        self.samkutxedi_answer.setObjectName("samkutxedi_answer")

        self.stackedWidget.addWidget(self.samkutxedi_page)
        self.otxkutxedi_page = QtWidgets.QWidget()
        self.otxkutxedi_page.setObjectName("otxkutxedi_page")

        self.label2 = QtWidgets.QLabel(self.otxkutxedi_page)
        self.label2.setText(
            "                                                                                                                                      ")
        self.label2.setGeometry(QtCore.QRect(160, 370, 150, 41))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(12)
        self.label2.setFont(font)
        self.label2.adjustSize()

        self.back_otxkutxedi = QtWidgets.QPushButton(self.otxkutxedi_page)
        self.back_otxkutxedi.setGeometry(QtCore.QRect(0, 0, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.back_otxkutxedi.setFont(font)
        self.back_otxkutxedi.setObjectName("back_otxkutxedi")

        self.otxkutxedi_gamotvla = QtWidgets.QPushButton(self.otxkutxedi_page)
        self.otxkutxedi_gamotvla.setGeometry(QtCore.QRect(534, 150, 171, 91))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.otxkutxedi_gamotvla.setFont(font)
        self.otxkutxedi_gamotvla.setObjectName("otxkutxedi_gamotvla")
        self.otxkutxedi_gamotvla.clicked.connect(self.otxkutxedi_area)

        self.otxkutxedi_sigrdze = QtWidgets.QLabel(self.otxkutxedi_page)
        self.otxkutxedi_sigrdze.setGeometry(QtCore.QRect(170, 150, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.otxkutxedi_sigrdze.setFont(font)
        self.otxkutxedi_sigrdze.setObjectName("otxkutxedi_sigrdze")

        self.otxkutxedi_sigane = QtWidgets.QLabel(self.otxkutxedi_page)
        self.otxkutxedi_sigane.setGeometry(QtCore.QRect(170, 200, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.otxkutxedi_sigane.setFont(font)
        self.otxkutxedi_sigane.setObjectName("otxkutxedi_sigane")

        self.otxkutxedi_sigrdz_input = QtWidgets.QLineEdit(self.otxkutxedi_page)
        self.otxkutxedi_sigrdz_input.setGeometry(QtCore.QRect(302, 150, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.otxkutxedi_sigrdz_input.setFont(font)
        self.otxkutxedi_sigrdz_input.setObjectName("otxkutxedi_sigrdz_input")

        self.otxkutxedi_sigane_input = QtWidgets.QLineEdit(self.otxkutxedi_page)
        self.otxkutxedi_sigane_input.setGeometry(QtCore.QRect(302, 200, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.otxkutxedi_sigane_input.setFont(font)
        self.otxkutxedi_sigane_input.setObjectName("otxkutxedi_sigane_input")

        self.otxkutxedi_answer = QtWidgets.QLCDNumber(self.otxkutxedi_page)
        self.otxkutxedi_answer.setGeometry(QtCore.QRect(543, 310, 181, 41))
        self.otxkutxedi_answer.setObjectName("otxkutxedi_answer")

        self.stackedWidget.addWidget(self.otxkutxedi_page)
        self.gridLayout_2.addWidget(self.stackedWidget, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(3)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # self.wre_sigrdze_answer.setStyleSheet(
        #     "QLCDNumber { color: #007bff; background-color: #f8f9fa; border: 2px solid #007bff; border-radius: 5px; font-size: 20px; font-weight: bold; }")
        # self.wre_fartobi_answer.setStyleSheet(
        #     "QLCDNumber { color: #007bff; background-color: #f8f9fa; border: 2px solid #007bff; border-radius: 5px; font-size: 20px; font-weight: bold; }")
        # self.samkutxedi_answer.setStyleSheet(
        #     "QLCDNumber { color: #007bff; background-color: #f8f9fa; border: 2px solid #007bff; border-radius: 5px; font-size: 20px; font-weight: bold; }")
        # self.otxkutxedi_answer.setStyleSheet(
        #     "QLCDNumber { color: #007bff; background-color: #f8f9fa; border: 2px solid #007bff; border-radius: 5px; font-size: 20px; font-weight: bold; }")

        self.stackedWidget.setCurrentWidget(self.page)
        self.choose.clicked.connect(self.select_shape)
        self.back_wre.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page))
        self.back_samkutxedi.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page))
        self.back_otxkutxedi.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page))
        self.stackedWidget.currentChanged.connect(self.clear_all_fields)
        self.wre_gamotvla.clicked.connect(self.clear_error_message)
        self.samkutxedi_gamotvla.clicked.connect(self.clear_error_message)
        self.otxkutxedi_gamotvla.clicked.connect(self.clear_error_message)


    def select_shape(self):
        shape_name = self.buttonGroup.checkedButton().objectName()
        self.stackedWidget.setCurrentWidget(
            getattr(self, f'{shape_name}_page', self.page)
        )

    import math

    def wre2pr(self):
        try:
            r = int(self.enter_radius.text())
            if r > 0:
                ans = 2 * math.pi * r
                self.wre_sigrdze_answer.display(ans)
            else:
                raise ValueError("Radius must be greater than 0")
        except ValueError:
            self.label1.setText("ERROR: Invalid input or radius must be greater than 0")

    def wre2prr(self):
        try:
            r = int(self.enter_radius.text())
            if r > 0:
                ans = math.pi * r ** 2
                self.wre_fartobi_answer.display(ans)
            else:
                raise ValueError("Radius must be greater than 0")
        except ValueError:
            self.label1.setText("ERROR: Invalid input or radius must be greater than 0")

    def samkutxedi_area(self):
        try:
            a = int(self.A_input.text())
            b = int(self.B_input.text())
            c = int(self.C_input.text())
            if a + b > c and a + c > b and b + c > a:
                s = (a + b + c) / 2
                area = math.sqrt(s * (s - a) * (s - b) * (s - c))
                self.samkutxedi_answer.display(area)
            else:
                raise ValueError("Invalid triangle sides")
        except ValueError:
            self.label.setText("ERROR: Invalid input or triangle inequality not satisfied")

    def otxkutxedi_area(self):
        try:
            x = int(self.otxkutxedi_sigrdz_input.text())
            y = int(self.otxkutxedi_sigane_input.text())
            if x > 0 and y > 0:
                ans = x * y
                self.otxkutxedi_answer.display(ans)
            else:
                raise ValueError("Sides must be greater than 0")
        except ValueError:
            self.label2.setText("ERROR: Invalid input or sides must be greater than 0")

    def clear_all_fields(self):
        self.label1.clear()
        self.label.clear()
        self.label2.clear()
        self.wre_sigrdze_answer.display(0)
        self.wre_fartobi_answer.display(0)
        self.samkutxedi_answer.display(0)
        self.otxkutxedi_answer.display(0)
        self.label1.setText("")
        self.label.setText("")
        self.label2.setText("")
        self.enter_radius.clear()
        self.A_input.clear()
        self.B_input.clear()
        self.C_input.clear()
        self.otxkutxedi_sigrdz_input.clear()
        self.otxkutxedi_sigane_input.clear()

    def clear_error_message(self):
        if self.label.text().strip():
            QtCore.QTimer.singleShot(3000, lambda: self.label.clear())
        if self.label1.text().strip():
            QtCore.QTimer.singleShot(3000, lambda: self.label1.clear())
        if self.label2.text().strip():
            QtCore.QTimer.singleShot(3000, lambda: self.label2.clear())

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.wre.setText(_translate("MainWindow", "წრეწირი"))
        self.otxkutxedi.setText(_translate("MainWindow", "ოთხკუთხედი"))
        self.samkutxedi.setText(_translate("MainWindow", "სამკუთხედი"))
        self.choose.setText(_translate("MainWindow", "არჩევა"))
        self.satauri.setText(_translate("MainWindow", "კალკულატორი"))
        self.enter_radius.setPlaceholderText(_translate("MainWindow", "ENTER RADIOUS"))
        self.wre_gamotvla.setText(_translate("MainWindow", "გამოთვლა"))
        self.wre_sigrdze.setText(_translate("MainWindow", "სიგრძე"))
        self.wre_fartobi.setText(_translate("MainWindow", "ფართობი"))
        self.back_wre.setText(_translate("MainWindow", "უკან"))
        self.back_samkutxedi.setText(_translate("MainWindow", "უკან"))
        self.A.setText(_translate("MainWindow", "გვერდი 1"))
        self.B.setText(_translate("MainWindow", "გვერდი 2"))
        self.C.setText(_translate("MainWindow", "გვერდი 3"))
        self.samkutxedi_gamotvla.setText(_translate("MainWindow", "გამოთვლა"))
        self.back_otxkutxedi.setText(_translate("MainWindow", "უკან"))
        self.otxkutxedi_gamotvla.setText(_translate("MainWindow", "გამოთვლა"))
        self.otxkutxedi_sigrdze.setText(_translate("MainWindow", "სიგრძე"))
        self.otxkutxedi_sigane.setText(_translate("MainWindow", "სიგანე"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)

    lcd_widgets = [
        ui.wre_sigrdze_answer,
        ui.wre_fartobi_answer,
        ui.samkutxedi_answer,
        ui.otxkutxedi_answer
    ]
    for lcd_widget in lcd_widgets:
        lcd_widget.setDigitCount(18)
        font = lcd_widget.font()
        font.setPointSize(20)
        lcd_widget.setFont(font)
        lcd_widget.setStyleSheet(
            "QLCDNumber { color: #007bff; background-color: #f8f9fa; border: 2px solid #007bff; border-radius: 5px; font-size: 20px; font-weight: bold; }")

    ui.samkutxedi_answer.setDigitCount(18)
    font = ui.samkutxedi_answer.font()
    font.setPointSize(20)
    ui.samkutxedi_answer.setFont(font)
    ui.samkutxedi_answer.setStyleSheet(
        "QLCDNumber { color: #007bff; background-color: #f8f9fa; border: 2px solid #007bff; border-radius: 5px; font-size: 20px; font-weight: bold; }")

    output_labels = [ui.label1, ui.label, ui.label2]
    for label in output_labels:
        font = label.font()
        font.setPointSize(14)
        label.setFont(font)
        label.setStyleSheet("color: blue")

    MainWindow.show()
    sys.exit(app.exec_())