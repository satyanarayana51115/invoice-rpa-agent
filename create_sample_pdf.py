from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import os

os.makedirs("invoices", exist_ok=True)
pdf_path = os.path.join("invoices", "sample_invoice.pdf")

c = canvas.Canvas(pdf_path, pagesize=letter)
c.setFont("Helvetica-Bold", 16)
c.drawString(200, 750, "TAX INVOICE")

c.setFont("Helvetica", 12)
c.drawString(50, 700, "Invoice Number: INV-2026-9081")
c.drawString(50, 680, "Invoice Date: 21-10-2026")
c.drawString(50, 660, "Billed To: Tirumala Enterprises")

c.drawString(50, 600, "Item: Spare Parts Kit")
c.drawString(250, 600, "Qty: 2")
c.drawString(350, 600, "Rate: 7500.00")

c.setFont("Helvetica-Bold", 12)
c.drawString(50, 520, "Total Amount: 15000.00")

c.save()
print(f"Sample invoice successfully generated at: {pdf_path}")