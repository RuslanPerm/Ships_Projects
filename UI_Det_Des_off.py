import sys

from PySide6 import QtWidgets
from PySide6.QtSql import QSqlTableModel
from PySide6.QtWidgets import QApplication, QMainWindow

import det_des_off
import add_det_des_off

from connection import Data


class DetDesOffTable(QMainWindow):
    def __init__(self):
        super(DetDesOffTable, self).__init__()
        self.det_des_off_ui = det_des_off.Ui_Dialog()

        self.det_des_off_ui.setupUi(self)
        self.conn = Data()
        self.view_data()

        self.det_des_off_ui.btn_new_des_off.clicked.connect(self.open_new_des_off_window)
        self.det_des_off_ui.btn_delete_des_off.clicked.connect(self.delete_current_det_des_off)

        self.ids = []

    def view_data(self):
        self.model = QSqlTableModel(self)
        self.model.setTable('Details_DesignOffice')
        self.model.select()
        self.det_des_off_ui.tableView.setModel(self.model)

    def open_new_des_off_window(self):
        self.new_window = QtWidgets.QDialog()
        self.ui_window = add_det_des_off.Ui_Dialog()
        self.ui_window.setupUi(self.new_window)
        self.new_window.show()
        sender = self.sender()
        if sender.text() == "Add":
            self.ui_window.btn_save.clicked.connect(self.add_new_det_des_off)

    def add_new_det_des_off(self):
        id_det = self.ui_window.lineEdit.text()
        id_des_off = self.ui_window.lineEdit_4.text()
        quantity = self.ui_window.lineEdit_2.text()
        self.conn.add_new_det_des_off_query(id_det, id_des_off, quantity)
        self.view_data()
        self.new_window.close()

    def delete_current_det_des_off(self):
        index = self.det_des_off_ui.tableView.selectedIndexes()[0]
        if len(self.ids) == 1:
            self.ids.append(int(self.det_des_off_ui.tableView.model().data(index)))
            self.conn.delete_det_des_off_query(self.ids[0], self.ids[1])
        else:
            self.ids = [int(self.det_des_off_ui.tableView.model().data(index))]

        self.view_data()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = DetDesOffTable()
    window.show()
    sys.exit(app.exec())
