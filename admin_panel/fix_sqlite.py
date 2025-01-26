import sqlite3

# Указать путь к файлу базы данных
db_path = 'db.sqlite3'

conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# Проверка данных в таблице
cursor.execute("SELECT * FROM admin_panel_service")
rows = cursor.fetchall()

for row in rows:
    print(row)

# Удаление некорректных данных (если нужно)
cursor.execute("DELETE FROM admin_panel_service WHERE category_id = 'Хирургия'")
conn.commit()

conn.close()
print("Некорректные записи удалены.")
