from data.storage import DatabaseManager
db = DatabaseManager()

users = [u[0] for u in db.fetchall('SELECT cid FROM users;')]

db.query('ALTER TABLE users ADD COLUMN settings TEXT DEFAULT "{{}}"')

for cid in users:
    db.setUserSettings(cid, {'renews':{'09:00':0, '16:00':0}})