import sqlite3 as lite
import config
import logging

language_suffixes = ['phrase_arm','phrase_rus','phrase_eng']

def log_queries(query):
    #if query.startswith(("INSERT", "UPDATE", "DELETE", "insert", "update", "delete")):
    logging.debug('SQL: '+query)
    

class DatabaseManager(object):
    def __init__(self):
        self.conn = lite.connect(config.DB_PATH)
        self.conn.execute('pragma foreign_keys = on')
        self.conn.commit()
        
        self.conn.set_trace_callback(log_queries)

        self.cur = self.conn.cursor()
        self.create_tables()

    def userExists(self, cid: int):
        return self.fetchone('SELECT count(cid) > 0 FROM users where cid=?;',(cid,))[0]

    def getUserLang(self, cid: int):
        return self.fetchone('SELECT preferred_language FROM users WHERE cid=?;',(cid,))[0]
    
    def setUserLang(self, cid: int, lang: int):
        self.query('UPDATE users SET preferred_language=? WHERE cid=?;',(lang,cid))

    def getUserName(self, cid):
        name = self.fetchone('SELECT name FROM users WHERE cid=?',(cid,))
        if name:
            return name[0]
        else:
            return 'Anon'
    
    def getUserSubscription(self, cid):
        return self.fetchone('SELECT subscription FROM users WHERE cid=?',(cid,))[0]
        
    def getState(self, cid: int):
        state_id = self.fetchone('SELECT state_id FROM users WHERE cid = ?;',(cid,))[0]
        return state_id

    def setState(self, cid: int, state_id : int):
        self.query('UPDATE users SET state_id = ? WHERE cid=?;',(state_id,cid))

    def create_tables(self):
        self.query('''CREATE TABLE IF NOT EXISTS users
                   (cid INTEGER PRIMARY KEY, name TEXT, phone_number TEXT, email TEXT, password TEXT, token TEXT, joining_date DATETIME, account_state INTEGER,
                    state_id INTEGER, preferred_language INTEGER, subscription INTEGER DEFAULT 0, subscription_end DATETIME DEFAULT '2025-01-01 00:00:00',
                      next_payment_amount INTEGER DEFAULT 0, referral_id TEXT DEFAULT '')''')

    def query(self, arg, values=None):
        if values == None:
            self.cur.execute(arg)
        else:
            self.cur.execute(arg, values)
        self.conn.commit()

    def fetchone(self, arg, values=None):
        if values == None:
            self.cur.execute(arg)
        else:
            self.cur.execute(arg, values)
        return self.cur.fetchone()

    def fetchall(self, arg, values=None):
        if values == None:
            self.cur.execute(arg)
        else:
            self.cur.execute(arg, values)
        return self.cur.fetchall()

    def __del__(self):
        self.conn.close()