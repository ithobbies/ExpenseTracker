from PySide6 import QtWidgets, QtSql
from new_transaction import Ui_Dialog


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
        query.exec("""CREATE TABLE IF NOT EXISTS expenses (ID integer primary key AUTOINCREMENT,
                                                             Date VARCHAR(20),
                                                             Category VARCHAR(20), 
                                                             Description VARCHAR(20),
                                                             Balance REAL,
                                                             Status VARCHAR(20))""")
        return True

    def open_new_transaction(self):
        self.window = QtWidgets.QDialog()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self.window)
        self.window.show()
        self.ui.btn_new_transaction.clicked.connect(self.add_new_transaction)

    def add_new_transaction(self):
        query = QtSql.QSqlQuery()
        query.prepare("INSERT INTO expenses (Date, Category, Description, Balance, Status) VALUES (?, ?, ?, ?, ?)")
        query.addBindValue(self.ui.dateEdit.text())
        query.addBindValue(self.ui.cb_choose_category.currentText())
        query.addBindValue(self.ui.le_description.text())
        query.addBindValue(self.ui.le_balance.text())
        query.addBindValue(self.ui.cb_status.currentText())
        query.exec()

    def total_balance(self):
        query = QtSql.QSqlQuery()
        query.exec("SELECT SUM(Balance) FROM expenses")

        if query.next():
            return str(query.value(0))

        return -1
