from playwright.sync_api import sync_playwright
from time import perf_counter, sleep


with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://www.nrk.no/spill/kula-1.17599534")

    page.locator(".start-button").click()
    page.locator("#restart-knapp").click()
