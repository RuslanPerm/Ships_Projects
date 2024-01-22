import sys

from PySide6 import QtWidgets
from PySide6.QtSql import QSqlTableModel
from PySide6.QtWidgets import QApplication, QMainWindow

import departments
import add_department

from connection import Data


class DepTable(QMainWindow):
    def __init__(self):
        super(DepTable, self).__init__()
        self.dep_ui = departments.Ui_Dialog()

        self.dep_ui.setupUi(self)
        self.conn = Data()
        self.view_dep_data()

        self.dep_ui.btn_new_department.clicked.connect(self.open_new_department_window)
        self.dep_ui.btn_delete_department.clicked.connect(self.delete_current_department)

    def view_dep_data(self):
        self.model = QSqlTableModel(self)
        self.model.setTable('Departments')
        self.model.select()
        self.dep_ui.tableView.setModel(self.model)

    def open_new_department_window(self):
        self.new_window = QtWidgets.QDialog()
        self.ui_window = add_department.Ui_Dialog()
        self.ui_window.setupUi(self.new_window)
        self.new_window.show()
        sender = self.sender()
        if sender.text() == "Add department":
            self.ui_window.btn_add_new_dep.clicked.connect(self.add_new_department)

    def add_new_department(self):
        name = self.ui_window.lineEdit_3.text()
        dep_head = self.ui_window.lineEdit_5.text()
        address = self.ui_window.lineEdit_2.text()
        self.conn.add_new_department_query(name, dep_head, address)
        self.view_dep_data()
        self.new_window.close()

    def delete_current_department(self):
        index = self.dep_ui.tableView.selectedIndexes()[0]
        id_dep = int(self.dep_ui.tableView.model().data(index))
        self.conn.delete_department_query(id_dep)

        self.view_dep_data()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = DepTable()
    window.show()
    sys.exit(app.exec())
