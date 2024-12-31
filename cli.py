import argparse
from core.invoice_manager import InvoiceManager

manager = InvoiceManager()

def main():
    parser = argparse.ArgumentParser(description="Freelancer Invoice Reminder CLI")
    parser.add_argument("--add", nargs=4, metavar=("client_name", "invoice_amount", "due_date", "contact_email"),
                        help="Add a new invoice")
    parser.add_argument("--list", action="store_true", help="List all pending invoices")
    parser.add_argument("--mark", metavar="invoice_id", type=int, help="Mark an invoice as paid")
    parser.add_argument("--remind", action="store_true", help="Send email reminders for due invoices")
    args = parser.parse_args()

    if args.add:
        manager.add_invoice(*args.add)
        print("Invoice added successfully!")
    elif args.list:
        print(manager.list_pending_invoices())
    elif args.mark:
        manager.mark_invoice_paid(args.mark)
        print(f"Invoice {args.mark} marked as paid!")
    elif args.remind:
        manager.send_reminders()
        print("Reminders sent!")

if __name__ == "__main__":
    main()
