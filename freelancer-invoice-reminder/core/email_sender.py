import smtplib
import os
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()

class EmailSender:
    def __init__(self):
        self.email_user = os.getenv('EMAIL_USER')
        self.email_pass = os.getenv('EMAIL_PASS')

    def send_reminders(self, invoices):
        for invoice in invoices:
            due_date = datetime.strptime(invoice[3], "%Y-%m-%d")
            if (due_date - datetime.now()).days <= 3:
                self._send_email(invoice)

    def _send_email(self, invoice):
        with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
            smtp.starttls()
            smtp.login(self.email_user, self.email_pass)
            subject = f"Invoice Reminder: Due Date {invoice[3]}"
            body = f"Dear {invoice[1]},\n\nYour invoice of amount {invoice[2]} is due soon. Please make the payment by {invoice[3]}.\n\nThank you!"
            msg = f"Subject: {subject}\n\n{body}"
            smtp.sendmail(self.email_user, invoice[4], msg)
