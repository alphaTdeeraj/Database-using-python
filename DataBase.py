import sqlite3



class Database:

    def __init__(self, name=None):
        self.db = self.createDatabase(name)
        self.c = self.db.cursor()
        self.createTable()
    


    def createDatabase(self, name):
        if(name):
            return sqlite3.connect(f'{name}.db')
        else:
            return sqlite3.connect(":memory:")
    

    def createTable(self):
        try:
            self.c.execute("CREATE TABLE Users (email text, password text)")
        except:
            pass
    
    def insertUser(self,email, password ):
        try:
            self.c.execute(f"INSERT INTO Users VALUES (?, ?)", (email, password))
            #missing important step
        except:
            pass
    

    def getUser(self, email):
        user = None
        try:
            user = self.c.execute("SELECT * FROM Users WHERE email=?", (email,)).fetchone()
        except:
            pass
        return user
