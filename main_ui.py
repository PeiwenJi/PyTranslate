# pyTranslate PeiwenJi 2021.4.20
# Translate DNA sequence to protein and display results to users.
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pyTranslate.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!
import sys
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_pyTranslate(object):
    def setupUi(self, pyTranslate):
        pyTranslate.setObjectName("pyTranslate")
        pyTranslate.resize(801, 600)
        self.centralwidget = QtWidgets.QWidget(pyTranslate)
        self.centralwidget.setObjectName("centralwidget")
        self.lblTitle = QtWidgets.QLabel(self.centralwidget)
        self.lblTitle.setGeometry(QtCore.QRect(240, 30, 321, 111))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(28)
        self.lblTitle.setFont(font)
        self.lblTitle.setObjectName("lblTitle")
        self.btClear = QtWidgets.QPushButton(self.centralwidget)
        self.btClear.setGeometry(QtCore.QRect(620, 300, 112, 34))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(13)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.btClear.setFont(font)
        self.btClear.setObjectName("btClear")
        self.btSubmit = QtWidgets.QPushButton(self.centralwidget)
        self.btSubmit.setGeometry(QtCore.QRect(320, 450, 121, 41))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(14)
        self.btSubmit.setFont(font)
        self.btSubmit.setObjectName("btSubmit")
        self.lblAuthor = QtWidgets.QLabel(self.centralwidget)
        self.lblAuthor.setGeometry(QtCore.QRect(240, 540, 291, 31))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(8)
        font.setItalic(True)
        self.lblAuthor.setFont(font)
        self.lblAuthor.setProperty("color", QtGui.QColor(141, 141, 141))
        self.lblAuthor.setObjectName("lblAuthor")
        self.lblNote = QtWidgets.QLabel(self.centralwidget)
        self.lblNote.setGeometry(QtCore.QRect(70, 180, 671, 31))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(10)
        font.setUnderline(True)
        self.lblNote.setFont(font)
        self.lblNote.setTextFormat(QtCore.Qt.AutoText)
        self.lblNote.setObjectName("lblNote")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setGeometry(QtCore.QRect(70, 226, 481, 181))
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        self.plainTextEdit.setFont(font)
        self.plainTextEdit.setObjectName("plainTextEdit")
        pyTranslate.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(pyTranslate)
        self.statusbar.setObjectName("statusbar")
        pyTranslate.setStatusBar(self.statusbar)

        self.retranslateUi(pyTranslate)
        self.btClear.clicked.connect(self.plainTextEdit.clear)
        QtCore.QMetaObject.connectSlotsByName(pyTranslate)

    def retranslateUi(self, pyTranslate):
        _translate = QtCore.QCoreApplication.translate
        pyTranslate.setWindowTitle(_translate("pyTranslate", "MainWindow"))
        self.lblTitle.setText(_translate("pyTranslate", "pyTranslate"))
        self.btClear.setText(_translate("pyTranslate", "Clear"))
        self.btSubmit.setText(_translate("pyTranslate", "Submit"))
        self.lblAuthor.setText(_translate("pyTranslate", "@PeiwenJi Computational Biology"))
        self.lblNote.setText(_translate("pyTranslate", "Please input a DNA sequence - numbers and blanks are ignored"))
        self.plainTextEdit.setPlaceholderText(_translate("pyTranslate", "Please input a DNA sequence to be translated."))


'''if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()    # 创建一个QMainWindow，用来装载你需要的各种组件、控件
    ui = Ui_pyTranslate()                    # ui是Ui_MainWindow()类的实例化对象
    ui.setupUi(MainWindow)                  # 执行类中的setupUi方法，方法的参数是第二步中创建的QMainWindow
    MainWindow.show()                       # 执行QMainWindow的show()方法，显示这个QMainWindow
    sys.exit(app.exec_())  '''