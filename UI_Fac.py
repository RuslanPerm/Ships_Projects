import sys

from PySide6 import QtWidgets
from PySide6.QtSql import QSqlTableModel
from PySide6.QtWidgets import QApplication, QMainWindow

import factory
import add_factory

from connection import Data


class FacTable(QMainWindow):
    def __init__(self):
        super(FacTable, self).__init__()
        self.fac_ui = factory.Ui_Dialog()

        self.fac_ui.setupUi(self)
        self.conn = Data()
        self.view_data()

        self.fac_ui.btn_add.clicked.connect(self.open_new_window)
        self.fac_ui.btn_delete.clicked.connect(self.delete_current)

    def view_data(self):
        self.model = QSqlTableModel(self)
        self.model.setTable('Factory')
        self.model.select()
        self.fac_ui.tableView.setModel(self.model)

    def open_new_window(self):
        self.new_window = QtWidgets.QDialog()
        self.ui_window = add_factory.Ui_Dialog()
        self.ui_window.setupUi(self.new_window)
        self.new_window.show()
        sender = self.sender()
        if sender.text() == "Add factory":
            self.ui_window.pushButton.clicked.connect(self.add_new_det)

    def add_new_det(self):
        name = self.ui_window.lineEdit.text()
        director = self.ui_window.lineEdit_2.text()
        self.conn.add_new_factory_query(name, director)
        self.view_data()
        self.new_window.close()

    def delete_current(self):
        index = self.fac_ui.tableView.selectedIndexes()[0]
        id_fac = int(self.fac_ui.tableView.model().data(index))
        self.conn.delete_factory_query(id_fac)

        self.view_data()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = FacTable()
    window.show()
    sys.exit(app.exec())
