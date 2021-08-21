import mysql.connector

class db:
    
    def __init__(self, user, host, password, database):
        try:
            self.db = mysql.connector.connect(user=user, host=host, password=password, database=database)
            self.cursor = self.db.cursor()
            print ('[result] Database connected!')
            
        except Exception as e:
            print ('[error] error connecting database!')
            print(e)

    def user(self, username, api):
        try:
            query = "select * from users where username='{}' and api_key='{}'".format(username, api)
            self.cursor.execute(query)
            output = self.cursor.fetchall()
            return output[0]
        except Exception as e:
            print('[error] ' + e)

    def get_apikeys(self):
        query = 'select api_key from users'
        self.cursor.execute(query)
        output = self.cursor.fetchall()
        dummy = []
        for api in output:
            dummy.append(api[0])
        return dummy

    def add_user(self, username, password, first_name, last_name, email, api_key):
        
        try:
            query = "insert into users (username, password, first_name, last_name, email, last_login, api_key) values ('{0}', '{1}', '{2}', '{3}', '{4}', now(), '{5}');".format(username, password, first_name, last_name, email, api_key)
            # print(query)
            self.cursor.execute(query)
            self.db.commit()
            return "success"
        except Exception as e:
            print( e)
    
    def update_values(self, apikey, fieldname, deviceID, latitud ,longitud, altitud, velocidad, personaone, personatwo, personathree, personafour):
        try:
            self.cursor.execute("select api_key from users;")
            output = self.cursor.fetchall()
            dummy = []
            for i in output:
                dummy.append(i[0])
            if apikey in dummy:
                print(fieldname)
                print(deviceID)
                query = 'insert into bus (deviceID,latitud ,longitud, altitud, velocidad, personaone, personatwo, personatree, personafour, date_time) values("{1}", {2}, {3}, {4}, {5},{6},{7},{8},{9},now());'.format(fieldname, deviceID, latitud, longitud, altitud, velocidad, personaone, personatwo, personathree, personafour)
                print(query)
                self.cursor.execute(query)
                self.db.commit()

                query = 'update Node set latitud={0}, longitud={1}, altitud ={2}, velocidad={3}, personaone={4}, personatwo={5}, personatree={6}, personafour={7} where deviceID="{8}";'.format(latitud, longitud, altitud, velocidad, personaone, personatwo, personathree, personafour, deviceID)
                self.cursor.execute(query)
                self.db.commit()
                #print(query)
                return True
            else:
                print("not available")

        except Exception as e:
            print("[ERROR!]")
            print(e)
#test side
#mydb = db('root', 'localhost','', 'movilidad_db')

#mydb.update_values("movilidad", "MET12012", 10, 10, 10, 10, 34, 45, 67, 89, 56)