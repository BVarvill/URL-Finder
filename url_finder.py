"""
URL Finder
----------
Searches Google for a given query and collects up to N result URLs.
Uses Selenium with ChromeDriver to handle dynamic pages.

Usage:
    python url_finder.py

Requirements:
    pip install selenium webdriver-manager
"""

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time


def scrape_google_search(query: str, num_results: int = 20) -> list[str]:
    """
    Search Google for `query` and return up to `num_results` URLs.

    Args:
        query:       The search query string.
        num_results: Maximum number of URLs to collect.

    Returns:
        A list of result URLs.
    """
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)

    driver.get(f"https://www.google.com/search?q={query}")
    urls = []

    while len(urls) < num_results:
        try:
            results = driver.find_elements(By.XPATH, "//a[h3]")
            for result in results:
                url = result.get_attribute("href")
                if url and url not in urls:
                    urls.append(url)
                if len(urls) >= num_results:
                    break

            try:
                next_button = driver.find_element(By.XPATH, "//a[@id='pnnext']")
                next_button.click()
                time.sleep(2)
            except Exception:
                print("No more pages available or 'Next' button not found.")
                break

        except Exception as e:
            print(f"Error encountered: {e}")
            break

    driver.quit()
    return urls


if __name__ == "__main__":
    query = "Quantum research center director"
    results = scrape_google_search(query, num_results=20)
    for url in results:
        print(url)
