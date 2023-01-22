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
        query.exec("""CREATE TABLE IF NOT EXISTS expenses (ID integer primary key AUTOINCREMENT,
                                                             Date VARCHAR(20),
                                                             Category VARCHAR(20), 
                                                             Description VARCHAR(20),
                                                             Balance REAL,
                                                             Status VARCHAR(20))""")
        return True

    def add_new_transaction_query(self, date, category, description, balance, status):
        query = QtSql.QSqlQuery()
        query.prepare("INSERT INTO expenses (Date, Category, Description, Balance, Status) VALUES (?, ?, ?, ?, ?)")
        query.addBindValue(date)
        query.addBindValue(category)
        query.addBindValue(description)
        query.addBindValue(balance)
        query.addBindValue(status)
        query.exec()

    def update_transaction_query(self, date, category, description, balance, status, id):
        query = QtSql.QSqlQuery()
        query.exec("UPDATE expenses SET Date=?, Category=?, Description=?, Balance=?, Status=? WHERE ID='%s'" % id)
        query.addBindValue(date)
        query.addBindValue(category)
        query.addBindValue(description)
        query.addBindValue(balance)
        query.addBindValue(status)
        query.exec()

    def delete_transaction_query(self, id):
        query = QtSql.QSqlQuery()
        query.exec("DELETE FROM expenses WHERE ID='%s'" % id)
        query.exec()

    def total_balance(self):
        query = QtSql.QSqlQuery()
        query.exec("SELECT SUM(Balance) FROM expenses")

        if query.next():
            return str(query.value(0)) + '$'

        return '0'

    def total_income(self):
        query = QtSql.QSqlQuery()
        query.exec("SELECT SUM(Balance) FROM expenses WHERE Status='Income'")

        if query.next():
            return str(query.value(0)) + '$'

        return '0'

    def total_outcome(self):
        query = QtSql.QSqlQuery()
        query.exec("SELECT SUM(Balance) FROM expenses WHERE Status='Outcome'")

        if query.next():
            return str(query.value(0)) + '$'

        return '0'

    def total_groceries(self):
        query = QtSql.QSqlQuery()
        query.exec("SELECT SUM(Balance) FROM expenses WHERE Category='Grocery'")

        if query.next():
            return str(query.value(0)) + '$'

        return '0'

    def total_auto(self):
        query = QtSql.QSqlQuery()
        query.exec("SELECT SUM(Balance) FROM expenses WHERE Category='Auto'")

        if query.next():
            return str(query.value(0)) + '$'

        return '0'

    def total_entertainment(self):
        query = QtSql.QSqlQuery()
        query.exec("SELECT SUM(Balance) FROM expenses WHERE Category='Entertainment'")

        if query.next():
            return str(query.value(0)) + '$'

        return '0'

    def total_other(self):
        query = QtSql.QSqlQuery()
        query.exec("SELECT SUM(Balance) FROM expenses WHERE Category='Other'")

        if query.next():
            return str(query.value(0)) + '$'

        return '0'
