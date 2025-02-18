# URL-Finder
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

def scrape_google_search(query, num_results=20):
    driver_path = r"/Users/benvarvill/Downloads/chromedriver-mac-arm64 2/chromedriver"  # Adjust path
    service = Service(driver_path)
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
            except:
                print("No more pages available or 'Next' button not found.")
                break  

        except Exception as e:
            print(f"Error encountered: {e}")
            break  

    driver.quit()
    return urls

query = "Quantum research center director"
search_results = scrape_google_search(query, num_results=20)  # Fetch up to 20 URLs
print(search_results)
