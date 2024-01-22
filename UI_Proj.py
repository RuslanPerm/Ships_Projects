import sys

from PySide6 import QtWidgets
from PySide6.QtSql import QSqlTableModel
from PySide6.QtWidgets import QApplication, QMainWindow

import projects
import add_project

from connection import Data


class ProjTable(QMainWindow):
    def __init__(self):
        super(ProjTable, self).__init__()
        self.proj_ui = projects.Ui_Dialog()

        self.proj_ui.setupUi(self)
        self.conn = Data()
        self.view_data()

        self.proj_ui.btn_add.clicked.connect(self.open_new_window)
        self.proj_ui.btn_delete.clicked.connect(self.delete_current)

    def view_data(self):
        self.model = QSqlTableModel(self)
        self.model.setTable('Project')
        self.model.select()
        self.proj_ui.tableView.setModel(self.model)

    def open_new_window(self):
        self.new_window = QtWidgets.QDialog()
        self.ui_window = add_project.Ui_Dialog()
        self.ui_window.setupUi(self.new_window)
        self.new_window.show()
        sender = self.sender()
        if sender.text() == "Add project":
            self.ui_window.btn_save.clicked.connect(self.add_new)

    def add_new(self):
        name = self.ui_window.lineEdit_3.text()
        main_designer = self.ui_window.lineEdit_5.text()
        start_date = self.ui_window.dateEdit.text()
        finish_date = self.ui_window.dateEdit_6.text()
        cost = self.ui_window.lineEdit_6.text()
        self.conn.add_new_project_query(name, main_designer, start_date, finish_date, cost)
        self.view_data()
        self.new_window.close()

    def delete_current(self):
        index = self.proj_ui.tableView.selectedIndexes()[0]
        id_proj = int(self.proj_ui.tableView.model().data(index))
        self.conn.delete_project_query(id_proj)

        self.view_data()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ProjTable()
    window.show()
    sys.exit(app.exec())
