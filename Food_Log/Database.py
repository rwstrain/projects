# @author: Wade Strain
# code for the database

import datetime
import mysql.connector as mc

DAY = datetime.datetime.now()

# creates user database if it hasn't been already
class userDatabase():

    def __init__(self, password):
        self.udb = mc.connect(
            host = 'localhost',
            user = 'root',
            passwd = password
        )
        print('connected to database!')
        self.ucursor = self.udb.cursor()
        self.createDatabase()
        self.createTable()

    def createDatabase(self):
        self.ucursor.execute('CREATE DATABASE IF NOT EXISTS usersdb')
        self.udb.commit()
        print('created usersdb database')

        #debugging
        self.ucursor.execute('SHOW DATABASES')
        for x in self.ucursor:
            print(x)

    def createTable(self):
        self.ucursor.execute('USE usersdb')
        self.ucursor.execute('''CREATE TABLE IF NOT EXISTS users (
                                id INT AUTO_INCREMENT PRIMARY KEY,
                                username VARCHAR(255),
                                password VARCHAR(255))''')
        self.udb.commit()
        print('created users table')

        #debugging
        self.ucursor.execute('SHOW TABLES')
        for x in self.ucursor:
            print(x)

    def close(self):
        self.ucursor.close()
        self.udb.close()
        print('closed usersdb database')

# creates foodlogdb database and Food_Entry table if it hasn't already
class foodDatabase():

    def __init__(self, password):
        self.fdb = mc.connect(
            host = 'localhost',
            user = 'root',
            passwd = password
        )
        print('connected to database!')
        self.fcursor = self.fdb.cursor()
        self.createDatabase()
        self.createTable()

    def createDatabase(self):
        self.fcursor.execute('CREATE DATABASE IF NOT EXISTS foodlogdb')
        self.fdb.commit()
        print('created foodlogdb database')

        #debugging
        self.fcursor.execute('SHOW DATABASES')
        for x in self.fcursor:
            print(x)

    def createTable(self):
        self.fcursor.execute('USE foodlogdb')
        self.fcursor.execute('''CREATE TABLE IF NOT EXISTS Food_Entries (
                                id INT AUTO_INCREMENT PRIMARY KEY,
                                user VARCHAR(255),
                                date VARCHAR(255),
                                name VARCHAR(255),
                                calories INT,
                                protein INT,
                                fat INT)''')
        self.fdb.commit()
        print('created Food_Entries table')

        #debugging
        self.fcursor.execute('SHOW TABLES')
        for x in self.fcursor:
            print(x)

    def close(self):
        self.fcursor.close()
        self.fdb.close()
        print('closed foodlogdb database')

class Database():

    # connects to database and sets cursor
    def __init__(self, user, password, database):
        self.db = mc.connect(
            host = 'localhost',
            user = user,
            passwd = password,
            database = database
        )
        self.cursor = self.db.cursor()
        print('connected to ' + database + ' database!')

    # checks if username is available
    # adds username and password to the users table
    def createUser(self, username, password):
        # check if username taken
        self.cursor.execute('SELECT COUNT(1) FROM users WHERE username = %s', (username,))
        if(self.cursor.fetchone()[0]):
            print('username not available')
            return False
        else:
            sql = ('INSERT INTO users (username, password) VALUES (%s, %s)')
            val = (username, password)

            self.cursor.execute(sql, val)
            self.db.commit()
            print('inserted ' + username + ' into users table')

            print('********* users in table **********')
            self.cursor.execute('SELECT * FROM users')
            data = self.cursor.fetchall()
            for x in data:
                print(x)

            return True

    # checks if user is in the users table
    # entry = [username, password]
    def isInUserTable(self, entry):
        print('checking if user is in table...')
        self.cursor.execute('''SELECT COUNT(1) FROM users WHERE username = %s AND
                            password = %s''', (entry[0], entry[1]))
        if(self.cursor.fetchone()[0]):
            print('in table')
            return True
        else:
            print('not in table')
            return False

    # inserts food data into Food_Entries table
    # entry = [user, date, name, calories, protein, fat]
    def insertEntry(self, entry):
        sql = ('''INSERT INTO Food_Entries (user, date, name, calories, protein, fat)
                  VALUES (%s, %s, %s, %s, %s, %s)''')
        val = (entry[0], entry[1], entry[2], entry[3], entry[4], entry[5])

        self.cursor.execute(sql, val)
        self.db.commit()

        print('inserted ' + str(entry) + ' into Food_Entry table')
        print('********* food entries **********')
        self.cursor.execute('SELECT * FROM Food_Entries')
        data = self.cursor.fetchall()
        for x in data:
            print(x)

    def deleteLastEntries(self, table, ids):
        self.cursor.execute('SELECT * FROM ' + table)
        self.cursor.fetchall()
        num_of_entries = self.cursor.rowcount

        if(ids > num_of_entries):
            print('error: not enough entries, there are only %d entries', num_of_entries)
            return

        for id in range(num_of_entries + 1 - ids, num_of_entries + 1):
            self.cursor.execute('DELETE FROM ' + table + ' WHERE id = ' + str(ids))
            self.db.commit()

        print('deleted entries from ' + table)

    def getTable(self, user):
        print('retrieving table...')
        self.cursor.execute('''SELECT date, name, calories, protein, fat FROM
                               Food_Entries WHERE user = %s''', (user, ))
        data = self.cursor.fetchall()
        return data

    def close(self):
        self.cursor.close()
        self.db.close()
        print('closed database')

# # for debugging
# if __name__ == '__main__':
