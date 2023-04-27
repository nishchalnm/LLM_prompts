import sqlite3
# import hashlib
import bcrypt

   
conn = sqlite3.connect('test.db')
#print("Opened database successfully")

curr = conn.cursor()
create_table_query = """create table if not exists user_creds(name text, email text, password text)"""
curr.execute(create_table_query)

def encrypt_password(password):
   salt = b"$2b$12$H9FRRo4zNBLmVFEK8855qq"
   password_text_encoded = password.encode('UTF-8')
   pwd_hash = bcrypt.hashpw(password_text_encoded, salt)
   return pwd_hash

def get_password(username):
   conn = sqlite3.connect('test.db')
   curr = conn.cursor()
   qr = f"select password from user_creds where name = '{username}'"
   curr.execute(qr)
   password = None
   for row in curr:
      password = row[0]
   #print("password", password)
   conn.commit()
   conn.close()
   return password

def get_username(user_name):
   user_flag = 1
   try:
      select_qr = f"select name from user_creds where name='{user_name}'"
      conn = sqlite3.connect('test.db')
      curr = conn.cursor()
      curr.execute(select_qr)
      rows = curr.fetchall()
      if len(rows) == 0:
         user_flag = 0
         conn.commit()
         conn.close()
   except Exception as e:
      print(e)
   return user_flag

def insert_into_user_table(name, email, password):
   # update_status = 0
   password_hash = encrypt_password(password)
   password_hash = password_hash.decode('UTF-8')
   insert_qr = f"insert into user_creds(name, email, password) values ('{name}', '{email}', '{password_hash}')"
   #print(insert_qr)
   #insert_qr = """insert into user_creds(name, email, password) values ('vichitra', 'vichitrak93@gmail.com', 'my_password')"""
   user_flag = get_username(name)
   print(user_flag)
   if user_flag == 0:
      try:
         conn = sqlite3.connect('test.db')
         curr = conn.cursor()
         curr.execute(insert_qr)
         conn.commit()
         conn.close()
         update_status = 1
      except Exception as e:
         print(e)
         
   return user_flag

def table_lookup():
   conn = sqlite3.connect('test.db')
   curr = conn.cursor()
   select_qr = """select * from user_creds"""
   curr.execute(select_qr)
   for row in curr:
      print("name = ", row[0])
      print("email = ", row[1])
      print("password = ", row[2], "\n")
   conn.commit()
   conn.close()

def table_cleanup(cond):
   conn = sqlite3.connect('test.db')
   curr = conn.cursor()
   del_qr = f"delete from user_creds where name='{cond}'"
   curr.execute(del_qr)
   conn.commit()
   conn.close()

#get_password('admin')
#table_lookup()
#table_cleanup('vkrr')
#insert_into_user_table('admin', 'admin@reddit.com', 'password')
#table_lookup()