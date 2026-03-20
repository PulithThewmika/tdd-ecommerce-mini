import sqlite3
import json
import datetime
from src.order import Order

class SQLiteOrderRepository:
    def __init__(self, db_path=":memory:"):
        self.conn = sqlite3.connect(db_path, check_same_thread=False)
        self.create_tables()

    def create_tables(self):
        with self.conn:
            self.conn.execute("""
                CREATE TABLE IF NOT EXISTS orders (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    total REAL NOT NULL,
                    items_json TEXT NOT NULL,
                    timestamp TEXT NOT NULL
                )
            """)

    def save(self, order):
        items_json = json.dumps(order.items)
        with self.conn:
            cursor = self.conn.execute(
                "INSERT INTO orders (total, items_json, timestamp) VALUES (?, ?, ?)",
                (order.total, items_json, order.timestamp.isoformat())
            )
            return cursor.lastrowid

    def get_all(self):
        cursor = self.conn.execute("SELECT items_json, total, timestamp FROM orders")
        orders = []
        for row in cursor.fetchall():
            items = json.loads(row[0])
            total = row[1]
            o = Order(items, total)
            o.timestamp = datetime.datetime.fromisoformat(row[2])
            orders.append(o)
        return orders
