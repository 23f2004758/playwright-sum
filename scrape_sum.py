from playwright.sync_api import sync_playwright
import re

total = 0
base = "https://sanand0.github.io/tdsdata/playwright-table/?seed={}"

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()

    for s in range(3, 13):
        page.goto(base.format(s), wait_until="networkidle")

        # read full rendered page text
        text = page.inner_text("body")

        nums = re.findall(r"-?\d+", text)
        total += sum(int(n) for n in nums)

    browser.close()

print(f"SUM={total}")
