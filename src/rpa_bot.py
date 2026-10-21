import os
from typing import Any, Dict
from playwright.sync_api import sync_playwright


class ERPAutomationBot:
  """Automates form filling in web-based ERP systems using Playwright."""

  def __init__(self, target_url: str, headless: bool = False):
    self.target_url = target_url
    self.headless = headless

  def submit_invoice(
      self,
      data: Dict[str, Any],
      proof_path: str = "proofs/submitted_invoice.png",
  ) -> bool:
    """Fills and submits invoice data into the ERP web portal smoothly."""
    os.makedirs(os.path.dirname(proof_path), exist_ok=True)

    with sync_playwright() as p:
      # Launch browser
      browser = p.chromium.launch(headless=self.headless)

      # Fixed viewport for visual consistency
      context = browser.new_context(viewport={"width": 1280, "height": 720})
      page = context.new_page()

      try:
        print(f"[RPA] Navigating to: {self.target_url}")
        page.goto(self.target_url, timeout=30000)

        # Type Invoice Number
        if data.get("invoice_number"):
          field = page.locator(
              'input[name="invoice_no"], #invoice_number'
          ).first
          field.click()
          field.press_sequentially(data["invoice_number"], delay=100)

        # Type Invoice Date
        if data.get("invoice_date"):
          field = page.locator(
              'input[name="invoice_date"], #invoice_date'
          ).first
          field.click()
          field.press_sequentially(data["invoice_date"], delay=100)

        # Type Total Amount formatted to 2 decimal places
        if data.get("total_amount") is not None:
          formatted_amount = f"{float(data['total_amount']):.2f}"
          field = page.locator(
              'input[name="total_amount"], #total_amount'
          ).first
          field.click()
          field.fill("")
          field.press_sequentially(formatted_amount, delay=100)

        # Remove focus from input fields
        page.locator("body").click(position={"x": 10, "y": 10})
        page.wait_for_timeout(500)

        # Capture audit proof screenshot of the form card
        form_element = page.locator(".form-card, form").first
        form_element.screenshot(path=proof_path)
        print(f"[RPA] Audit proof screenshot saved at: {proof_path}")

        print("[RPA] Invoice data successfully entered.")

        # Pause briefly to verify the UI before teardown
        page.wait_for_timeout(3000)
        return True

      except Exception as e:
        print(f"[ERROR] Automation failed: {str(e)}")
        page.screenshot(path="proofs/error_snapshot.png")
        return False

      finally:
        browser.close()