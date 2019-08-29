# @author: Wade Strain
# main window for food log

import sys
import datetime
from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import (QMainWindow, QApplication, QWidget, QLabel,
                            QLineEdit, QPushButton, QHBoxLayout, QVBoxLayout,
                            QFormLayout, QTableWidget, QTableWidgetItem,
                            QHeaderView)

TODAY = datetime.datetime.now()

from Database import Database

class MainWindow(QWidget):

    def __init__(self, user, root_password):
        super().__init__()

        self.setMinimumSize(QSize(500, 500))
        self.setWindowTitle("Food Log")

        # connects to foodlogdb
        self.database = Database('root', root_password, 'foodlogdb')
        # sets user of the foodlogdb
        self.user = user

        # ----------- widget initializaitons -------------
        self.food = QLineEdit(self)
        self.calories = QLineEdit(self)
        self.protein = QLineEdit(self)
        self.fat = QLineEdit(self)

        add_btn = QPushButton('Add')
        cancel_btn = QPushButton('Cancel')

        self.table = QTableWidget()
        self.tableInitialization()

        # ------------ layout -----------------------------
        btn_hbox = QHBoxLayout()
        btn_hbox.addStretch(1)
        btn_hbox.addWidget(add_btn)
        btn_hbox.addWidget(cancel_btn)

        data_form = QFormLayout()
        data_form.addRow(QLabel('Food:'), self.food)
        data_form.addRow(QLabel('Calories:'), self.calories)
        data_form.addRow(QLabel('Protein:'), self.protein)
        data_form.addRow(QLabel('Fat:'), self.fat)

        vbox = QVBoxLayout()
        vbox.addLayout(data_form)
        vbox.addLayout(btn_hbox)
        vbox.addWidget(self.table)
        vbox.addStretch(1)

        self.setLayout(vbox)

        add_btn.clicked.connect(self.add)
        cancel_btn.clicked.connect(self.cancel)

        self.show()

    # adds food entry data to the foodlogdb when user clicks add button
    def add(self):
        food = self.food.text()
        calories = self.calories.text()
        protein = self.protein.text()
        fat = self.fat.text()
        entry = [self.user, str(TODAY), str(food), str(calories), str(protein), str(fat)]

        self.database.insertEntry(entry)
        # adds row to table instead of accessing database when user adds entry
        entry = [str(TODAY), str(food), str(calories), str(protein), str(fat)]
        self.addRow(entry)

    # clears the text edit boxes when user clicks cancel button
    def cancel(self):
        print('clicked cancel button')
        self.food.clear()
        self.calories.clear()
        self.protein.clear()
        self.fat.clear()

    def tableInitialization(self):
        self.table.setColumnCount(5)
        self.table.setHorizontalHeaderLabels(['Date', 'Food', 'Calories (g)', 'Protein (g)', 'Fat (g)'])
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        data = self.database.getTable(self.user)
        if(data == None):
            print('nothing in the table')
        else:
            for r in data:
                self.addRow(r)

    def addRow(self, entry):
        print('adding row to gui table...')
        rowPosition = self.table.rowCount()
        self.table.insertRow(rowPosition)
        for i in range(len(entry)):
            self.table.setItem(rowPosition, i, QTableWidgetItem(str(entry[i])))
#
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     ex = MainWindow()
#     sys.exit(app.exec_())
