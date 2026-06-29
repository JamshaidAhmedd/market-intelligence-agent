import asyncio
from base_scraper import get_browser, save_results

async def scrape_tiktok_trends():
    playwright, browser = await get_browser()
    page = await browser.new_page()
    print("[TikTok Scraper] Fetching trending creatives...")
    await page.goto("https://ads.tiktok.com/business/creativecenter/inspiration/topads/pc/en", wait_until="networkidle")
    trends = []
    await browser.close()
    await playwright.stop()
    await save_results(trends, "tiktok_trends_raw.json")
    return trends

if __name__ == "__main__":
    asyncio.run(scrape_tiktok_trends())
