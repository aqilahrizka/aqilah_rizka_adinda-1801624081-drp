from database import get_connection


def create_tables():
    conn = get_connection()
    cursor = conn.cursor()

    # Tabel afirmasi
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS affirmations (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            text TEXT NOT NULL,
            category TEXT NOT NULL
        )
    """)

    # Tabel favorit
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS favorites (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            affirmation_id INTEGER,
            saved_date TEXT,
            FOREIGN KEY (affirmation_id)
                REFERENCES affirmations(id)
        )
    """)

    conn.commit()
    conn.close()

    print("Database dan tabel berhasil dibuat.")


if __name__ == "__main__":
    create_tables()
    