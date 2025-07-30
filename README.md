# selenium-pdf-generator

Generate high-quality PDFs from any public or authenticated webpage using Selenium and headless Chrome.

## 💡 Why I Built This

I often needed to generate PDFs of webpages — dashboards, reports, previews — but struggled with most Python libraries. Tools like `reportlab`, `pdfkit`, and others often fell short when trying to replicate the **exact design of a webpage**.

So I tried using **Selenium + headless Chrome**, and it just worked.

This package wraps that working solution into something reusable and configurable for everyone.



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
## 🔐 Authenticated Page Support
If the webpage uses JWT stored in access_token, the generator will automatically:

- Open the base domain in the browser

- Set a cookie access_token=...

- Load the target URL with auth
```bash

PdfGenerator(is_authenticated=True, access_token="...")
```

## 📐 Page Size Options
| Name     | Dimensions (inches) |
|----------|---------------------|
| `A4`     | 8.27 × 11.69        |
| `Letter` | 8.5 × 11            |
| `Legal`  | 8.5 × 14            |
| `A3`     | 11.69 × 16.54       |

---

## 🙌 Contributing

If you find this useful and have ideas to improve it, feel free to open a Pull Request (PR) or raise an issue.

I'm open to collaboration and happy to enhance this further with the community.


---

