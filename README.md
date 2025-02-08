## Scraping Ajio website for women grooming products
## Libraries used
- Selenium
- Pandas
- used single pyhton script to scrape data from ajios website using selenium 
## Setup Selenium & WebDriver
- Uses webdriver_manager to automatically install the Chrome WebDriver.
- Launches a Chrome browser and navigates to the specified Ajio page.
## Scrolling for Dynamic Loading (Commented Out)
- A loop was designed to scroll down the page until all products are loaded. However, it's currently commented out.
## Extracting Product Details
- Finds all product containers using XPath.
## Error Handling
- If an element is missing, it increments no_of_missing_elements instead of breaking.
## Saving Data to CSV
- The extracted data is stored in a Pandas DataFrame.
- Creates an "output" folder if it doesn’t exist.
- Saves the CSV file as ajio_women_grooming_products.csv.
## Closing the WebDriver
- Uses driver.close() and driver.quit() to properly terminate the session.
## Areas for Improvement
- Enable scrolling to load all products dynamically.
- Use WebDriverWait instead of time.sleep() for better performance.
- Handle dynamic elements using try-except with explicit waits.
- Optimize XPath expressions to be more robust.
