import sqlite3
import os

def toDict(t):
    transaction = {'rowid':t[0], 'item_num':t[1], 'amount':t[2], 'category':t[3], 'date':t[4],'description':t[5]}
    return transaction

class Transaction():
    #---------------------------------methods from Trista -----------------------------------
    def __init__(self):
        self.runQuery('''CREATE TABLE IF NOT EXISTS transactions
                    (item_num int, amount int, category text, date int, description text)''',())
      
    def add(self, item):
        return self.runQuery("INSERT INTO transactions VALUES(?,?,?,?,?)",(item['item_num'],item['amount'],item['category'],item['date'],item['description']))
     
    def showTransactions(self):
        return self.runQuery("SELECT rowid,* from transactions",())
    
    def delete(self, item):
        return self.runQuery("DELETE FROM transactions WHERE item_num=(?)",(item['item_num'],))
    #-----------------------------end of methods from Trista -----------------------------------
    
    def runQuery(self,query,tuple):
        con= sqlite3.connect(os.getenv('HOME')+'/Desktop/cs103aSpr23Team22/PA03/tracker.db')
        cur = con.cursor() 
        cur.execute(query,tuple)
        tuples = cur.fetchall()
        con.commit()
        con.close()
        return [toDict(t) for t in tuples]
