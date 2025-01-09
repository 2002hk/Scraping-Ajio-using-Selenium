# selenium 4
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
import time
import pandas as pd
import os



driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get('https://www.ajio.com/s/grooming-4384-57431?query=%3Arelevance%3Agenderfilter%3AWomen&curated=true&curatedid=grooming-4384-57431&gridColumns=3&segmentIds=')
time.sleep(2)
#scrolling down to load all products
height=driver.execute_script("return document.body.scrollHeight")
#print(height)
# intializing infinite loop
'''
while True:
    print("Page length scrolled", height)
    # scroll to the bottom of the page
    driver.execute_script("window.scroll(0,document.body.scrollHeight)")
    time.sleep(2)
    #if the additional content is loaded the height will increase
    new_height=driver.execute_script("return document.body.scrollHeight")
    # if the old height == new height means no additional content is loaded that means scrolling completed break loop
    if new_height==height:
        break
    #new_height will bw stored in height
    height=new_height
print("Scrolling Completed")
'''

# Locate all parent containers of the Products
product_containers=driver.find_elements(By.XPATH, '//div[@class="preview"]')
#print(product_containers)
#initialize dataset and counter for missing products
filtered_data=[]
no_of_missing_elements=0
for container in product_containers:
    #print(container.text)
    try:
        #extract brand name rating price
        brand=container.find_element(By.XPATH,'.//div[@class="brand"]//strong').text.strip()
        print(brand)
        name=container.find_element(By.XPATH,'.//div[@class="nameCls"]').text.strip()
        print(name)
        rating=container.find_element(By.XPATH,'.//div[@class="_1gIWf"]//p[@class="_3I65V"]').text.strip()
        print(rating)
        price=container.find_element(By.XPATH,'.//span[@class="price  "]//strong').text.strip()
        print(price)
        #append data
        filtered_data.append({
            'Brand':brand,
            'Name':name,
            'Rating':rating,
            'Price':price
        })
    except Exception as e:
        no_of_missing_elements+=1
print(filtered_data)
print(f"No of scraped products{len(filtered_data)}")
print(f"No of missing products{no_of_missing_elements}")

df=pd.DataFrame(filtered_data)
os.makedirs('output',exist_ok=True)
output_path='output/ajio_women_grooming_products.csv'
df.to_csv(output_path,index=False)


driver.close()
driver.quit()
