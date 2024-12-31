
# Freelancer Invoice Reminder System

A simple, automated tool designed to help freelancers manage invoices, track payments, and send reminders to clients when invoices are due.

## Project Description

Freelancers often face the challenge of managing multiple invoices and ensuring timely payments from clients. This system automates the process of:
- Adding invoices with client details and due dates.
- Keeping track of pending invoices.
- Sending email reminders when invoices are approaching their due dates.

It provides both a **REST API** for web-based interaction and a **Command-Line Interface (CLI)** for those who prefer working directly in the terminal.

## Features

- **Add Invoices**: Add a new invoice with client name, amount, due date, and contact email.
- **List Pending Invoices**: View all unpaid invoices that are still pending.
- **Mark Invoices as Paid**: Update the invoice status when payment is made.
- **Send Payment Reminders**: Automatically send email reminders for invoices that are about to expire (3 days before due date).

## Technology Stack

- **Python** 3.x
- **Flask**: A lightweight framework for the REST API.
- **SQLite3**: A simple, serverless database for storing invoices.
- **SMTP** (via Python's `smtplib`): Used for sending email reminders.
- **python-dotenv**: Used for loading environment variables (like email credentials).

## Installation

Follow these steps to get your environment set up:

### 1. Clone the repository

```bash
git clone https://github.com/your-username/freelancer-invoice-reminder.git
cd freelancer-invoice-reminder
```

### 2. Create a virtual environment

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scriptsctivate`
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Set up environment variables

Create a `.env` file in the root directory and add your email credentials:

```
EMAIL_USER=your-email@gmail.com
EMAIL_PASS=your-email-password
```

> **Note:** Make sure to use an app-specific password if you're using Gmail with two-factor authentication.

### 5. Run the app

- **For REST API:**

```bash
python app.py
```

The server will start on `http://localhost:5000`.

- **For CLI:**

```bash
python cli.py --help
```

You can use the CLI to add invoices, list pending invoices, mark invoices as paid, and send email reminders.

## Folder Structure

```
freelancer-invoice-reminder/
├── app.py               # Flask app for the REST API
├── cli.py               # Command-line interface for managing invoices
├── core/
│   ├── database_handler.py   # Database interaction logic
│   ├── email_sender.py       # Email sending logic
│   └── invoice_manager.py    # Business logic for invoice management
├── .env                  # Environment variables for email credentials
├── requirements.txt       # Project dependencies
└── README.md              # This file
```

## API Endpoints

### 1. **Add Invoice** (POST `/add_invoice`)

- **Request Body:**

```json
{
    "client_name": "John Doe",
    "invoice_amount": 500,
    "due_date": "2024-01-15",
    "contact_email": "john@example.com"
}
```

- **Response:**

```json
{
    "message": "Invoice added successfully!"
}
```

### 2. **List Pending Invoices** (GET `/invoices`)

- **Response:**

```json
[
    {
        "id": 1,
        "client_name": "John Doe",
        "invoice_amount": 500,
        "due_date": "2024-01-15",
        "status": "pending",
        "contact_email": "john@example.com"
    },
    ...
]
```

### 3. **Mark Invoice as Paid** (POST `/mark_paid/<invoice_id>`)

- **Response:**

```json
{
    "message": "Invoice marked as paid!"
}
```

## CLI Commands

- **Add an invoice**:
  
```bash
python cli.py --add "John Doe" 500 "2024-01-15" "john@example.com"
```

- **List all pending invoices**:

```bash
python cli.py --list
```

- **Mark an invoice as paid**:

```bash
python cli.py --mark 1
```

- **Send reminders for due invoices**:

```bash
python cli.py --remind
```

## Testing

Run the tests using `pytest` to ensure everything is working properly.

```bash
pytest tests/
```

## Contributions

Feel free to fork this repository and submit pull requests with improvements. Contributions are welcome!

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
