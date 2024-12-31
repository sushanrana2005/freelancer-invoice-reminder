import sqlite3

class DatabaseHandler:
    DB_NAME = "invoices.db"

    def __init__(self):
        self.initialize_db()

    def initialize_db(self):
        with sqlite3.connect(self.DB_NAME) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS invoices (
                    id INTEGER PRIMARY KEY,
                    client_name TEXT,
                    invoice_amount REAL,
                    due_date TEXT,
                    contact_email TEXT,
                    status TEXT DEFAULT 'pending'
                )
            ''')
            conn.commit()

    def add_invoice(self, client_name, invoice_amount, due_date, contact_email):
        with sqlite3.connect(self.DB_NAME) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO invoices (client_name, invoice_amount, due_date, contact_email)
                VALUES (?, ?, ?, ?)
            ''', (client_name, invoice_amount, due_date, contact_email))
            conn.commit()

    def get_pending_invoices(self):
        with sqlite3.connect(self.DB_NAME) as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM invoices WHERE status = "pending"')
            return cursor.fetchall()

    def mark_as_paid(self, invoice_id):
        with sqlite3.connect(self.DB_NAME) as conn:
            cursor = conn.cursor()
            cursor.execute('UPDATE invoices SET status = "paid" WHERE id = ?', (invoice_id,))
            conn.commit()
