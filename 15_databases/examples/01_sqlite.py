"""\nSQLite\n\n"""\n\nimport sqlite3

with sqlite3.connect("learning.db") as conn:
    conn.execute("CREATE TABLE IF NOT EXISTS students (id INTEGER PRIMARY KEY, name TEXT)")
    conn.execute("INSERT INTO students (name) VALUES (?)", ("Learner",))
    for row in conn.execute("SELECT id, name FROM students"):
        print(row)\n