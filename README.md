# Market Intelligence Agent

An OpenClaw-powered competitor monitoring agent that scrapes ad libraries, tracks social trends, and delivers a weekly AI-generated brief via Claude.

## What It Does

1. **Scrapes** competitor Facebook Ad Library and TikTok Creative Center using Playwright
2. **Tracks** trending content by category across social platforms
3. **Processes** raw scrape data through a Python pipeline
4. **Summarizes** using Claude API into a structured weekly intelligence brief
5. **Delivers** the brief as a formatted Markdown report

## Architecture

```
Playwright Scraper (Facebook Ad Library, TikTok)
    |
    v
Python Data Processor (dedup, normalize, score)
    |
    v
Claude API (claude-sonnet-4-6)
    |
    v
/output/weekly-brief-YYYY-MM-DD.md
    |
    v
Slack / Email Delivery
```

## Tech Stack

- **OpenClaw** — agent orchestration
- **Python 3.11** — data processing pipeline
- **Claude API** (claude-sonnet-4-6) — brief generation
- **Playwright** — headless browser scraping

## Folder Structure

```
market-intelligence-agent/
├── scrapers/
│   ├── fb_ad_library.py
│   ├── tiktok_creative.py
│   └── base_scraper.py
├── prompts/
│   └── weekly-brief-prompt.txt
├── output/
│   └── sample-brief.md
├── requirements.txt
├── .env.example
└── README.md
```

## Setup

```bash
git clone https://github.com/jamshaidahmedd/market-intelligence-agent
cd market-intelligence-agent
python -m venv venv && source venv/bin/activate
pip install -r requirements.txt
playwright install chromium
cp .env.example .env
python scrapers/fb_ad_library.py
```

## Sample Output

See /output/sample-brief.md for a full example weekly brief.

**Brief excerpt:**
> **Top Competitor Move:** BrandX launched 14 new video ads this week focused on "daily ritual" messaging. Engagement rate on these creatives is 2.3x their Q1 average.

## License

MIT
