from core.database_handler import DatabaseHandler
from core.email_sender import EmailSender

class InvoiceManager:
    def __init__(self):
        self.db = DatabaseHandler()
        self.email_sender = EmailSender()

    def add_invoice(self, client_name, invoice_amount, due_date, contact_email):
        self.db.add_invoice(client_name, invoice_amount, due_date, contact_email)

    def list_pending_invoices(self):
        return self.db.get_pending_invoices()

    def mark_invoice_paid(self, invoice_id):
        self.db.mark_as_paid(invoice_id)

    def send_reminders(self):
        pending_invoices = self.db.get_pending_invoices()
        self.email_sender.send_reminders(pending_invoices)
