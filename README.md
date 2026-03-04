# URL Finder

A lightweight Google search scraper that collects URLs for a given query using Selenium. Built as the first stage of a lead-generation pipeline — feeding URLs into a downstream web scraper for contact and institution extraction.

## What it does

Given a search query (e.g. `"Quantum research center director"`), it:

1. Opens a Chrome browser via Selenium
2. Paginates through Google search results
3. Collects up to N result URLs
4. Returns them as a clean list for further processing

## Setup

**Install dependencies:**
```bash
pip install selenium webdriver-manager
```

> `webdriver-manager` handles ChromeDriver installation automatically — no manual driver path needed.

## Usage

Edit the query at the bottom of `url_finder.py`:

```python
query = "Quantum research center director"
results = scrape_google_search(query, num_results=20)
```

Then run:
```bash
python url_finder.py
```

URLs are printed to stdout and can be piped into downstream scripts.

## Function reference

```python
scrape_google_search(query: str, num_results: int = 20) -> list[str]
```

| Parameter     | Description                        | Default |
|--------------|------------------------------------|---------|
| `query`      | The Google search query            | —       |
| `num_results`| Maximum number of URLs to return   | `20`    |

## Pipeline context

```
URL Finder  →  WebScraper  →  Lead Enrichment Pipeline
```

This script feeds into [WebScraper](https://github.com/BVarvill/WebScraper), which extracts institution names, research centres, and director names from each URL.
