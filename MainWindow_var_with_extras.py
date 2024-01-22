# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindow_var_with_extras.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QLayout, QMainWindow, QPushButton,
    QSizePolicy, QSplitter, QWidget)
import resourses

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(560, 344)
        MainWindow.setWindowOpacity(0.980000000000000)
        MainWindow.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0, stop:0 rgba(81, 0, 135, 255), stop:0.427447 rgba(41, 61, 132, 235), stop:1 rgba(155, 79, 165, 255));\n"
"font-family: Noto Sans SC")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.splitter = QSplitter(self.centralwidget)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setGeometry(QRect(20, 30, 521, 291))
        self.splitter.setOrientation(Qt.Vertical)
        self.label = QLabel(self.splitter)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"color: white;\n"
"font-weight: bold;\n"
"font-size: 20pt;\n"
"background-color: none;\n"
"border: none;")
        self.splitter.addWidget(self.label)
        self.frame = QFrame(self.splitter)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"background-color: rgba(255, 255, 255, 30);\n"
"border-radius: 10px;")
        self.gridLayout = QGridLayout(self.frame)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.turn_to_emp = QPushButton(self.frame)
        self.turn_to_emp.setObjectName(u"turn_to_emp")
        self.turn_to_emp.setStyleSheet(u"QPushButton {\n"
"color: white;\n"
"background-color: rgba(255, 255, 255, 30);\n"
"border: 1px solid rgba(255, 255, 255, 40);\n"
"border-radius: 10px;\n"
"width: 230px;\n"
"height: 50px;\n"
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
        icon = QIcon()
        icon.addFile(u":/icons/icons/emp.png", QSize(), QIcon.Normal, QIcon.Off)
        self.turn_to_emp.setIcon(icon)

        self.gridLayout.addWidget(self.turn_to_emp, 1, 2, 1, 1)

        self.turn_to_costs = QPushButton(self.frame)
        self.turn_to_costs.setObjectName(u"turn_to_costs")
        self.turn_to_costs.setStyleSheet(u"QPushButton {\n"
"color: white;\n"
"background-color: rgba(255, 255, 255, 30);\n"
"border: 1px solid rgba(255, 255, 255, 40);\n"
"border-radius: 10px;\n"
"width: 230px;\n"
"height: 50px;\n"
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
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/price.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.turn_to_costs.setIcon(icon1)

        self.gridLayout.addWidget(self.turn_to_costs, 4, 0, 1, 1)

        self.turn_to_dep_proj = QPushButton(self.frame)
        self.turn_to_dep_proj.setObjectName(u"turn_to_dep_proj")
        self.turn_to_dep_proj.setStyleSheet(u"QPushButton {\n"
"color: white;\n"
"background-color: rgba(255, 255, 255, 30);\n"
"border: 1px solid rgba(255, 255, 255, 40);\n"
"border-radius: 10px;\n"
"width: 230px;\n"
"height: 50px;\n"
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
        icon2 = QIcon()
        icon2.addFile(u":/icons/icons/workin.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.turn_to_dep_proj.setIcon(icon2)

        self.gridLayout.addWidget(self.turn_to_dep_proj, 2, 1, 1, 1)

        self.turn_to_details = QPushButton(self.frame)
        self.turn_to_details.setObjectName(u"turn_to_details")
        self.turn_to_details.setStyleSheet(u"QPushButton {\n"
"color: white;\n"
"background-color: rgba(255, 255, 255, 30);\n"
"border: 1px solid rgba(255, 255, 255, 40);\n"
"border-radius: 10px;\n"
"width: 230px;\n"
"height: 50px;\n"
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
        icon3 = QIcon()
        icon3.addFile(u":/icons/icons/handyman_FILL0_wght400_GRAD0_opsz24.png", QSize(), QIcon.Normal, QIcon.Off)
        self.turn_to_details.setIcon(icon3)

        self.gridLayout.addWidget(self.turn_to_details, 1, 0, 1, 1)

        self.turn_to_quantity = QPushButton(self.frame)
        self.turn_to_quantity.setObjectName(u"turn_to_quantity")
        self.turn_to_quantity.setStyleSheet(u"QPushButton {\n"
"color: white;\n"
"background-color: rgba(255, 255, 255, 30);\n"
"border: 1px solid rgba(255, 255, 255, 40);\n"
"border-radius: 10px;\n"
"width: 230px;\n"
"height: 50px;\n"
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
        icon4 = QIcon()
        icon4.addFile(u":/icons/icons/quantity.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.turn_to_quantity.setIcon(icon4)

        self.gridLayout.addWidget(self.turn_to_quantity, 2, 0, 1, 1)

        self.turn_to_work_type = QPushButton(self.frame)
        self.turn_to_work_type.setObjectName(u"turn_to_work_type")
        self.turn_to_work_type.setStyleSheet(u"QPushButton {\n"
"color: white;\n"
"background-color: rgba(255, 255, 255, 30);\n"
"border: 1px solid rgba(255, 255, 255, 40);\n"
"border-radius: 10px;\n"
"width: 230px;\n"
"height: 50px;\n"
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
        icon5 = QIcon()
        icon5.addFile(u":/icons/icons/question_mark_FILL0_wght400_GRAD0_opsz24.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.turn_to_work_type.setIcon(icon5)

        self.gridLayout.addWidget(self.turn_to_work_type, 2, 2, 1, 1)

        self.turn_to_fac = QPushButton(self.frame)
        self.turn_to_fac.setObjectName(u"turn_to_fac")
        self.turn_to_fac.setStyleSheet(u"QPushButton {\n"
"color: white;\n"
"background-color: rgba(255, 255, 255, 30);\n"
"border: 1px solid rgba(255, 255, 255, 40);\n"
"border-radius: 10px;\n"
"width: 230px;\n"
"height: 50px;\n"
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
        icon6 = QIcon()
        icon6.addFile(u":/icons/icons/factory_FILL0_wght400_GRAD0_opsz24.png", QSize(), QIcon.Normal, QIcon.Off)
        self.turn_to_fac.setIcon(icon6)
        self.turn_to_fac.setIconSize(QSize(12, 12))

        self.gridLayout.addWidget(self.turn_to_fac, 0, 0, 1, 1)

        self.turn_to_dep = QPushButton(self.frame)
        self.turn_to_dep.setObjectName(u"turn_to_dep")
        self.turn_to_dep.setStyleSheet(u"QPushButton {\n"
"color: white;\n"
"background-color: rgba(255, 255, 255, 30);\n"
"border: 1px solid rgba(255, 255, 255, 40);\n"
"border-radius: 10px;\n"
"width: 230px;\n"
"height: 50px;\n"
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
        icon7 = QIcon()
        icon7.addFile(u":/icons/icons/segment_FILL0_wght400_GRAD0_opsz24.png", QSize(), QIcon.Normal, QIcon.Off)
        self.turn_to_dep.setIcon(icon7)
        self.turn_to_dep.setAutoRepeatDelay(300)

        self.gridLayout.addWidget(self.turn_to_dep, 1, 1, 1, 1)

        self.turn_to_des_off = QPushButton(self.frame)
        self.turn_to_des_off.setObjectName(u"turn_to_des_off")
        self.turn_to_des_off.setStyleSheet(u"QPushButton {\n"
"color: white;\n"
"background-color: rgba(255, 255, 255, 30);\n"
"border: 1px solid rgba(255, 255, 255, 40);\n"
"border-radius: 10px;\n"
"width: 230px;\n"
"height: 50px;\n"
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
        icon8 = QIcon()
        icon8.addFile(u":/icons/icons/source_environment_FILL0_wght400_GRAD0_opsz24.png", QSize(), QIcon.Normal, QIcon.Off)
        self.turn_to_des_off.setIcon(icon8)

        self.gridLayout.addWidget(self.turn_to_des_off, 0, 2, 1, 1)

        self.turn_to_proj = QPushButton(self.frame)
        self.turn_to_proj.setObjectName(u"turn_to_proj")
        self.turn_to_proj.setMinimumSize(QSize(0, 18))
        self.turn_to_proj.setMaximumSize(QSize(16777211, 16777215))
        self.turn_to_proj.setStyleSheet(u"QPushButton {\n"
"color: white;\n"
"background-color: rgba(255, 255, 255, 30);\n"
"border: 1px solid rgba(255, 255, 255, 40);\n"
"border-radius: 10px;\n"
"width: 230px;\n"
"height: 50px;\n"
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
        icon9 = QIcon()
        icon9.addFile(u":/icons/icons/directions_boat_FILL0_wght400_GRAD0_opsz24.png", QSize(), QIcon.Normal, QIcon.Off)
        self.turn_to_proj.setIcon(icon9)
        self.turn_to_proj.setAutoDefault(False)

        self.gridLayout.addWidget(self.turn_to_proj, 0, 1, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_total = QLabel(self.frame)
        self.label_total.setObjectName(u"label_total")
        self.label_total.setStyleSheet(u"color: white;\n"
"background-color: rgba(255, 255, 255, 40);\n"
"font: bold 9pt;\n"
"padding-left: 3px")

        self.horizontalLayout.addWidget(self.label_total)

        self.total_show = QLabel(self.frame)
        self.total_show.setObjectName(u"total_show")
        self.total_show.setStyleSheet(u"color: white;\n"
"background-color: rgba(255, 255, 255, 40);\n"
"font: bold 9pt;")

        self.horizontalLayout.addWidget(self.total_show)


        self.gridLayout.addLayout(self.horizontalLayout, 4, 1, 1, 1)

        self.splitter.addWidget(self.frame)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Database of Marine Ships", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Database of Marine Ships", None))
        self.turn_to_emp.setText(QCoreApplication.translate("MainWindow", u"Employees", None))
        self.turn_to_costs.setText(QCoreApplication.translate("MainWindow", u"Cost of details", None))
        self.turn_to_dep_proj.setText(QCoreApplication.translate("MainWindow", u"What projects are\n"
" departments working on", None))
        self.turn_to_details.setText(QCoreApplication.translate("MainWindow", u"Details", None))
        self.turn_to_quantity.setText(QCoreApplication.translate("MainWindow", u"Quantity of details\n"
"in Design Offices", None))
        self.turn_to_work_type.setText(QCoreApplication.translate("MainWindow", u"What type of work\n"
" Design Offices do", None))
        self.turn_to_fac.setText(QCoreApplication.translate("MainWindow", u"Factories", None))
        self.turn_to_dep.setText(QCoreApplication.translate("MainWindow", u"Departments", None))
        self.turn_to_des_off.setText(QCoreApplication.translate("MainWindow", u"Design Offices", None))
        self.turn_to_proj.setText(QCoreApplication.translate("MainWindow", u"Projects", None))
        self.label_total.setText(QCoreApplication.translate("MainWindow", u"Total cost of\n"
"all projects:", None))
        self.total_show.setText("")
    # retranslateUi

