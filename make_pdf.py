import os
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

# Ensure invoices directory exists
os.makedirs("invoices", exist_ok=True)
pdf_path = os.path.join("invoices", "sample_invoice.pdf")

# Generate a clean dummy invoice
c = canvas.Canvas(pdf_path, pagesize=letter)
c.setFont("Helvetica-Bold", 16)
c.drawString(200, 750, "TAX INVOICE")

c.setFont("Helvetica", 12)
c.drawString(50, 700, "Invoice Number: INV-2026-9081")
c.drawString(50, 680, "Invoice Date: 21-10-2026")
c.drawString(50, 660, "Billed To: Customer Name")

c.drawString(50, 600, "Item: Automation Service Kit")
c.drawString(250, 600, "Qty: 1")
c.drawString(350, 600, "Rate: 15000.00")

c.setFont("Helvetica-Bold", 12)
c.drawString(50, 520, "Total Amount: 15000.00")

c.save()
print(f"[SUCCESS] Sample invoice created at: {pdf_path}")