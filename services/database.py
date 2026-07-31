import sqlite3


def get_connection():
    conn = sqlite3.connect("database/insightbridge.db")
    conn.row_factory = sqlite3.Row
    return conn


def initialize_database():

    conn = get_connection()

    conn.execute("""
        CREATE TABLE IF NOT EXISTS analyses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            company_name TEXT NOT NULL,
            overview TEXT NOT NULL
        )
    """)

    conn.commit()
    conn.close()


def save_analysis(company, overview):

    conn = get_connection()

    conn.execute(
        """
        INSERT INTO analyses (
            company_name,
            overview
        )
        VALUES (?, ?)
        """,
        (company, overview)
    )

    conn.commit()
    conn.close()


def get_all_analyses():

    conn = get_connection()

    analyses = conn.execute(
        """
        SELECT *
        FROM analyses
        ORDER BY id DESC
        """
    ).fetchall()

    conn.close()

    return analyses