# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'add_project.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDateEdit, QDialog, QFrame,
    QHBoxLayout, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(199, 300)
        Dialog.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0, stop:0 rgba(81, 0, 135, 255), stop:0.427447 rgba(41, 61, 132, 235), stop:1 rgba(155, 79, 165, 255));")
        self.frame = QFrame(Dialog)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(10, 10, 181, 281))
        self.frame.setStyleSheet(u"background-color: rgba(255, 255, 255, 30);\n"
"border-radius: 10px")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"color: white;\n"
"font-weight: bold;\n"
"font-size: 13pt;\n"
"background-color: none;\n"
"border: none;")
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.label)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.lineEdit_3 = QLineEdit(self.frame)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setStyleSheet(u"color: white;\n"
"font-size: 13pt;\n"
"border-radius: 2px")

        self.verticalLayout.addWidget(self.lineEdit_3)

        self.lineEdit_5 = QLineEdit(self.frame)
        self.lineEdit_5.setObjectName(u"lineEdit_5")
        self.lineEdit_5.setStyleSheet(u"color: white;\n"
"font-size: 13pt;\n"
"border-radius: 2px")

        self.verticalLayout.addWidget(self.lineEdit_5)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"color: rgba(255, 255, 255, 98);\n"
"font-size: 12pt;")

        self.horizontalLayout.addWidget(self.label_2)

        self.dateEdit = QDateEdit(self.frame)
        self.dateEdit.setObjectName(u"dateEdit")
        self.dateEdit.setStyleSheet(u"color: rgba(255, 255, 255, 98);\n"
"font-size: 12pt;")
        self.dateEdit.setDateTime(QDateTime(QDate(2024, 1, 1), QTime(0, 0, 0)))
        self.dateEdit.setMinimumDate(QDate(1930, 1, 1))

        self.horizontalLayout.addWidget(self.dateEdit)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_7 = QLabel(self.frame)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setStyleSheet(u"color: rgba(255, 255, 255, 98);\n"
"font-size: 12pt;")

        self.horizontalLayout_6.addWidget(self.label_7)

        self.dateEdit_6 = QDateEdit(self.frame)
        self.dateEdit_6.setObjectName(u"dateEdit_6")
        self.dateEdit_6.setStyleSheet(u"color: rgba(255, 255, 255, 98);\n"
"font-size: 12pt;")
        self.dateEdit_6.setDateTime(QDateTime(QDate(2024, 1, 1), QTime(0, 0, 0)))
        self.dateEdit_6.setMinimumDate(QDate(1930, 1, 1))

        self.horizontalLayout_6.addWidget(self.dateEdit_6)


        self.verticalLayout.addLayout(self.horizontalLayout_6)

        self.lineEdit_6 = QLineEdit(self.frame)
        self.lineEdit_6.setObjectName(u"lineEdit_6")
        self.lineEdit_6.setStyleSheet(u"color: white;\n"
"font-size: 13pt;\n"
"border-radius: 2px")

        self.verticalLayout.addWidget(self.lineEdit_6)


        self.verticalLayout_3.addLayout(self.verticalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.btn_save = QPushButton(self.frame)
        self.btn_save.setObjectName(u"btn_save")
        self.btn_save.setStyleSheet(u"QPushButton {\n"
"color: white;\n"
"background-color: rgba(255, 255, 255, 30);\n"
"border: 1px solid rgba(255, 255, 255, 40);\n"
"border-radius: 10px;\n"
"width: 50px;\n"
"height: 20px;\n"
"font: 10pt;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: rgba(0, 255, 0, 50);\n"
"border: 1px solid rgba(0, 255, 0, 60);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background-color: rgba(0, 255, 0, 90);\n"
"border: 1px solid rgba(0, 255, 0, 100);\n"
"}")

        self.verticalLayout_2.addWidget(self.btn_save)


        self.verticalLayout_3.addLayout(self.verticalLayout_2)


        self.verticalLayout_4.addLayout(self.verticalLayout_3)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Adding new project", None))
        self.lineEdit_3.setText("")
        self.lineEdit_3.setPlaceholderText(QCoreApplication.translate("Dialog", u"Name", None))
        self.lineEdit_5.setText("")
        self.lineEdit_5.setPlaceholderText(QCoreApplication.translate("Dialog", u"Main designer", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"Start date", None))
        self.label_7.setText(QCoreApplication.translate("Dialog", u"Finish date", None))
        self.lineEdit_6.setText("")
        self.lineEdit_6.setPlaceholderText(QCoreApplication.translate("Dialog", u"Cost", None))
        self.btn_save.setText(QCoreApplication.translate("Dialog", u"Save", None))
    # retranslateUi

