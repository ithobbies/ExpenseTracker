# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_main.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QHeaderView,
    QLabel, QMainWindow, QPushButton, QSizePolicy,
    QTableView, QVBoxLayout, QWidget)
import res

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(803, 673)
        MainWindow.setMinimumSize(QSize(800, 600))
        font = QFont()
        font.setFamilies([u"Noto Sans SC"])
        MainWindow.setFont(font)
        MainWindow.setStyleSheet(u"font-family: Noto Sans SC;\n"
"background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0, stop:0 rgba(81, 0, 135, 255), stop:0.427447 rgba(41, 61, 132, 235), stop:1 rgba(155, 79, 165, 255));\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.balances_frame = QFrame(self.centralwidget)
        self.balances_frame.setObjectName(u"balances_frame")
        self.balances_frame.setStyleSheet(u"background-color: rgba(255, 255, 255, 30); \n"
"border: 1px solid rgba(255,255,255,40);\n"
"border-radius: 7px;")
        self.balances_frame.setFrameShape(QFrame.NoFrame)
        self.balances_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_21 = QVBoxLayout(self.balances_frame)
        self.verticalLayout_21.setSpacing(0)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.verticalLayout_21.setContentsMargins(12, 12, 12, 12)
        self.lbl_current_balance = QLabel(self.balances_frame)
        self.lbl_current_balance.setObjectName(u"lbl_current_balance")
        font1 = QFont()
        font1.setFamilies([u"Noto Sans SC"])
        font1.setPointSize(20)
        font1.setBold(True)
        self.lbl_current_balance.setFont(font1)
        self.lbl_current_balance.setStyleSheet(u"color: white;\n"
"font-weight: bold;\n"
"font-size: 20pt;\n"
"background-color: none;\n"
"border: none;")

        self.verticalLayout_21.addWidget(self.lbl_current_balance)

        self.current_balance = QLabel(self.balances_frame)
        self.current_balance.setObjectName(u"current_balance")
        font2 = QFont()
        font2.setFamilies([u"Noto Sans SC"])
        font2.setPointSize(30)
        font2.setBold(False)
        font2.setItalic(False)
        font2.setKerning(True)
        self.current_balance.setFont(font2)
        self.current_balance.setStyleSheet(u"color: white;\n"
"font-size: 30pt;\n"
"background-color: none;\n"
"border: none;")
        self.current_balance.setLineWidth(0)

        self.verticalLayout_21.addWidget(self.current_balance)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.lbl_arrow_top = QLabel(self.balances_frame)
        self.lbl_arrow_top.setObjectName(u"lbl_arrow_top")
        self.lbl_arrow_top.setMaximumSize(QSize(24, 16777215))
        font3 = QFont()
        font3.setFamilies([u"Noto Sans SC"])
        font3.setPointSize(16)
        font3.setBold(True)
        self.lbl_arrow_top.setFont(font3)
        self.lbl_arrow_top.setStyleSheet(u"color: white;\n"
"font-weight: bold;\n"
"font-size: 16pt;\n"
"background-color: none;\n"
"border: none;\n"
"padding-top: 10px;")
        self.lbl_arrow_top.setPixmap(QPixmap(u":/icons/icons/north_west_white_24dp.svg"))

        self.horizontalLayout_9.addWidget(self.lbl_arrow_top)

        self.lbl_income = QLabel(self.balances_frame)
        self.lbl_income.setObjectName(u"lbl_income")
        self.lbl_income.setFont(font3)
        self.lbl_income.setStyleSheet(u"color: white;\n"
"font-weight: bold;\n"
"font-size: 16pt;\n"
"background-color: none;\n"
"border: none;\n"
"padding-top: 10px;")

        self.horizontalLayout_9.addWidget(self.lbl_income)


        self.verticalLayout_21.addLayout(self.horizontalLayout_9)

        self.income_balance = QLabel(self.balances_frame)
        self.income_balance.setObjectName(u"income_balance")
        font4 = QFont()
        font4.setFamilies([u"Noto Sans SC"])
        font4.setPointSize(20)
        font4.setBold(False)
        font4.setItalic(False)
        font4.setKerning(True)
        self.income_balance.setFont(font4)
        self.income_balance.setStyleSheet(u"color: white;\n"
"font-size: 20pt;\n"
"background-color: none;\n"
"border: none;")
        self.income_balance.setLineWidth(0)

        self.verticalLayout_21.addWidget(self.income_balance)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.lbl_arrow_bottom = QLabel(self.balances_frame)
        self.lbl_arrow_bottom.setObjectName(u"lbl_arrow_bottom")
        self.lbl_arrow_bottom.setMaximumSize(QSize(24, 16777215))
        self.lbl_arrow_bottom.setFont(font3)
        self.lbl_arrow_bottom.setStyleSheet(u"color: white;\n"
"font-weight: bold;\n"
"font-size: 16pt;\n"
"background-color: none;\n"
"border: none;\n"
"padding-top: 10px;")
        self.lbl_arrow_bottom.setPixmap(QPixmap(u":/icons/icons/call_received_white_24dp.svg"))

        self.horizontalLayout_10.addWidget(self.lbl_arrow_bottom)

        self.lbl_outcome = QLabel(self.balances_frame)
        self.lbl_outcome.setObjectName(u"lbl_outcome")
        self.lbl_outcome.setFont(font3)
        self.lbl_outcome.setStyleSheet(u"color: white;\n"
"font-weight: bold;\n"
"font-size: 16pt;\n"
"background-color: none;\n"
"border: none;\n"
"padding-top: 10px;")

        self.horizontalLayout_10.addWidget(self.lbl_outcome)


        self.verticalLayout_21.addLayout(self.horizontalLayout_10)

        self.outcome_balance = QLabel(self.balances_frame)
        self.outcome_balance.setObjectName(u"outcome_balance")
        self.outcome_balance.setFont(font4)
        self.outcome_balance.setStyleSheet(u"color: white;\n"
"font-size: 20pt;\n"
"background-color: none;\n"
"border: none;")
        self.outcome_balance.setLineWidth(0)

        self.verticalLayout_21.addWidget(self.outcome_balance)


        self.horizontalLayout_2.addWidget(self.balances_frame)

        self.balances_frame_2 = QFrame(self.centralwidget)
        self.balances_frame_2.setObjectName(u"balances_frame_2")
        self.balances_frame_2.setStyleSheet(u"background-color: rgba(255, 255, 255, 30); \n"
"border: 1px solid rgba(255,255,255,40);\n"
"border-radius: 7px;")
        self.balances_frame_2.setFrameShape(QFrame.NoFrame)
        self.balances_frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_20 = QVBoxLayout(self.balances_frame_2)
        self.verticalLayout_20.setSpacing(0)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.verticalLayout_20.setContentsMargins(12, 12, 12, 12)
        self.lbl_expenses_categories = QLabel(self.balances_frame_2)
        self.lbl_expenses_categories.setObjectName(u"lbl_expenses_categories")
        self.lbl_expenses_categories.setFont(font1)
        self.lbl_expenses_categories.setStyleSheet(u"color: white;\n"
"font-weight: bold;\n"
"font-size: 20pt;\n"
"background-color: none;\n"
"border: none;")

        self.verticalLayout_20.addWidget(self.lbl_expenses_categories)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.icon_groceries = QLabel(self.balances_frame_2)
        self.icon_groceries.setObjectName(u"icon_groceries")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.icon_groceries.sizePolicy().hasHeightForWidth())
        self.icon_groceries.setSizePolicy(sizePolicy)
        self.icon_groceries.setMaximumSize(QSize(24, 16777215))
        font5 = QFont()
        font5.setFamilies([u"Noto Sans SC"])
        font5.setPointSize(14)
        font5.setBold(True)
        self.icon_groceries.setFont(font5)
        self.icon_groceries.setStyleSheet(u"color: white;\n"
"font-weight: bold;\n"
"font-size: 14pt;\n"
"background-color: none;\n"
"border: none;")
        self.icon_groceries.setPixmap(QPixmap(u":/icons/icons/local_grocery_store_white_24dp.svg"))

        self.horizontalLayout_3.addWidget(self.icon_groceries)

        self.lbl_groceries = QLabel(self.balances_frame_2)
        self.lbl_groceries.setObjectName(u"lbl_groceries")
        self.lbl_groceries.setFont(font5)
        self.lbl_groceries.setStyleSheet(u"color: white;\n"
"font-weight: bold;\n"
"font-size: 14pt;\n"
"background-color: none;\n"
"border: none;")

        self.horizontalLayout_3.addWidget(self.lbl_groceries)

        self.total_groceries = QLabel(self.balances_frame_2)
        self.total_groceries.setObjectName(u"total_groceries")
        font6 = QFont()
        font6.setFamilies([u"Noto Sans SC"])
        font6.setPointSize(16)
        font6.setBold(False)
        font6.setItalic(False)
        font6.setKerning(True)
        self.total_groceries.setFont(font6)
        self.total_groceries.setStyleSheet(u"color: white;\n"
"font-size: 16pt;\n"
"background-color: none;\n"
"border: none;")
        self.total_groceries.setLineWidth(0)

        self.horizontalLayout_3.addWidget(self.total_groceries)


        self.verticalLayout_20.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.icon_entertainment = QLabel(self.balances_frame_2)
        self.icon_entertainment.setObjectName(u"icon_entertainment")
        self.icon_entertainment.setMaximumSize(QSize(24, 16777215))
        self.icon_entertainment.setFont(font5)
        self.icon_entertainment.setStyleSheet(u"color: white;\n"
"font-weight: bold;\n"
"font-size: 14pt;\n"
"background-color: none;\n"
"border: none;")
        self.icon_entertainment.setPixmap(QPixmap(u":/icons/icons/sports_esports_white_24dp.svg"))

        self.horizontalLayout_4.addWidget(self.icon_entertainment)

        self.lbl_entertainment = QLabel(self.balances_frame_2)
        self.lbl_entertainment.setObjectName(u"lbl_entertainment")
        self.lbl_entertainment.setFont(font5)
        self.lbl_entertainment.setStyleSheet(u"color: white;\n"
"font-weight: bold;\n"
"font-size: 14pt;\n"
"background-color: none;\n"
"border: none;")

        self.horizontalLayout_4.addWidget(self.lbl_entertainment)

        self.total_entertainment = QLabel(self.balances_frame_2)
        self.total_entertainment.setObjectName(u"total_entertainment")
        self.total_entertainment.setFont(font6)
        self.total_entertainment.setStyleSheet(u"color: white;\n"
"font-size: 16pt;\n"
"background-color: none;\n"
"border: none;")
        self.total_entertainment.setLineWidth(0)

        self.horizontalLayout_4.addWidget(self.total_entertainment)


        self.verticalLayout_20.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.icon_auto = QLabel(self.balances_frame_2)
        self.icon_auto.setObjectName(u"icon_auto")
        self.icon_auto.setMaximumSize(QSize(24, 16777215))
        self.icon_auto.setFont(font5)
        self.icon_auto.setStyleSheet(u"color: white;\n"
"font-weight: bold;\n"
"font-size: 14pt;\n"
"background-color: none;\n"
"border: none;")
        self.icon_auto.setPixmap(QPixmap(u":/icons/icons/directions_car_white_24dp.svg"))

        self.horizontalLayout_5.addWidget(self.icon_auto)

        self.lbl_auto = QLabel(self.balances_frame_2)
        self.lbl_auto.setObjectName(u"lbl_auto")
        self.lbl_auto.setFont(font5)
        self.lbl_auto.setStyleSheet(u"color: white;\n"
"font-weight: bold;\n"
"font-size: 14pt;\n"
"background-color: none;\n"
"border: none;")

        self.horizontalLayout_5.addWidget(self.lbl_auto)

        self.total_auto = QLabel(self.balances_frame_2)
        self.total_auto.setObjectName(u"total_auto")
        self.total_auto.setFont(font6)
        self.total_auto.setStyleSheet(u"color: white;\n"
"font-size: 16pt;\n"
"background-color: none;\n"
"border: none;")
        self.total_auto.setLineWidth(0)

        self.horizontalLayout_5.addWidget(self.total_auto)


        self.verticalLayout_20.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.icon_other = QLabel(self.balances_frame_2)
        self.icon_other.setObjectName(u"icon_other")
        self.icon_other.setMaximumSize(QSize(24, 16777215))
        self.icon_other.setFont(font5)
        self.icon_other.setStyleSheet(u"color: white;\n"
"font-weight: bold;\n"
"font-size: 14pt;\n"
"background-color: none;\n"
"border: none;")
        self.icon_other.setPixmap(QPixmap(u":/icons/icons/list_white_24dp.svg"))

        self.horizontalLayout_6.addWidget(self.icon_other)

        self.lbl_other = QLabel(self.balances_frame_2)
        self.lbl_other.setObjectName(u"lbl_other")
        self.lbl_other.setFont(font5)
        self.lbl_other.setStyleSheet(u"color: white;\n"
"font-weight: bold;\n"
"font-size: 14pt;\n"
"background-color: none;\n"
"border: none;")

        self.horizontalLayout_6.addWidget(self.lbl_other)

        self.total_other = QLabel(self.balances_frame_2)
        self.total_other.setObjectName(u"total_other")
        self.total_other.setFont(font6)
        self.total_other.setStyleSheet(u"color: white;\n"
"font-size: 16pt;\n"
"background-color: none;\n"
"border: none;")
        self.total_other.setLineWidth(0)

        self.horizontalLayout_6.addWidget(self.total_other)


        self.verticalLayout_20.addLayout(self.horizontalLayout_6)


        self.horizontalLayout_2.addWidget(self.balances_frame_2)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.btn_frame = QFrame(self.centralwidget)
        self.btn_frame.setObjectName(u"btn_frame")
        self.btn_frame.setStyleSheet(u"background-color: transparent;")
        self.horizontalLayout = QHBoxLayout(self.btn_frame)
#ifndef Q_OS_MAC
        self.horizontalLayout.setSpacing(-1)
#endif
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.btn_new_transaction = QPushButton(self.btn_frame)
        self.btn_new_transaction.setObjectName(u"btn_new_transaction")
        self.btn_new_transaction.setMinimumSize(QSize(230, 50))
        font7 = QFont()
        font7.setFamilies([u"Noto Sans SC"])
        font7.setBold(True)
        self.btn_new_transaction.setFont(font7)
        self.btn_new_transaction.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"     background-color:rgba(255,255,255,30);\n"
"     border: 1px solid rgba(255,255,255,40);\n"
"     border-radius:7px;\n"
"width: 230;\n"
"height: 50;\n"
"}\n"
"QPushButton:hover{\n"
"background-color:rgba(255,255,255,30);\n"
"}\n"
"QPushButton:pressed{\n"
"background-color:rgba(255,255,255,70);\n"
"}")
        icon = QIcon()
        icon.addFile(u":/icons/icons/post_add_white_24dp.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_new_transaction.setIcon(icon)
        self.btn_new_transaction.setIconSize(QSize(24, 24))

        self.horizontalLayout.addWidget(self.btn_new_transaction)

        self.btn_delete_transaction = QPushButton(self.btn_frame)
        self.btn_delete_transaction.setObjectName(u"btn_delete_transaction")
        self.btn_delete_transaction.setMinimumSize(QSize(230, 50))
        self.btn_delete_transaction.setFont(font7)
        self.btn_delete_transaction.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"     background-color:rgba(255,255,255,30);\n"
"     border: 1px solid rgba(255,255,255,40);\n"
"     border-radius:7px;\n"
"width: 230;\n"
"height: 50;\n"
"}\n"
"QPushButton:hover{\n"
"background-color:rgba(255,255,255,30);\n"
"}\n"
"QPushButton:pressed{\n"
"background-color:rgba(255,255,255,70);\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/delete_white_24dp.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_delete_transaction.setIcon(icon1)
        self.btn_delete_transaction.setIconSize(QSize(24, 24))

        self.horizontalLayout.addWidget(self.btn_delete_transaction)

        self.btn_edit_transaction = QPushButton(self.btn_frame)
        self.btn_edit_transaction.setObjectName(u"btn_edit_transaction")
        self.btn_edit_transaction.setMinimumSize(QSize(230, 50))
        self.btn_edit_transaction.setFont(font7)
        self.btn_edit_transaction.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"     background-color:rgba(255,255,255,30);\n"
"     border: 1px solid rgba(255,255,255,40);\n"
"     border-radius:7px;\n"
"width: 230;\n"
"height: 50;\n"
"}\n"
"QPushButton:hover{\n"
"background-color:rgba(255,255,255,30);\n"
"}\n"
"QPushButton:pressed{\n"
"background-color:rgba(255,255,255,70);\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u":/icons/icons/edit_white_24dp.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_edit_transaction.setIcon(icon2)
        self.btn_edit_transaction.setIconSize(QSize(24, 24))

        self.horizontalLayout.addWidget(self.btn_edit_transaction)


        self.verticalLayout_2.addWidget(self.btn_frame)

        self.tableView = QTableView(self.centralwidget)
        self.tableView.setObjectName(u"tableView")
        self.tableView.setStyleSheet(u"QTableView {\n"
"background-color: rgba(255, 255, 255, 30); \n"
"border: 1px solid rgba(255,255,255,40);\n"
"border-bottom-right-radius: 7px; \n"
"border-bottom-left-radius: 7px; \n"
"color: white;\n"
"}\n"
"\n"
"QHeaderView::section {\n"
"background-color: rgb(53, 53, 53);\n"
"color: white;\n"
"border: none;\n"
"height: 50px;\n"
"font-size: 16pt;\n"
"}\n"
"\n"
"QTableView::item {\n"
"    border-style: none;\n"
"    border-bottom: 1px solid rgba(255,255,255,50);\n"
"}\n"
"\n"
"QTableView::item:selected{\n"
"	border: none;\n"
"	color: rgb(255, 255, 255);\n"
"    background-color: rgba(255, 255, 255, 50);\n"
"}\n"
"")
        self.tableView.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.tableView.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.tableView.setTextElideMode(Qt.ElideRight)
        self.tableView.setShowGrid(False)
        self.tableView.setSortingEnabled(True)
        self.tableView.horizontalHeader().setDefaultSectionSize(135)
        self.tableView.verticalHeader().setVisible(False)

        self.verticalLayout_2.addWidget(self.tableView)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.lbl_current_balance.setText(QCoreApplication.translate("MainWindow", u"Current Balance", None))
        self.current_balance.setText(QCoreApplication.translate("MainWindow", u"$3235,50", None))
        self.lbl_arrow_top.setText("")
        self.lbl_income.setText(QCoreApplication.translate("MainWindow", u"Income", None))
        self.income_balance.setText(QCoreApplication.translate("MainWindow", u"$3235,50", None))
        self.lbl_arrow_bottom.setText("")
        self.lbl_outcome.setText(QCoreApplication.translate("MainWindow", u"Outcome", None))
        self.outcome_balance.setText(QCoreApplication.translate("MainWindow", u"$3235,50", None))
        self.lbl_expenses_categories.setText(QCoreApplication.translate("MainWindow", u"Expenses categories", None))
        self.icon_groceries.setText("")
        self.lbl_groceries.setText(QCoreApplication.translate("MainWindow", u"Groceries", None))
        self.total_groceries.setText(QCoreApplication.translate("MainWindow", u"$3235,50", None))
        self.icon_entertainment.setText("")
        self.lbl_entertainment.setText(QCoreApplication.translate("MainWindow", u"Entertainment", None))
        self.total_entertainment.setText(QCoreApplication.translate("MainWindow", u"$3235,50", None))
        self.icon_auto.setText("")
        self.lbl_auto.setText(QCoreApplication.translate("MainWindow", u"Auto", None))
        self.total_auto.setText(QCoreApplication.translate("MainWindow", u"$3235,50", None))
        self.icon_other.setText("")
        self.lbl_other.setText(QCoreApplication.translate("MainWindow", u"Other", None))
        self.total_other.setText(QCoreApplication.translate("MainWindow", u"$3235,50", None))
        self.btn_new_transaction.setText(QCoreApplication.translate("MainWindow", u"New transaction", None))
        self.btn_delete_transaction.setText(QCoreApplication.translate("MainWindow", u"Delete transaction", None))
        self.btn_edit_transaction.setText(QCoreApplication.translate("MainWindow", u"Edit transaction", None))
    # retranslateUi

