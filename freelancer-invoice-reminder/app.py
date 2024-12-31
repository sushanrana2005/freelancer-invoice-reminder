from flask import Flask, request, jsonify
from core.invoice_manager import InvoiceManager

app = Flask(__name__)
manager = InvoiceManager()

@app.route('/add_invoice', methods=['POST'])
def add_invoice():
    data = request.json
    manager.add_invoice(data['client_name'], data['invoice_amount'], data['due_date'], data['contact_email'])
    return jsonify({"message": "Invoice added successfully!"})

@app.route('/invoices', methods=['GET'])
def list_invoices():
    invoices = manager.list_pending_invoices()
    return jsonify(invoices)

@app.route('/mark_paid/<int:invoice_id>', methods=['POST'])
def mark_paid(invoice_id):
    manager.mark_invoice_paid(invoice_id)
    return jsonify({"message": "Invoice marked as paid!"})

if __name__ == "__main__":
    app.run(debug=True)
