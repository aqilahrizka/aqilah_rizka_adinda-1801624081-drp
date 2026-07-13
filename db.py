from database import get_connection


def create_tables():
    conn = get_connection()
    cursor = conn.cursor()

    # =========================
    # Tabel Categories
    # =========================
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS categories (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL UNIQUE
        )
    """)

    # =========================
    # Tabel Affirmations
    # =========================
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS affirmations (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            text TEXT NOT NULL,
            category_id INTEGER NOT NULL,
            FOREIGN KEY (category_id)
                REFERENCES categories(id)
        )
    """)

    # =========================
    # Tabel Favorites
    # =========================
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS favorites (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            affirmation_id INTEGER,
            saved_date TEXT,
            FOREIGN KEY (affirmation_id)
                REFERENCES affirmations(id)
        )
    """)

    # Menambahkan kategori jika belum ada
    cursor.executemany("""
        INSERT OR IGNORE INTO categories(name)
        VALUES (?)
    """, [
        ("Motivasi",),
        ("Percaya Diri",),
        ("Mental",)
    ])

    conn.commit()
    conn.close()

    print("Database dan tabel berhasil dibuat.")


if __name__ == "__main__":
    create_tables()
    