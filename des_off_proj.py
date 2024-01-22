# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'des_off_proj.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QFrame, QHBoxLayout,
    QHeaderView, QLabel, QPushButton, QSizePolicy,
    QTableView, QVBoxLayout, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(653, 389)
        Dialog.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0, stop:0 rgba(81, 0, 135, 255), stop:0.427447 rgba(41, 61, 132, 235), stop:1 rgba(155, 79, 165, 255));\n"
"")
        self.frame = QFrame(Dialog)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(10, 10, 651, 381))
        self.frame.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0, stop:0 rgba(81, 0, 135, 255), stop:0.427447 rgba(41, 61, 132, 235), stop:1 rgba(155, 79, 165, 255));")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(280, 10, 131, 21))
        self.label.setStyleSheet(u"color: white;\n"
"font-weight: bold;\n"
"font-size: 15pt;\n"
"background-color: none;\n"
"border: none;")
        self.layoutWidget = QWidget(self.frame)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, 40, 621, 331))
        self.verticalLayout = QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.tableView = QTableView(self.layoutWidget)
        self.tableView.setObjectName(u"tableView")
        self.tableView.setStyleSheet(u"QTableView {\n"
"background-color: rgba(255, 255, 255, 30);\n"
"border: 1px solid rgba(255, 255, 255, 40);\n"
"border-radius: 7px;\n"
"}\n"
"\n"
"QTableView::section {\n"
"background-color: rgba(53, 53, 53);\n"
"color: white;\n"
"border: none;\n"
"height: 50px;\n"
"font-size: 14pt;\n"
"}\n"
"\n"
"QTableView::item {\n"
"border-style: none;\n"
"border: 1px solid rgba(255, 255, 255, 40);\n"
"}\n"
"\n"
"QTableView::item:selected {\n"
"border: none;\n"
"color: rgba(255, 255, 255);\n"
"background-color: rgba(255, 255, 255, 50);\n"
"}")
        self.tableView.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.tableView.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.tableView.setShowGrid(False)
        self.tableView.horizontalHeader().setDefaultSectionSize(135)

        self.verticalLayout.addWidget(self.tableView)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.btn_new_des_off = QPushButton(self.layoutWidget)
        self.btn_new_des_off.setObjectName(u"btn_new_des_off")
        self.btn_new_des_off.setStyleSheet(u"QPushButton {\n"
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
"color: black;\n"
"background-color: rgba(0, 0, 0, 30);\n"
"border: 1px solid rgba(0, 0, 0, 40);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"color: black;\n"
"background-color: rgba(0, 0, 0, 80);\n"
"border: 1px solid rgba(0, 0, 0, 90);\n"
"}")

        self.horizontalLayout.addWidget(self.btn_new_des_off)

        self.btn_delete_des_off = QPushButton(self.layoutWidget)
        self.btn_delete_des_off.setObjectName(u"btn_delete_des_off")
        self.btn_delete_des_off.setStyleSheet(u"QPushButton {\n"
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
"color: black;\n"
"background-color: rgba(255, 0, 0, 50);\n"
"border: 1px solid rgba(255, 0, 0, 60);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"color: black;\n"
"background-color: rgba(255, 0, 0, 90);\n"
"border: 1px solid rgba(255, 0, 0, 100);\n"
"}")

        self.horizontalLayout.addWidget(self.btn_delete_des_off)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Work type", None))
        self.btn_new_des_off.setText(QCoreApplication.translate("Dialog", u"Add", None))
        self.btn_delete_des_off.setText(QCoreApplication.translate("Dialog", u"Delete current", None))
    # retranslateUi

