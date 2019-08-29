# @author: Wade Strain
# controls the different GUI windows for the food log


import sys

from PyQt5.QtWidgets import QApplication

from LoginForm import LoginForm
from MainWindow import MainWindow
from Database import userDatabase, foodDatabase

class GUI_Manager():

    # open and create userdb and foodlogdb (databases)
    # and users and Food_Entries tables
    def __init__(self):
        # asks user for the root account password in terminal for mysql server
        self.__password = input('root account password: ')
        self.user_database = userDatabase(self.__password)
        self.user_database.close()
        self.food_database = foodDatabase(self.__password)
        self.food_database.close()

    def open_login(self):
        self.login = LoginForm(self.__password)
        self.login.switch_window.connect(self.open_main)
        self.login.show()

    def open_main(self, user):
        self.main = MainWindow(user, self.__password)
        self.login.close()
        self.main.show()

def main():
    app = QApplication(sys.argv)
    manager = GUI_Manager()
    manager.open_login()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
