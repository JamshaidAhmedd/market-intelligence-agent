import asyncio
from base_scraper import get_browser, save_results

TARGET_PAGE = "example-competitor-brand"
AD_LIBRARY_URL = "https://www.facebook.com/ads/library/?active_status=active&ad_type=all&search_type=page"

async def scrape_fb_ads():
    playwright, browser = await get_browser()
    page = await browser.new_page()
    print(f"[FB Scraper] Navigating to Ad Library for: {TARGET_PAGE}")
    await page.goto(AD_LIBRARY_URL, wait_until="networkidle")
    ads = []
    await browser.close()
    await playwright.stop()
    await save_results(ads, "fb_ads_raw.json")
    return ads

if __name__ == "__main__":
    asyncio.run(scrape_fb_ads())
