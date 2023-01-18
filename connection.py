from PySide6 import QtWidgets, QtSql


class Data:
    def __init__(self):
        super(Data, self).__init__()
        self.create_connection()

    def create_connection(self):
        db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
        db.setDatabaseName('expense_db.db')

        if not db.open():
            QtWidgets.QMessageBox.critical(None, "Cannot open database",
                                           "Click Cancel to exit.", QtWidgets.QMessageBox.Cancel)
            return False

        query = QtSql.QSqlQuery()
        query.exec("""CREATE TABLE IF NOT EXISTS expenses (ID int primary key, 
                                                              Category VARCHAR(20), 
                                                             Description VARCHAR(20),
                                                             Balance REAL,
                                                             Status VARCHAR(20))""")
        query.exec("insert into expenses values(101, 'Auto', 'REPAIR', 200.2, 'Outcome')")
        query.exec("insert into expenses values(102, 'Auto', 'REPAIR', 200.1, 'Outcome')")
        return True

    def total_balance(self):
        query = QtSql.QSqlQuery()
        query.exec("SELECT SUM(Balance) FROM expenses")

        if query.next():
            return query.value(0).toString()

        return -1
