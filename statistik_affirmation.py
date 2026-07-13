from database import get_connection


def tampilkan_statistik():
    conn = get_connection()
    cursor = conn.cursor()

    # Total afirmasi
    cursor.execute("SELECT COUNT(*) FROM affirmations")
    total_afirmasi = cursor.fetchone()[0]

    # Total favorit
    cursor.execute("SELECT COUNT(*) FROM favorites")
    total_favorit = cursor.fetchone()[0]

    # Statistik per kategori
    cursor.execute("""
        SELECT
            categories.name AS category,
            COUNT(affirmations.id) AS jumlah
        FROM categories
        LEFT JOIN affirmations
            ON categories.id = affirmations.category_id
        GROUP BY categories.id
        ORDER BY categories.id
    """)

    kategori = cursor.fetchall()

    print("\n========== STATISTIK ==========")
    print(f"Total Afirmasi : {total_afirmasi}")
    print(f"Total Favorit  : {total_favorit}")

    print("\nJumlah Afirmasi per Kategori")
    print("-" * 30)

    for item in kategori:
        print(f"{item['category']} : {item['jumlah']}")

    print("=" * 30)

    conn.close()


if __name__ == "__main__":
    tampilkan_statistik()
    