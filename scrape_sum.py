from playwright.sync_api import sync_playwright
import re

total = 0
base = "https://sanand0.github.io/tdsdata/playwright-table/?seed={}"

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()

    for s in range(3, 13):
        page.goto(base.format(s))

        # wait for tables to render (IMPORTANT)
        page.wait_for_selector("table")

        tables = page.locator("table").all()

        for t in tables:
            nums = re.findall(r"-?\d+", t.inner_text())
            total += sum(int(n) for n in nums)

    browser.close()

print(f"TOTAL_SUM={total}")
