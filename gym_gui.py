# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setStyleSheet("background-color: beige")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(260, 10, 491, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(100, 90, 55, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("white")
        self.label_2.setTextFormat(QtCore.Qt.AutoText)
        self.label_2.setScaledContents(False)
        self.label_2.setWordWrap(False)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(100, 110, 61, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(100, 150, 55, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(80, 180, 81, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(90, 280, 55, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(90, 220, 55, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.lineEditName = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditName.setGeometry(QtCore.QRect(170, 90, 113, 22))
        self.lineEditName.setStyleSheet("background-color: white;")
        self.lineEditName.setObjectName("lineEditName")
        self.squatweightlineedit = QtWidgets.QLineEdit(self.centralwidget)
        self.squatweightlineedit.setGeometry(QtCore.QRect(170, 120, 113, 22))
        self.squatweightlineedit.setStyleSheet("background-color: white;\n"
"")
        self.squatweightlineedit.setObjectName("squatweightlineedit")
        self.benchweightlineedit = QtWidgets.QLineEdit(self.centralwidget)
        self.benchweightlineedit.setGeometry(QtCore.QRect(170, 150, 113, 22))
        self.benchweightlineedit.setStyleSheet("background-color: white;\n"
"")
        self.benchweightlineedit.setObjectName("benchweightlineedit")
        self.deadliftweightlineedit = QtWidgets.QLineEdit(self.centralwidget)
        self.deadliftweightlineedit.setGeometry(QtCore.QRect(170, 180, 113, 22))
        self.deadliftweightlineedit.setStyleSheet("background-color: white;\n"
"")
        self.deadliftweightlineedit.setObjectName("deadliftweightlineedit")
        self.lineEditTotal = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditTotal.setGeometry(QtCore.QRect(170, 280, 113, 22))
        self.lineEditTotal.setStyleSheet("background-color: white;\n"
"")
        self.lineEditTotal.setObjectName("lineEditTotal")
        self.comboBoxunit = QtWidgets.QComboBox(self.centralwidget)
        self.comboBoxunit.setGeometry(QtCore.QRect(170, 220, 69, 22))
        self.comboBoxunit.setStyleSheet("background-color: white;\n"
"")
        self.comboBoxunit.setObjectName("comboBoxunit")
        self.comboBoxunit.addItem("")
        self.comboBoxunit.addItem("")
        self.nextbutton = QtWidgets.QPushButton(self.centralwidget)
        self.nextbutton.setGeometry(QtCore.QRect(430, 70, 141, 32))
        self.nextbutton.setMouseTracking(False)
        self.nextbutton.setStyleSheet("background-color: white;")
        self.nextbutton.setObjectName("nextbutton")
        self.previousbutton = QtWidgets.QPushButton(self.centralwidget)
        self.previousbutton.setGeometry(QtCore.QRect(590, 70, 141, 32))
        self.previousbutton.setStyleSheet("background-color: white;")
        self.previousbutton.setObjectName("previousbutton")
        self.cleardatbtn = QtWidgets.QPushButton(self.centralwidget)
        self.cleardatbtn.setGeometry(QtCore.QRect(430, 110, 141, 32))
        self.cleardatbtn.setStyleSheet("background-color: white;")
        self.cleardatbtn.setObjectName("cleardatbtn")
        self.insertAthletebtn = QtWidgets.QPushButton(self.centralwidget)
        self.insertAthletebtn.setGeometry(QtCore.QRect(590, 110, 141, 32))
        self.insertAthletebtn.setStyleSheet("background-color: white;")
        self.insertAthletebtn.setObjectName("insertAthletebtn")
        self.calctotalbtn = QtWidgets.QPushButton(self.centralwidget)
        self.calctotalbtn.setGeometry(QtCore.QRect(430, 150, 141, 32))
        self.calctotalbtn.setStyleSheet("background-color: white;")
        self.calctotalbtn.setObjectName("calctotalbtn")
        self.incSquatbtn = QtWidgets.QPushButton(self.centralwidget)
        self.incSquatbtn.setGeometry(QtCore.QRect(590, 150, 141, 32))
        self.incSquatbtn.setStyleSheet("background-color: white;")
        self.incSquatbtn.setObjectName("incSquatbtn")
        self.incbenchbtn = QtWidgets.QPushButton(self.centralwidget)
        self.incbenchbtn.setGeometry(QtCore.QRect(430, 190, 141, 32))
        self.incbenchbtn.setStyleSheet("background-color: white;")
        self.incbenchbtn.setObjectName("incbenchbtn")
        self.incdeadliftbtn = QtWidgets.QPushButton(self.centralwidget)
        self.incdeadliftbtn.setGeometry(QtCore.QRect(590, 190, 141, 32))
        self.incdeadliftbtn.setAutoFillBackground(False)
        self.incdeadliftbtn.setStyleSheet("background-color: white;")
        self.incdeadliftbtn.setObjectName("incdeadliftbtn")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(290, 110, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(290, 140, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(290, 176, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.lineEditsquatreps = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditsquatreps.setGeometry(QtCore.QRect(360, 120, 31, 22))
        self.lineEditsquatreps.setStyleSheet("background-color: white;")
        self.lineEditsquatreps.setObjectName("lineEditsquatreps")
        self.lineEditbenchreps = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditbenchreps.setGeometry(QtCore.QRect(360, 150, 31, 22))
        self.lineEditbenchreps.setStyleSheet("background-color: white;")
        self.lineEditbenchreps.setObjectName("lineEditbenchreps")
        self.lineEditdeadliftreps = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditdeadliftreps.setGeometry(QtCore.QRect(360, 180, 31, 22))
        self.lineEditdeadliftreps.setStyleSheet("background-color: white;")
        self.lineEditdeadliftreps.setObjectName("lineEditdeadliftreps")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(40, 330, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(30, 380, 101, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(20, 420, 121, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.lineEditSquatORM = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditSquatORM.setGeometry(QtCore.QRect(170, 340, 113, 22))
        self.lineEditSquatORM.setStyleSheet("background-color: white;\n"
"")
        self.lineEditSquatORM.setObjectName("lineEditSquatORM")
        self.lineEditBenchOrm = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditBenchOrm.setGeometry(QtCore.QRect(170, 380, 113, 22))
        self.lineEditBenchOrm.setStyleSheet("background-color: white;")
        self.lineEditBenchOrm.setObjectName("lineEditBenchOrm")
        self.lineEditDeadliftORM = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditDeadliftORM.setGeometry(QtCore.QRect(170, 420, 113, 22))
        self.lineEditDeadliftORM.setStyleSheet("background-color: white;")
        self.lineEditDeadliftORM.setObjectName("lineEditDeadliftORM")
        self.checkBoxisapowerlifter = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBoxisapowerlifter.setGeometry(QtCore.QRect(170, 250, 141, 20))
        self.checkBoxisapowerlifter.setStyleSheet("")
        self.checkBoxisapowerlifter.setObjectName("checkBoxisapowerlifter")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Gym Management System"))
        self.label_2.setText(_translate("MainWindow", "Name"))
        self.label_3.setText(_translate("MainWindow", "Squat"))
        self.label_4.setText(_translate("MainWindow", "Bench"))
        self.label_5.setText(_translate("MainWindow", "Deadlift"))
        self.label_6.setText(_translate("MainWindow", "Total"))
        self.label_7.setText(_translate("MainWindow", "Units"))
        self.lineEditName.setText(_translate("MainWindow", "jamie"))
        self.squatweightlineedit.setText(_translate("MainWindow", "112"))
        self.benchweightlineedit.setText(_translate("MainWindow", "112"))
        self.deadliftweightlineedit.setText(_translate("MainWindow", "112"))
        self.comboBoxunit.setItemText(0, _translate("MainWindow", "LBS"))
        self.comboBoxunit.setItemText(1, _translate("MainWindow", "KG"))
        self.nextbutton.setText(_translate("MainWindow", "Next"))
        self.previousbutton.setText(_translate("MainWindow", "Previous"))
        self.cleardatbtn.setText(_translate("MainWindow", "Clear Data"))
        self.insertAthletebtn.setText(_translate("MainWindow", "Insert Athlete"))
        self.calctotalbtn.setText(_translate("MainWindow", "Calculate Total"))
        self.incSquatbtn.setText(_translate("MainWindow", "Increment Squat"))
        self.incbenchbtn.setText(_translate("MainWindow", "Increment Bench"))
        self.incdeadliftbtn.setText(_translate("MainWindow", "Increment Deadlift"))
        self.label_8.setText(_translate("MainWindow", "Reps x"))
        self.label_9.setText(_translate("MainWindow", "Reps x"))
        self.label_10.setText(_translate("MainWindow", "Reps x"))
        self.lineEditsquatreps.setText(_translate("MainWindow", "1"))
        self.lineEditbenchreps.setText(_translate("MainWindow", "1"))
        self.lineEditdeadliftreps.setText(_translate("MainWindow", "1"))
        self.label_11.setText(_translate("MainWindow", "Squat ORM"))
        self.label_12.setText(_translate("MainWindow", "Bench ORM"))
        self.label_13.setText(_translate("MainWindow", "Deadlift ORM"))
        self.checkBoxisapowerlifter.setText(_translate("MainWindow", "Is a Powerlifter"))
