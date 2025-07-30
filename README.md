# selenium-pdf-generator

Generate high-quality PDFs from any public or authenticated webpage using Selenium and headless Chrome.



---

## 🚀 Overview

This package lets you render full-page PDFs using Chrome’s DevTools Protocol via Selenium. It supports public pages and authenticated routes — perfect for dashboards, reports, invoices, etc.

---

## ✅ Features

- 🔒 Authenticated route support using cookies or JWT tokens
- 🧾 Headless Chrome print-to-PDF rendering
- 🖨️ Support for multiple page sizes: `A4`, `Letter`, `Legal`, `A3`
- ⚙️ Fully configurable and reusable in Django, FastAPI, Flask
- 🚀 Supports secure PyPI publishing using GitHub Trusted Publisher

---

## 📦 Installation

```bash
pip install selenium-pdf-generator

```
## 🧪 Usage
```bash
from selenium_pdf_generator import PdfGenerator

generator = PdfGenerator(
    access_token="your-access-token",   # Optional
    is_authenticated=True,              # True if page requires auth
    page_size="A4"                      # A4, Letter, Legal, A3
)

pdf_io = generator.generate_pdf_from_url("https://yourdomain.com/protected-page")

with open("report.pdf", "wb") as f:
    f.write(pdf_io.read())
```


