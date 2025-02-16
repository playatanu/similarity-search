import sqlite3


class SqliteDB:
    def __init__(self):
        conn = sqlite3.connect("metadata.db")
        cursor = conn.cursor()

        query = f"CREATE TABLE IF NOT EXISTS images (faiss_id INTEGER PRIMARY KEY AUTOINCREMENT, filename TEXT NOT NULL)"

        cursor.execute(query)
        conn.commit()
        conn.close()

    def store(self, images):
        conn = sqlite3.connect("metadata.db")
        cursor = conn.cursor()

        query = f"INSERT INTO images  (filename) VALUES (?)"
        cursor.executemany(query, [(img,) for img in images])

        query = f"SELECT * FROM images  ORDER BY faiss_id DESC LIMIT ?"
        cursor.execute(query, (len(images),))
        inserted_rows = cursor.fetchall()

        conn.commit()
        conn.close()

        return inserted_rows[::-1]

    def search(self, ids: list[int]):
        conn = sqlite3.connect("metadata.db")
        cursor = conn.cursor()

        query = (
            f"SELECT * FROM images  WHERE faiss_id IN ({','.join(['?'] * len(ids))})"
        )

        cursor.execute(query, tuple(ids))
        row = cursor.fetchall()

        conn.close()

        return row

    def load(self):
        conn = sqlite3.connect("metadata.db")
        cursor = conn.cursor()

        query = f"SELECT * FROM images"

        cursor.execute(query)
        row = cursor.fetchall()

        conn.close()

        return row
