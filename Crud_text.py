import mysql.connector as sql
import os

dataframe = sql.connect(host="localhost", user="root",password="")

kursor = dataframe.cursor()

batas = 0

input("Input your name database and tabel")

database = input("Your name db be like : ")
table_name = input("your table: ")


def MembuatDatabase(dataframe):
	kursor.execute("CREATE DATABASE {}".format(database))
	print("Database can be made")

def MembuatTable():
	dataframes = sql.connect(host="localhost", database="{}".format(database), user="root", password="")
	kurs = dataframes.cursor()

	creating = """CREATE TABLE {} (id_mhs INT AUTO_INCREMENT PRIMARY KEY,
				NIM VARCHAR(255), NAMA VARCHAR(255), ASAL VARCHAR(255))""".format(table_name)
	kurs.execute(creating)
	print("Succesfully for table")

def InsertDb():
	global batas
	dataframes = sql.connect(host="localhost", database="{}".format(database), user="root", password="")
	kurs = dataframes.cursor()
	while batas <= 3:
		nim_mhs = str(input("how many ur nim: "))
		nama_mhs = str(input("who will your name input: "))
		asal_mhs = str(input("where she/he come from: "))
		value = (nim_mhs,nama_mhs,asal_mhs)
		mysql_db = "INSERT INTO {} (NIM,NAMA,ASAL) VALUES (%s,%s,%s)".format(table_name)
		kurs.execute(mysql_db,value)
		batas +=1
	dataframes.commit()
	print("{} data succesed append".format(kurs.rowcount))

def ShownData():
	dataframes = sql.connect(host="localhost", database="{}".format(database), user="root", password="")
	kurs = dataframes.cursor()

	show = "SELECT*FROM {}".format(table_name)
	kurs.execute(show)

	output = kurs.fetchall()

	if kurs.rowcount < 0:
		print("No have data")
	else:
		for showing in output:
			print(showing)

def UpdateData():
	dataframes = sql.connect(host="localhost", database="{}".format(database), user="root", password="")
	kurs = dataframes.cursor()

	ShownData()
	id_some = input("Which one id: ")
	nim_mhs = input("input nim: ")
	nama_mhs = input("input name: ")
	asal_mhs = input("input come from: ")

	update_sql = "UPDATE {} SET NIM=%s, NAMA=%s, ASAL=%s WHERE id_mhs=%s".format(table_name)
	val = (nim_mhs,nama_mhs,asal_mhs,id_some)
	kurs.execute(update_sql,val)
	dataframes.commit()
	print("{} data succesfully changed".format(kurs.rowcount))

def DeleteData():
	dataframes = sql.connect(host="localhost", database="{}".format(database), user="root", password="")
	kurs = dataframes.cursor()

	ShownData()
	id_some = input("which id: ")
	delete = "DELETE FROM {} WHERE id_mhs=%s".format(table_name)
	val = (id_some, )
	kurs.execute(delete,val)
	dataframes.commit()
	print("{} data succesfully delete".format(kurs.rowcount))

def SearchData():
	dataframes = sql.connect(host="localhost", database="{}".format(database), user="root", password="")
	kurs = dataframes.cursor()

	key = input("input keywoard: ")
	search = "SELECT*FROM {} WHERE NAMA LIKE %s or NIM LIKE %s".format(table_name)
	val = ("%{}%".format(key), "%{}%".format(key))
	kurs.execute(search,val)
	hasil = kurs.fetchall()

	if kurs.rowcount <0:
		print("no data in here")
	else:
		for data in hasil:
			print(data)

def show_menu(dataframe):
	print("---> Database Control <---")
	print("1. Make a Database")
	print("2  Make a tabel")
	print("3. Insert Data")
	print("4. Show Data")
	print("5. Update Data")
	print("6. Delete Data")
	print("7. Search Data")
	print("0. Out")
	print("------------------")
	menu = input("Pilih menu: ")

	

	if menu == "1":
		MembuatDatabase(dataframe)
	elif menu == "2":
		MembuatTable()
	elif menu == "3":
		InsertDb()
	elif menu == "4":
		ShownData()
	elif menu == "5":
		UpdateData()
	elif menu == "6":
		DeleteData()
	elif menu == "7":
		SearchData()
	elif menu == 0:
		sys.exit()
	else:
		print("Menu tidak tercantum :)")

if __name__ == "__main__":
	while True:
		show_menu(dataframe)

