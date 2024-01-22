import sys

from PySide6 import QtWidgets
from PySide6.QtSql import QSqlTableModel
from PySide6.QtWidgets import QApplication, QMainWindow

import fac_det
import add_fac_det

from connection import Data


class FacDetTable(QMainWindow):
    def __init__(self):
        super(FacDetTable, self).__init__()
        self.des_off_proj_ui = fac_det.Ui_Dialog()

        self.des_off_proj_ui.setupUi(self)
        self.conn = Data()
        self.view_data()

        self.des_off_proj_ui.btn_new_des_off.clicked.connect(self.open_new_des_off_window)
        self.des_off_proj_ui.btn_delete_des_off.clicked.connect(self.delete_current_des_off_proj)

        self.ids = []

    def view_data(self):
        self.model = QSqlTableModel(self)
        self.model.setTable('Factory_Details')
        self.model.select()
        self.des_off_proj_ui.tableView.setModel(self.model)

    def open_new_des_off_window(self):
        self.new_window = QtWidgets.QDialog()
        self.ui_window = add_fac_det.Ui_Dialog()
        self.ui_window.setupUi(self.new_window)
        self.new_window.show()
        sender = self.sender()
        if sender.text() == "Add":
            self.ui_window.btn_save.clicked.connect(self.add_new_des_off_proj)

    def add_new_des_off_proj(self):
        id_fac = self.ui_window.lineEdit.text()
        id_det = self.ui_window.lineEdit_4.text()
        price = self.ui_window.lineEdit_5.text()
        self.conn.add_new_fac_det_query(id_fac, id_det, price)
        self.view_data()
        self.new_window.close()

    def delete_current_des_off_proj(self):
        index = self.des_off_proj_ui.tableView.selectedIndexes()[0]
        if len(self.ids) == 1:
            self.ids.append(int(self.des_off_proj_ui.tableView.model().data(index)))
            self.conn.delete_fac_det_query(self.ids[0], self.ids[1])
        else:
            self.ids = [int(self.des_off_proj_ui.tableView.model().data(index))]

        self.view_data()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = FacDetTable()
    window.show()
    sys.exit(app.exec())
