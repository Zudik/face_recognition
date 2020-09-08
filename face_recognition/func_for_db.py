import sqlite3

conn = sqlite3.connect('example.db')
c = conn.cursor()
c.execute("""
	CREATE TABLE if not exists persons (id INTEGER NOT NULL PRIMARY KEY,
					     name varchar(30) NOT NULL)""")
conn.commit()
conn.close()

def get_name_person(uid):
	conn = sqlite3.connect('example.db')
	c = conn.cursor()
	command_get_name = "SELECT name from persons WHERE id = ?"
	name_person_cursor = c.execute(command_get_name, str(uid))
	name_person = name_person_cursor.fetchone()
	conn.close()
	return name_person
	
def update_db(uid, person_name):
	conn = sqlite3.connect('example.db')
	c = conn.cursor()
	command_update_insert = "INSERT OR REPLACE INTO persons(id, name) VALUES(?,?)"
	c.execute(command_update_insert, (uid, person_name))
	conn.commit()
	conn.close()

