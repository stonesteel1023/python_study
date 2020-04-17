import winsound
import sqlite3 as s3, datetime

# winsound.PlaySound('./sound/OK.wav', winsound.SND_FILENAME)
# winsound.PlaySound('./sound/NG.wav', winsound.SND_FILENAME)

conn = s3.connect('D:\py_workspace\pyDB\Game\game.db', isolation_level=None)

cursor = conn.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS records(\
    id integer primary key autoincrement, OK_cnt integer, NG_cnt integer, record text, regdate text)")

cursor.execute("INSERT INTO records('OK_cnt', 'NG_cnt', 'record', 'regdate') VALUES (?, ?, ?, ?)", \
    (0, 1, 'NG', datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')))

conn.close()