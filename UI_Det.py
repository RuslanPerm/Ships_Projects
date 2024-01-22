import sys

from PySide6 import QtWidgets
from PySide6.QtSql import QSqlTableModel
from PySide6.QtWidgets import QApplication, QMainWindow

import details
import add_detail

from connection import Data


class DetTable(QMainWindow):
    def __init__(self):
        super(DetTable, self).__init__()
        self.det_ui = details.Ui_Dialog()

        self.det_ui.setupUi(self)
        self.conn = Data()
        self.view_data()

        self.det_ui.btn_add.clicked.connect(self.open_new_window)
        self.det_ui.btn_delete.clicked.connect(self.delete_current)

    def view_data(self):
        self.model = QSqlTableModel(self)
        self.model.setTable('Details')
        self.model.select()
        self.det_ui.tableView.setModel(self.model)

    def open_new_window(self):
        self.new_window = QtWidgets.QDialog()
        self.ui_window = add_detail.Ui_Dialog()
        self.ui_window.setupUi(self.new_window)
        self.new_window.show()
        sender = self.sender()
        if sender.text() == "Add detail":
            self.ui_window.btn_save.clicked.connect(self.add_new_det)

    def add_new_det(self):
        name = self.ui_window.lineEdit_3.text()
        mass = self.ui_window.lineEdit.text()
        material = self.ui_window.lineEdit_2.text()
        self.conn.add_new_details_query(name, mass, material)
        self.view_data()
        self.new_window.close()

    def delete_current(self):
        index = self.det_ui.tableView.selectedIndexes()[0]
        id_det = int(self.det_ui.tableView.model().data(index))
        self.conn.delete_details_query(id_det)

        self.view_data()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = DetTable()
    window.show()
    sys.exit(app.exec())
