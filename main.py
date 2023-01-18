import sys

from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6 import QtWidgets
from PySide6.QtSql import QSqlTableModel

from ui_main import Ui_MainWindow
from connection import Data
from new_transaction import Ui_Dialog


class ExpenseTracker(QMainWindow):
    def __init__(self):
        super(ExpenseTracker, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.conn = Data()
        self.view_data()
        self.ui.btn_new_transaction.clicked.connect(self.open_new_transaction_window)
        self.ui.current_balance.setText(self.conn.total_balance())

    def view_data(self):
        self.model = QSqlTableModel(self)
        self.model.setTable('expenses')
        self.model.select()
        self.ui.tableView.setModel(self.model)

    def open_new_transaction_window(self):
        self.window = QtWidgets.QDialog()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self.window)
        self.window.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ExpenseTracker()
    window.show()

    sys.exit(app.exec())
