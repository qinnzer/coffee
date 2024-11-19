import sys

from PyQt6.QtWidgets import QWidget, QTableWidget, QApplication, QTableWidgetItem
from PyQt6 import uic

import sqlite3


class CoffeeApp(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("main.ui", self)
        self.initTable()

    def initTable(self):
        self.tableWidget.setColumnCount(6)
        self.tableWidget.setHorizontalHeaderLabels(
            ["Сорт", "Обжарка", "Молотый/В зернах", "Вкус", "Цена", "Объем упаковки"])

        with sqlite3.connect("coffee.sqlite") as db:
            cur = db.cursor()
            data = cur.execute("""
            SELECT * FROM Coffee
            """).fetchall()

        self.tableWidget.setRowCount(len(data))

        for i in range(len(data)):
            self.tableWidget.setRowHeight(i, 75)
            self.tableWidget.setItem(i, 0, QTableWidgetItem(data[i][1]))
            self.tableWidget.setItem(i, 1, QTableWidgetItem(data[i][2]))
            self.tableWidget.setItem(i, 2, QTableWidgetItem(data[i][3]))
            self.tableWidget.setItem(i, 3, QTableWidgetItem(data[i][4]))
            self.tableWidget.setItem(i, 4, QTableWidgetItem(str(data[i][5])))
            self.tableWidget.setItem(i, 5, QTableWidgetItem(data[i][6]))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    coffee_app = CoffeeApp()
    coffee_app.show()
    sys.exit(app.exec())
