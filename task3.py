from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from datetime import datetime

def create_receipt(transaction_id, date, customer_name, items, total_amount):
    file_name = f"receipt_{transaction_id}.pdf"
    document = canvas.Canvas(file_name, pagesize=letter)
    
    # Set title
    document.setTitle(f"Receipt #{transaction_id}")

    # Add header
    document.setFont("Helvetica-Bold", 20)
    document.drawString(200, 750, "Payment Receipt")
    
    # Add transaction details
    document.setFont("Helvetica", 12)
    document.drawString(50, 720, f"Transaction ID: {transaction_id}")
    document.drawString(50, 700, f"Date: {date}")
    document.drawString(50, 680, f"Customer Name: {customer_name}")

    # Add table headers
    document.drawString(50, 650, "Item")
    document.drawString(300, 650, "Price")
    
    # Add items
    y = 630
    for item, price in items.items():
        document.drawString(50, y, item)
        document.drawString(300, y, f"${price:.2f}")
        y -= 20
    
    # Add total amount
    document.setFont("Helvetica-Bold", 12)
    document.drawString(50, y - 20, f"Total Amount: ${total_amount:.2f}")
    
    # Add footer
    document.setFont("Helvetica", 10)
    document.drawString(50, y - 60, "Thank you for your purchase!")
    
    # Save the PDF
    document.save()
    print(f"Receipt saved as {file_name}")

if __name__ == "__main__":
    transaction_id = "123456"
    date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    customer_name = "John Doe"
    items = {
        "Item 1": 10.99,
        "Item 2": 5.49,
        "Item 3": 7.99
    }
    total_amount = sum(items.values())
    
    create_receipt(transaction_id, date, customer_name, items, total_amount)
