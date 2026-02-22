from playwright.sync_api import sync_playwright
import re

seeds = list(range(3, 13))
base = "https://sanand0.github.io/tdsdata/playwright-table/?seed={}"

total_sum = 0

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()

    for s in seeds:
        page.goto(base.format(s))
        tables = page.locator("table").all()

        for t in tables:
            text = t.inner_text()
            nums = re.findall(r"-?\d+\.?\d*", text)
            total_sum += sum(float(n) for n in nums)

    browser.close()

print(f"TOTAL_SUM={int(total_sum)}")
