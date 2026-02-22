from playwright.sync_api import sync_playwright
import re

seeds = range(3, 13)
base = "https://sanand0.github.io/tdsdata/playwright-table/?seed={}"

total = 0

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()

    for s in seeds:
        page.goto(base.format(s))
        tables = page.locator("table").all()

        for t in tables:
            nums = re.findall(r"-?\d+\.?\d*", t.inner_text())
            total += sum(float(n) for n in nums)

    browser.close()

print(f"TOTAL_SUM={int(total)}")
