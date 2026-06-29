from playwright.async_api import async_playwright
import asyncio
import json

async def get_browser():
    playwright = await async_playwright().start()
    browser = await playwright.chromium.launch(headless=True)
    return playwright, browser

async def save_results(data, filename):
    with open(f"output/{filename}", "w") as f:
        json.dump(data, f, indent=2)
    print(f"[Scraper] Saved {len(data)} records to output/{filename}")
