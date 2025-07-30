import time
import base64
from io import BytesIO
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


class PdfGenerator:
    """
    A simple class to generate PDF files from any public or authenticated webpage URL using headless Chrome.
    """

    SUPPORTED_SIZES = {
        "A4": [8.27, 11.69],
        "LETTER": [8.5, 11],
        "LEGAL": [8.5, 14],
        "A3": [11.69, 16.54],
    }

    def __init__(self, access_token=None, is_authenticated=False, page_size="A4", domain=None):
        """
        :param access_token: Optional. JWT or session token to be passed as a cookie.
        :param is_authenticated: Set to True to attach the token to domain.
        :param page_size: Page size in A4, LETTER, LEGAL, or A3 (default: A4).
        :param domain: Optional. Used to preload the base domain for cookie injection.
        """
        self.access_token = access_token
        self.is_authenticated = is_authenticated
        self.page_size = page_size.upper()
        self.domain = domain
        self._validate_page_size()

    def _validate_page_size(self):
        if self.page_size not in self.SUPPORTED_SIZES:
            raise ValueError(
                f"Unsupported page size '{self.page_size}'. "
                f"Supported sizes: {', '.join(self.SUPPORTED_SIZES.keys())}"
            )

    def generate_pdf_from_url(self, url: str) -> BytesIO:
        chrome_options = ChromeOptions()
        chrome_options.add_argument("--headless=new")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--window-size=1920,1080")
        chrome_options.add_argument("--print-to-pdf-no-header")

        driver = webdriver.Chrome(
            service=ChromeService(ChromeDriverManager().install()),
            options=chrome_options
        )

        try:
            # Step 1: Load base domain to allow cookies if authentication is required
            if self.is_authenticated and self.access_token and self.domain:
                driver.get(f"https://{self.domain}/")
                time.sleep(1)
                driver.add_cookie({
                    "name": "access_token",
                    "value": self.access_token,
                    "path": "/",
                    "domain": self.domain
                })

            # Step 2: Load target page
            driver.get(url)
            time.sleep(2)

            # Step 3: Generate PDF
            width, height = self.SUPPORTED_SIZES[self.page_size]
            pdf_data = driver.execute_cdp_cmd("Page.printToPDF", {
                "paperWidth": width,
                "paperHeight": height,
                "printBackground": True
            })

            return BytesIO(base64.b64decode(pdf_data["data"]))

        finally:
            driver.quit()
