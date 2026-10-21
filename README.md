# ⚡ Zero-LLM Enterprise Invoice RPA Agent

### Autonomous, Deterministic Invoice Extraction & Web ERP Data Entry Engine Built with Python & Playwright

![Python 3.10+](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python)
![Automation](https://img.shields.io/badge/Automation-Playwright-green?logo=playwright)
![Parser](https://img.shields.io/badge/Parser-pdfplumber%20%26%20Regex-orange)
![Architecture](https://img.shields.io/badge/Architecture-Modular%20RPA-purple)
![Cost](https://img.shields.io/badge/Cost-Zero--LLM%20%2F%20Open--Source-success)

---

## 📌 Executive Summary

Enterprise invoice processing often suffers from either excessive licensing fees (e.g., UiPath, Automation Anywhere) or unpredictable operational costs and non-deterministic behavior associated with Large Language Model (LLM) APIs.

**Zero-LLM Enterprise Invoice RPA Agent** eliminates these constraints through pure engineering. It provides an ultra-fast, deterministic, and auditable pipeline that parses semi-structured PDF invoices and automatically commits them into a web-based ERP portal using human-like typing flows and automated visual verification.

---

## 🚀 Key Highlights & Capabilities

* **Deterministic Document Parsing:** Uses `pdfplumber` paired with optimized multi-pattern Regular Expressions (Regex) to extract Invoice Number, Issue Date, and Payable Amount without paying per-token API costs.
* **Human-Emulated Data Entry:** Features human-like sequential keystrokes (`press_sequentially`) to interact reliably with dynamic frontend fields and prevent script-blocking mechanisms.
* **Automated Audit Trail:** Captures clean, focused visual proof screenshots of submitted records into `proofs/` for immediate compliance and accounting reconciliation.
* **High-Speed & Cost-Free:** Executes complete document-to-ERP workflows in sub-second timelines with zero vendor lock-in.

---

## 📂 Project Architecture

```text
invoice-rpa-agent/
├── invoices/
│   └── sample_invoice.pdf      # Target PDF documents
├── proofs/
│   └── submitted_invoice.png   # Audit-trail screenshot proofs
├── src/
│   ├── parser.py               # Deterministic Regex & text extractor
│   └── rpa_bot.py              # Playwright browser automation bot
├── tests/
│   └── test_parser.py          # Pytest validation for regex heuristics
├── mock_erp.html               # Enterprise mock form for local verification
├── main.py                     # Pipeline orchestrator
└── requirements.txt            # Project dependencies
```
## ⚙️ Installation & Setup

1. **Clone the repository:**

```
git clone https://github.com/satyanarayana51115/invoice-rpa-agent.git
cd invoice-rpa-agent
```

2. **Activate Virtual Environment:**

```
python -m venv .venv
.\.venv\Scripts\activate
```

3. **Install Dependencies & Playwright Browsers:**

```
pip install -r requirements.txt
playwright install chromium
```

## 🧪 Testing & Execution

* **Run Regex Extraction Tests:**

```
pytest tests/test_parser.py -v
```

* **Execute Full RPA Pipeline:**

```
python main.py
```

## 🛡️ Engineering Over Hype

​By deliberately substituting stochastic LLMs with deterministic heuristics and solid test coverage, this bot demonstrates that core automation challenges in finance and accounting are best solved with predictable, maintainable, and cost-efficient software design.