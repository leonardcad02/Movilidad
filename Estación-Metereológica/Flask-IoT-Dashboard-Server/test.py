from passlib.hash import sha512_crypt as sha
password = sha.hash("123456")
print(password)
from database import db

mydb = db('root', 'localhost', '', 'movilidad_db')
query = "update users set password = '{}' where username = 'administrador'".format(password)

mydb.cursor.execute(query)
mydb.db.commit()

