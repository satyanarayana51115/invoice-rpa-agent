import re
import pdfplumber
from typing import Dict, Any, List, Optional


class InvoiceParser:
    """Zero-LLM / Heuristic and Regex based Invoice Parser."""

    def __init__(self, pdf_path: str):
        self.pdf_path = pdf_path
        self.raw_text = ""

    def extract_text(self) -> str:
        """Extract full plain text from all PDF pages."""
        text_pages = []
        with pdfplumber.open(self.pdf_path) as pdf:
            for page in pdf.pages:
                page_text = page.extract_text()
                if page_text:
                    text_pages.append(page_text)
        self.raw_text = "\n".join(text_pages)
        return self.raw_text

    def parse_invoice_number(self) -> Optional[str]:
        """Extract invoice or bill number using precise regex patterns."""
        patterns = [
            # Matches: Invoice No: INV-2026-0042, Invoice #: 12345, Inv No. ABCD
            r"(?i)invoice\s*(?:no|number|#)[\s.:]*([A-Z0-9\-\/]+)",
            r"(?i)bill\s*(?:no|number|#)[\s.:]*([A-Z0-9\-\/]+)",
            r"(?i)inv\s*#[\s.:]*([A-Z0-9\-\/]+)",
            r"(?i)invoice\s*[:#]\s*([A-Z0-9\-\/]+)"
        ]
        for pattern in patterns:
            match = re.search(pattern, self.raw_text)
            if match:
                val = match.group(1).strip()
                # Ignore if it matched pure English words like 'INVOICE' itself
                if val.lower() not in ["invoice", "bill", "tax"]:
                    return val
        return None

    def parse_date(self) -> Optional[str]:
        """Extract invoice date in common formats."""
        patterns = [
            r"(?i)(?:invoice\s*date|date|dated)[:.\s]*(\d{1,2}[\/\-\.]\d{1,2}[\/\-\.]\d{2,4})",
            r"(?i)(?:date)[:.\s]*(\d{4}[\/\-\.]\d{1,2}[\/\-\.]\d{1,2})",
        ]
        for pattern in patterns:
            match = re.search(pattern, self.raw_text)
            if match:
                return match.group(1).strip()
        return None

    def parse_total_amount(self) -> Optional[float]:
        """Extract total payable amount."""
        patterns = [
            r"(?i)(?:grand\s*total|net\s*total|total\s*amount|total)[:\s]*(?:₹|rs\.?|inr|\$)?\s*([\d,]+\.?\d*)",
        ]
        for pattern in patterns:
            matches = re.findall(pattern, self.raw_text)
            if matches:
                clean_value = matches[-1].replace(",", "").strip()
                try:
                    return float(clean_value)
                except ValueError:
                    continue
        return None

    def extract_line_items(self) -> List[Dict[str, Any]]:
        """Extract table items (Description, Quantity, Unit Price, Amount)."""
        line_items = []
        with pdfplumber.open(self.pdf_path) as pdf:
            for page in pdf.pages:
                tables = page.extract_tables()
                for table in tables:
                    for row in table:
                        # Skip empty rows or header rows
                        if not row or len(row) < 3:
                            continue
                        clean_row = [str(col).strip() if col else "" for col in row]
                        
                        # Heuristic: Check if row contains price-like numeric digits
                        has_number = any(re.search(r"\d+\.?\d*", col) for col in clean_row)
                        header_keywords = ["description", "item", "qty", "quantity", "price", "amount"]
                        is_header = any(keyword in clean_row[0].lower() for keyword in header_keywords)

                        if has_number and not is_header:
                            line_items.append({
                                "raw_row": clean_row
                            })
        return line_items

    def parse_all(self) -> Dict[str, Any]:
        """Parse all invoice attributes into a structured dictionary."""
        if not self.raw_text:
            self.extract_text()

        return {
            "invoice_number": self.parse_invoice_number(),
            "invoice_date": self.parse_date(),
            "total_amount": self.parse_total_amount(),
            "items": self.extract_line_items(),
        }