import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    ERP_URL = os.getenv("ERP_PORTAL_URL", "https://example.com/erp/invoices/new")
    USERNAME = os.getenv("ERP_USERNAME", "")
    PASSWORD = os.getenv("ERP_PASSWORD", "")
    HEADLESS = os.getenv("HEADLESS_MODE", "False").lower() == "true"