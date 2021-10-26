# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tagtool.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets

from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog
from PyQt5.QtGui import QIcon

import pandas as pd

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(423, 348)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(9, 9, 411, 111))
        self.frame.setAutoFillBackground(False)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(10, 180, 411, 70))
        self.textEdit.setObjectName("textEdit")
        self.load_eval = QtWidgets.QPushButton(self.centralwidget)
        self.load_eval.setGeometry(QtCore.QRect(125, 140, 151, 27))
        self.load_eval.setObjectName("load_eval")
        self.KalanSorular = QtWidgets.QLCDNumber(self.centralwidget)
        self.KalanSorular.setGeometry(QtCore.QRect(320, 140, 64, 23))
        self.KalanSorular.setObjectName("KalanSorular")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(20, 20, 127, 95))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.excel_name = QtWidgets.QPushButton(self.widget)
        self.excel_name.setObjectName("excel_name")
        self.verticalLayout.addWidget(self.excel_name)
        self.com_col = QtWidgets.QLineEdit(self.widget)
        self.com_col.setObjectName("com_col")
        self.verticalLayout.addWidget(self.com_col)
        self.com_pn = QtWidgets.QLineEdit(self.widget)
        self.com_pn.setObjectName("com_pn")
        self.verticalLayout.addWidget(self.com_pn)
        self.widget1 = QtWidgets.QWidget(self.centralwidget)
        self.widget1.setGeometry(QtCore.QRect(160, 50, 82, 62))
        self.widget1.setObjectName("widget1")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget1)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.com_load = QtWidgets.QPushButton(self.widget1)
        self.com_load.setObjectName("com_load")
        self.verticalLayout_2.addWidget(self.com_load)
        self.pn_load = QtWidgets.QPushButton(self.widget1)
        self.pn_load.setObjectName("pn_load")
        self.verticalLayout_2.addWidget(self.pn_load)
        self.widget2 = QtWidgets.QWidget(self.centralwidget)
        self.widget2.setGeometry(QtCore.QRect(270, 50, 136, 25))
        self.widget2.setObjectName("widget2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget2)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.PozitifSay = QtWidgets.QLCDNumber(self.widget2)
        self.PozitifSay.setObjectName("PozitifSay")
        self.horizontalLayout.addWidget(self.PozitifSay)
        self.NegatifSay = QtWidgets.QLCDNumber(self.widget2)
        self.NegatifSay.setObjectName("NegatifSay")
        self.horizontalLayout.addWidget(self.NegatifSay)
        self.widget3 = QtWidgets.QWidget(self.centralwidget)
        self.widget3.setGeometry(QtCore.QRect(270, 28, 141, 21))
        self.widget3.setObjectName("widget3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget3)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.widget3)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.horizontalLayout_2.addWidget(self.lineEdit_3)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.widget3)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.horizontalLayout_2.addWidget(self.lineEdit_4)
        self.widget4 = QtWidgets.QWidget(self.centralwidget)
        self.widget4.setGeometry(QtCore.QRect(120, 260, 168, 29))
        self.widget4.setObjectName("widget4")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget4)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.pos_eval = QtWidgets.QPushButton(self.widget4)
        self.pos_eval.setObjectName("pos_eval")
        self.horizontalLayout_3.addWidget(self.pos_eval)
        self.neg_eval = QtWidgets.QPushButton(self.widget4)
        self.neg_eval.setObjectName("neg_eval")
        self.horizontalLayout_3.addWidget(self.neg_eval)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 423, 24))
        self.menubar.setObjectName("menubar")
        self.menuDashboard = QtWidgets.QMenu(self.menubar)
        self.menuDashboard.setObjectName("menuDashboard")
        self.menuAssessment = QtWidgets.QMenu(self.menubar)
        self.menuAssessment.setObjectName("menuAssessment")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuDashboard.menuAction())
        self.menubar.addAction(self.menuAssessment.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.load_eval.setText(_translate("MainWindow", "Değerlendirme Yükle"))
        self.excel_name.setText(_translate("MainWindow", "Excel File"))
        self.com_col.setText(_translate("MainWindow", "Yorum Kolonu Adı"))
        self.com_pn.setText(_translate("MainWindow", "P/N Kolonu Adı"))
        self.com_load.setText(_translate("MainWindow", "Yükle"))
        self.pn_load.setText(_translate("MainWindow", "Yükle"))
        self.lineEdit_3.setText(_translate("MainWindow", "Pozitif"))
        self.lineEdit_4.setText(_translate("MainWindow", "Negatif"))
        self.pos_eval.setText(_translate("MainWindow", "Pozitif"))
        self.neg_eval.setText(_translate("MainWindow", "Negatif"))
        self.menuDashboard.setTitle(_translate("MainWindow", "Dashboard"))
        self.menuAssessment.setTitle(_translate("MainWindow", "Assessment"))
        self.excel_name.clicked.connect(self.pushButton_handler)
        
    def pushButton_handler(self):
        print("Button pressed")
        self.open_dialog_box()
        
    def open_dialog_box(self):
        filename = QFileDialog.getOpenFileName()
        self.path = filename[0]
        print(self.path)
        self.file_open()
        return self.path
    
    def file_open(self):
        self.df_cevaplar = pd.read_excel(self.path)
        return self.df_cevaplar


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
    

