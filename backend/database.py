import sqlite3

conn = sqlite3.connect("users.db", check_same_thread=False)
cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS preferences (
    user_id TEXT,
    preference TEXT
)
""")

def save_user_preference(user, preference):
    cur.execute("INSERT INTO preferences VALUES (?,?)", (user, preference))
    conn.commit()

def get_user_preferences(user):
    cur.execute(
        "SELECT preference FROM preferences WHERE user_id = ?",
        (user,)
    )
    rows = cur.fetchall()
    return [row[0] for row in rows]