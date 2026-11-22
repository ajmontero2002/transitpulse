import sqlite3

DB_PATH = "transit.db"

def init_db():
    conn = sqlite3.connect(DB_PATH)
    conn.execute("""
        CREATE TABLE IF NOT EXISTS vehicle_positions (
            vehicle_id TEXT,
            route_id TEXT,
            latitude REAL,
            longitude REAL,
            timestamp INTEGER

            )
    """)
    conn.commit()
    conn.close()

def save_vehicles(rows):
    conn = sqlite3.connect(DB_PATH)
    conn.executemany(
        "INSERT INTO vehicle_positions VALUES (?, ?, ?, ?, ?)", 
        rows,
    )
    conn.commit()
    conn.close()