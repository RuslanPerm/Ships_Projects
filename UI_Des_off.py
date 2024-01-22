import sys

from PySide6 import QtWidgets
from PySide6.QtSql import QSqlTableModel
from PySide6.QtWidgets import QApplication, QMainWindow

import design_offices
import add_des_office

from connection import Data


class DesOffTable(QMainWindow):
    def __init__(self):
        super(DesOffTable, self).__init__()
        self.des_off_ui = design_offices.Ui_Dialog()

        self.des_off_ui.setupUi(self)
        self.conn = Data()
        self.view_data()

        self.des_off_ui.btn_new_des_off.clicked.connect(self.open_new_des_off_window)
        self.des_off_ui.btn_delete_des_off.clicked.connect(self.delete_current_des_off)

    def view_data(self):
        self.model = QSqlTableModel(self)
        self.model.setTable('Design_office')
        self.model.select()
        self.des_off_ui.tableView.setModel(self.model)

    def open_new_des_off_window(self):
        self.new_window = QtWidgets.QDialog()
        self.ui_window = add_des_office.Ui_Dialog()
        self.ui_window.setupUi(self.new_window)
        self.new_window.show()
        sender = self.sender()
        if sender.text() == "Add design office":
            self.ui_window.pushButton.clicked.connect(self.add_new_des_off)

    def add_new_des_off(self):
        name = self.ui_window.lineEdit_3.text()
        director = self.ui_window.lineEdit_5.text()
        complited_project_quantity = self.ui_window.lineEdit_2.text()
        self.conn.add_new_design_office_query(name, director, complited_project_quantity)
        self.view_data()
        self.new_window.close()

    def delete_current_des_off(self):
        index = self.des_off_ui.tableView.selectedIndexes()[0]
        id_des_off = int(self.des_off_ui.tableView.model().data(index))
        self.conn.delete_design_office_query(id_des_off)

        self.view_data()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = DesOffTable()
    window.show()
    sys.exit(app.exec())
