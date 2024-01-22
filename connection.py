from PySide6 import QtWidgets, QtSql


class Data:
    def __init__(self):
        super(Data, self).__init__()
        self.create_connection()

    def create_connection(self):
        db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
        db.setDatabaseName('Ships.db')

        if not db.open():
            QtWidgets.QMessageBox.critical(None, "Can not connect database",
                                           "Click cancel", QtWidgets.QMessageBox.Cancel)
            return False

        query = QtSql.QSqlQuery()
        query.exec("CREATE TABLE IF NOT EXISTS Departments (id_department PRIMARY KEY AUTOINCREMENT, name TEXT, "
                   "dep_head TEXT, address TEXT")
        query.exec("CREATE TABLE IF NOT EXISTS Design_office (id_des_off PRIMARY KEY AUTOINCREMENT, name TEXT, "
                   "director TEXT, complited_projects_quantity INTEGER")
        query.exec("CREATE TABLE IF NOT EXISTS Factory (id_factory PRIMARY KEY AUTOINCREMENT, name TEXT, "
                   "director TEXT")
        query.exec("CREATE TABLE IF NOT EXISTS Project (id_project INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, "
                   "main_designer TEXT, start_date NUMERIC, finish_date NUMERIC, cost REAL")
        query.exec("CREATE TABLE IF NOT EXISTS DesignOffice_Project (id_des_officie	INTEGER, id_project	INTEGER, "
                   "work_type TEXT,	FOREIGN KEY(id_project) REFERENCES Project(id_project),	"
                   "FOREIGN KEY(id_des_officie) REFERENCES Design_office(id_des_office), PRIMARY KEY(id_des_officie,"
                   "id_project")
        return True

    def execute_query_with_params(self, sql_query, query_values=None):
        query = QtSql.QSqlQuery()
        query.prepare(sql_query)

        if query_values is not None:
            for query_value in query_values:
                query.addBindValue(query_value)

        query.exec()
        return query

    # Department
    def add_new_department_query(self, name, dep_head, address):
        sql_query = "INSERT INTO Departments (name, dep_head, address) VALUES (?, ?, ?)"
        self.execute_query_with_params(sql_query, [name, dep_head, address])

    def delete_department_query(self, id_department):
        sql_query = "DELETE FROM Departments WHERE id_department=?"
        self.execute_query_with_params(sql_query, [id_department])

    # Design_office
    def add_new_design_office_query(self, name, director, complited_projects_quantity):
        sql_query = "INSERT INTO Design_office (name, director, complited_projects_quantity) VALUES (?, ?, ?)"
        self.execute_query_with_params(sql_query, [name, director, complited_projects_quantity])

    def delete_design_office_query(self, id_des_office):
        sql_query = "DELETE FROM Design_office WHERE id_des_office=?"
        self.execute_query_with_params(sql_query, [id_des_office])

    # Details
    def add_new_details_query(self, name, mass, material):
        sql_query = "INSERT INTO Details (name, mass, material) VALUES (?, ?, ?)"
        self.execute_query_with_params(sql_query, [name, mass, material])

    def delete_details_query(self, id_detail):
        sql_query = "DELETE FROM Details WHERE id_detail=?"
        self.execute_query_with_params(sql_query, [id_detail])

    # Employees
    def add_new_employees_query(self, full_name, dep_name, position, phone_num, office_num):
        sql_query = "INSERT INTO Employees (full_name, dep_name, position, phone_num, office_num)" \
                    " VALUES (?, ?, ?, ?, ?)"
        self.execute_query_with_params(sql_query, [full_name, dep_name, position, phone_num, office_num])

    def delete_employees_query(self, id_emp):
        sql_query = "DELETE FROM Employees WHERE id_emp=?"
        self.execute_query_with_params(sql_query, [id_emp])

    # Factory
    def add_new_factory_query(self, name, director):
        sql_query = "INSERT INTO Factory (name, director) VALUES (?, ?)"
        self.execute_query_with_params(sql_query, [name, director])

    def delete_factory_query(self, id_factory):
        sql_query = "DELETE FROM Factory WHERE id_factory=?"
        self.execute_query_with_params(sql_query, [id_factory])

    # Project
    def add_new_project_query(self, name, main_designer, start_date, finish_date, cost):
        sql_query = "INSERT INTO Project (name, main_designer, start_date, finish_date, cost)" \
                    " VALUES (?, ?, ?, ?, ?)"
        self.execute_query_with_params(sql_query, [name, main_designer, start_date, finish_date, cost])

    def delete_project_query(self, id_project):
        sql_query = "DELETE FROM Project WHERE id_project=?"
        self.execute_query_with_params(sql_query, [id_project])

    # Det_Des_off
    def add_new_det_des_off_query(self, id_detail, id_des_office, quantity):
        sql_query = "INSERT INTO Details_DesignOffice (id_detail, id_des_office, quantity)" \
                    " VALUES (?, ?, ?)"
        self.execute_query_with_params(sql_query, [id_detail, id_des_office, quantity])

    def delete_det_des_off_query(self, id_detail, id_des_office):
        sql_query = "DELETE FROM Details_DesignOffice WHERE id_detail=? AND id_des_office=?"
        self.execute_query_with_params(sql_query, [id_detail, id_des_office])

    # Des_off_Proj
    def add_new_des_off_proj_query(self, id_detail, id_des_office, work_type):
        sql_query = "INSERT INTO DesignOffice_Project (id_des_officie, id_project, work_type)" \
                    " VALUES (?, ?, ?)"
        self.execute_query_with_params(sql_query, [id_detail, id_des_office, work_type])

    def delete_des_off_proj_query(self, id_des_office, id_project):
        sql_query = "DELETE FROM DesignOffice_Project WHERE id_des_officie=? AND id_project=?"
        self.execute_query_with_params(sql_query, [id_des_office, id_project])

    # Proj_Dep
    def add_new_proj_dep_query(self, id_project, id_dep):
        sql_query = "INSERT INTO Project_Departments (id_project, id_department)" \
                    " VALUES (?, ?)"
        self.execute_query_with_params(sql_query, [id_project, id_dep])

    def delete_proj_dep_query(self, id_project, id_dep):
        sql_query = "DELETE FROM Project_Departments WHERE id_project=? AND id_department=?"
        self.execute_query_with_params(sql_query, [id_project, id_dep])

    # Proj_Dep
    def add_new_fac_det_query(self, id_factory, id_detail, price):
        sql_query = "INSERT INTO Factory_Details (id_factory, id_detail, price)" \
                    " VALUES (?, ?, ?)"
        self.execute_query_with_params(sql_query, [id_factory, id_detail, price])

    def delete_fac_det_query(self, id_factory, id_detail):
        sql_query = "DELETE FROM Factory_Details WHERE id_factory=? AND id_detail=?"
        self.execute_query_with_params(sql_query, [id_factory, id_detail])

    # Вычисляемое поле (в нашем случае считаем общие затраты на разрабатываемые проекты)
    def get_total(self):
        sql_query = """SELECT SUM(cost) FROM Project"""
        query = self.execute_query_with_params(sql_query)

        if query.next():
            return str(query.value(0)) + '$'

        return '0'
