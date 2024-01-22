import sys

from PySide6 import QtWidgets
from PySide6.QtSql import QSqlTableModel
from PySide6.QtWidgets import QApplication, QMainWindow

import employees
import add_employer

from connection import Data


class EmpTable(QMainWindow):
    def __init__(self):
        super(EmpTable, self).__init__()
        self.emp_ui = employees.Ui_Dialog()

        self.emp_ui.setupUi(self)
        self.conn = Data()
        self.view_data()

        self.emp_ui.btn_add.clicked.connect(self.open_new_window)
        self.emp_ui.btn_delete.clicked.connect(self.delete_current)

    def view_data(self):
        self.model = QSqlTableModel(self)
        self.model.setTable('Employees')
        self.model.select()
        self.emp_ui.tableView.setModel(self.model)

    def open_new_window(self):
        self.new_window = QtWidgets.QDialog()
        self.ui_window = add_employer.Ui_Dialog()
        self.ui_window.setupUi(self.new_window)
        self.new_window.show()
        sender = self.sender()
        if sender.text() == "Add employer":
            self.ui_window.btn_save.clicked.connect(self.add_new)

    def add_new(self):
        name = self.ui_window.lineEdit_3.text()
        dep_name = self.ui_window.lineEdit.text()
        position = self.ui_window.lineEdit_4.text()
        phone = self.ui_window.lineEdit_5.text()
        off_num = self.ui_window.lineEdit_2.text()
        self.conn.add_new_employees_query(name, dep_name, position, phone, off_num)
        self.view_data()
        self.new_window.close()

    def delete_current(self):
        index = self.emp_ui.tableView.selectedIndexes()[0]
        id_emp = int(self.emp_ui.tableView.model().data(index))
        self.conn.delete_employees_query(id_emp)

        self.view_data()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = EmpTable()
    window.show()
    sys.exit(app.exec())
