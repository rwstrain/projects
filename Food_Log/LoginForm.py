# @author: Wade Strain
# Login form gui

import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QDialog, QLabel, QLineEdit,
                             QPushButton, QFormLayout, QMessageBox)
from PyQt5.QtCore import pyqtSignal

from Database import Database

class LoginForm(QDialog):

    switch_window = pyqtSignal(str)

    def __init__(self, password):
        super(LoginForm, self).__init__()

        self.username = QLineEdit(self)
        self.password = QLineEdit(self)
        login_btn = QPushButton('Login')
        create_accnt_btn = QPushButton('Create Account')

        mainlayout = QFormLayout()
        mainlayout.addRow(QLabel('Username:'), self.username)
        mainlayout.addRow(QLabel('Password:'), self.password)
        mainlayout.addRow(create_accnt_btn)
        mainlayout.addRow(login_btn)
        self.setLayout(mainlayout)

        login_btn.clicked.connect(self.submit)
        create_accnt_btn.clicked.connect(self.createAccount)
        root_passwd = password
        self.user_database = Database('root', root_passwd, 'usersdb')

    def submit(self):
        print('Login button clicked!')
        un = self.username.text()
        pw = self.password.text()
        entry = [str(un), str(pw)]

        if(un == '' or pw == ''):
            print('need a username and password')
        elif(self.user_database.isInUserTable(entry)):
            self.user_database.close()
            self.switch_window.emit(str(un))
        else:
            print('incorrect username or password')

    def createAccount(self):
        print('Create Account button clicked!')
        un = self.username.text()
        pw = self.password.text()

        if(self.user_database.createUser(str(un), str(pw))):
            print('created user')
            self.user_database.close()
            self.switch_window.emit(str(un))
        else:
            print('pick different username')

# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     ex = LoginForm()
#     sys.exit(app.exec_())
