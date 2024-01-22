import sys

from PySide6 import QtWidgets
from PySide6.QtWidgets import QApplication, QMainWindow

import departments
import des_off_proj
import design_offices
import det_des_off
import details
import employees
import fac_det
import factory
import proj_dep
import projects
from MainWindow_var_with_extras import Ui_MainWindow
from connection import Data


class ShipsDatabase(QMainWindow):
    def __init__(self):
        super(ShipsDatabase, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.conn = Data()

        self.ui.turn_to_fac.clicked.connect(self.open_factory)
        self.ui.turn_to_proj.clicked.connect(self.open_projects)
        self.ui.turn_to_dep.clicked.connect(self.open_departments)
        self.ui.turn_to_emp.clicked.connect(self.open_employees)
        self.ui.turn_to_des_off.clicked.connect(self.open_des_offs)
        self.ui.turn_to_costs.clicked.connect(self.open_costs)
        self.ui.turn_to_dep_proj.clicked.connect(self.open_dep_proj)
        self.ui.turn_to_details.clicked.connect(self.open_details)
        self.ui.turn_to_quantity.clicked.connect(self.open_quantity)
        self.ui.turn_to_work_type.clicked.connect(self.open_work_type)

        self.reload_data()

    def open_factory(self):
        self.new_window = QtWidgets.QDialog()
        self.ui_window = factory.Ui_Dialog()
        self.ui_window.setupUi(self.new_window)
        self.new_window.show()

    def open_projects(self):
        self.new_window = QtWidgets.QDialog()
        self.ui_window = projects.Ui_Dialog()
        self.ui_window.setupUi(self.new_window)
        self.new_window.show()

    def open_departments(self):
        self.new_window = QtWidgets.QDialog()
        self.ui_window = departments.Ui_Dialog()
        self.ui_window.setupUi(self.new_window)
        self.new_window.show()

    def open_employees(self):
        self.new_window = QtWidgets.QDialog()
        self.ui_window = employees.Ui_Dialog()
        self.ui_window.setupUi(self.new_window)
        self.new_window.show()

    def open_des_offs(self):
        self.new_window = QtWidgets.QDialog()
        self.ui_window = design_offices.Ui_Dialog()
        self.ui_window.setupUi(self.new_window)
        self.new_window.show()

    def open_costs(self):
        self.new_window = QtWidgets.QDialog()
        self.ui_window = fac_det.Ui_Dialog()
        self.ui_window.setupUi(self.new_window)
        self.new_window.show()

    def open_dep_proj(self):
        self.new_window = QtWidgets.QDialog()
        self.ui_window = proj_dep.Ui_Dialog()
        self.ui_window.setupUi(self.new_window)
        self.new_window.show()

    def open_details(self):
        self.new_window = QtWidgets.QDialog()
        self.ui_window = details.Ui_Dialog()
        self.ui_window.setupUi(self.new_window)
        self.new_window.show()

    def open_quantity(self):
        self.new_window = QtWidgets.QDialog()
        self.ui_window = det_des_off.Ui_Dialog()
        self.ui_window.setupUi(self.new_window)
        self.new_window.show()

    def open_work_type(self):
        self.new_window = QtWidgets.QDialog()
        self.ui_window = des_off_proj.Ui_Dialog()
        self.ui_window.setupUi(self.new_window)
        self.new_window.show()

    def reload_data(self):
        self.ui.total_show.setText(self.conn.get_total())


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ShipsDatabase()
    window.show()
    sys.exit(app.exec())
