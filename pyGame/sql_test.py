# section 12

# sqllite3 불러오기(파이썬은 기본으로 sqlite3)
import sqlite3 as s3

# version
print(s3.version, s3.sqlite_version)

# datetime
import datetime
now = datetime.datetime.now()
nowDateTime = now.strftime('%Y-%m-%d %H:%M:%S')
print("now : ", now, "-> datetime : ", nowDateTime)

# DB생성 & autocommit 설정
conn = s3.connect('D:\py_workspace\pyDB\database.db', isolation_level=None)

# cursor 획득
cur = conn.cursor()
print(type(cur))

# 테이블생성 text, numeric, integer, real, blob
cur.execute("CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY, \
                                username TEXT, \
                                email TEXT, \
                                phone TEXT, \
                                website TEXT, \
                                regdate TEXT)")

# 테이블에 데이터삽입 - tuple 형식으로도 가능
# cur.execute("INSERT INTO users(id, username, regdate) VALUES (1, 'Choi', ?)", (nowDateTime,))

# Many 삽입
userList = [
    (2, 'Lee2', 'lee2@naver.com', '010-2222-2222', 'lee2.com', nowDateTime),
    (3, 'Lee3', 'lee3@google.com', '010-3333-3333', 'lee3.com', nowDateTime),
    (4, 'Lee4', 'lee4@yahoo.com', '010-4444-4444', 'lee4.com', nowDateTime),
    (5, 'Lee5', 'lee5@facebook.com', '010-5555-5555', 'lee5.com', nowDateTime),
]

# cur.executemany("INSERT INTO users(id, username, email, phone, website, regdate) \
#    VALUES (?, ?, ?, ?, ?, ?)", userList)

# 데이터 삭제
# cur.execute("DELETE FROM users WHERE id = 1")
print("users db deleted : ", cur.execute("DELETE FROM users WHERE id = 1").rowcount)

# isolation_level = None 일 경우 자동커밋
# 수동 커밋/롤백
# conn.commit()
# conn.rollback()

# 접속해제
conn.close()