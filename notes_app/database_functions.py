import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="qweasdzxc",
 database="test_task"
)

def get_all_posts():
	mycursor = mydb.cursor(dictionary=True)
	mycursor.execute("SELECT * FROM notes WHERE 1")
	notes=[]
	note=mycursor.fetchone()
	while note!=None:
		notes.append(note)
		note = mycursor.fetchone()
	return notes

def append_post(post_name,post_text):
	mycursor = mydb.cursor()
	mycursor.execute("INSERT INTO notes(name,text) VALUES ('%s','%s') "%(post_name,post_text))
	mydb.commit()
	