import os
from pathlib import Path
from src.parser import InvoiceParser
from src.rpa_bot import ERPAutomationBot


def run_pipeline():
  invoice_file = os.path.join("invoices", "sample_invoice.pdf")

  if not os.path.exists(invoice_file):
    print(f"[ERROR] Target file not found: {invoice_file}")
    return

  print("Step 1: Parsing invoice using Pure Engineering / Regex...")
  parser = InvoiceParser(invoice_file)
  extracted_data = parser.parse_all()

  print("[INFO] Extracted Data:")
  for key, value in extracted_data.items():
    print(f"  - {key}: {value}")

  print("\nStep 2: Submitting data via Playwright...")

  # Use local mock ERP page instead of dummy internet url
  local_html_path = Path("mock_erp.html").resolve().as_uri()

  bot = ERPAutomationBot(target_url=local_html_path, headless=False)
  bot.submit_invoice(extracted_data)


if __name__ == "__main__":
  run_pipeline()