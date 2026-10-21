import sys
import os

# Add root directory to sys.path so 'src' can be imported anywhere
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import pytest
from src.parser import InvoiceParser


def test_regex_matching_patterns():
    parser = InvoiceParser(pdf_path="dummy.pdf")
    parser.raw_text = """
    TAX INVOICE
    Invoice No: INV-2026-0042
    Date: 21-10-2026
    Total Amount: 15,450.00
    """

    assert parser.parse_invoice_number() == "INV-2026-0042"
    assert parser.parse_date() == "21-10-2026"
    assert parser.parse_total_amount() == 15450.00